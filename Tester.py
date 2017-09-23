#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ===========================================================================
# Tester for Project 3 (CS 6250: Computer Networks)
# Run: 'python Tester.py'
# Notes: Make sure that the ALPHABETIZE constant in helper.py is set to TRUE
# 	 Only tested in Linux.
# 
# @author   Carlos Perea (carlos.perea@gatech.edu)
# @date     09/22/2017
# ===========================================================================

import filecmp
import os
from subprocess import check_call

my_dir = os.path.dirname(__file__)
reference_dir = "reference_logs"
devnull = open(os.devnull, 'w')

# Open the file containing the list of topologies to test
tl_file = open('test_list.txt', 'r')

tests = []
for line in tl_file:
    test = line.replace('\r', '').replace('\n', '').strip()
    if len(test):
        tests.append(test)
tl_file.close()

def populate_log_list(file_name):
    ''' Opens a log file and retrieves the last sub-section as a list of lines
    and the total number of lines in the log file.
    - file_name: The file top open '''
    
    log_file = open(file_name)
    list = []
    first_d = False
    lines = log_file.readlines()
    rev_lines = reversed(lines)
    for line in rev_lines:
        if "-----" in line:
            if first_d:
                break
            else:
                first_d = True
                continue
        list.append(line)
    log_file.close()
    return {"lines": list, "total_lines": len(lines)}

tests_total = 0
passed_tests = 0

# Go through all the lines of the file and try to run the project for that topology
for test in tests:
    test_pass = True
    
    check_call(["./run.sh", test], stdout=devnull, stderr=devnull)
    log_file_name = "{filename}.log".format(filename=test)
    ref_file_path = os.path.join(reference_dir, log_file_name)
    
    # Open both log files and store them in lists
    log_data = populate_log_list(log_file_name)
    ref_data = populate_log_list(ref_file_path)
    
    log_line_list = log_data["lines"].replace('\r', '').replace('\n', '')
    ref_line_list = ref_data["lines"].replace('\r', '').replace('\n', '')
    total_num_lines = log_data["total_lines"]
    
    print "Topology: {test_name}".format(test_name=test)
    print "Total lines in log: {num_lines}".format(num_lines=total_num_lines)
    
    if len(log_line_list) == len(ref_line_list):
        for i in range(0, len(log_line_list)):
            # Get the current line in the log files
            log_line = log_line_list[i]
            ref_line = ref_line_list[i]
            
            # Split it by ':' to get the current node and its distance vector
            log_split = log_line.split(":")
            ref_split = ref_line.split(":")
            
            # The node's name
            log_node = log_split[0]
            ref_node = ref_split[0]
            
            if log_node != ref_node:
                test_pass = False
                break
            
            # Split the distance vector by ',' to get the individual nodes and distances
            log_dv = log_split[1].split(",")
            ref_dv = ref_split[1].split(",")
            log_dv.sort()
            ref_dv.sort()
            
            # Check that both distance vectors are the same length
            if len(log_dv) != len(ref_dv):
                test_pass = False
                break
            
            # Go through all the destination nodes and check that they all match
            for j in range(0, len(log_dv)):
                log_dest_node = log_dv[j]
                ref_dest_node = ref_dv[j]
                if log_dest_node != ref_dest_node:
                    test_pass = False
                    break
            
            if not test_pass:
                break
    else:
        test_pass = False
    
    tests_total += 1
    
    if test_pass:
        print "Result: Passed\n".format(test_name=test)
        passed_tests += 1
    else:
        print "Result: Failed\n".format(test_name=test)

# Print the results
total_tests_str = "Total tests: {tests_total}\n".format(tests_total=tests_total)
perc_tests_str = "Percentage pass: {perc_pass}%\n".format(perc_pass=(round((float(passed_tests)/float(tests_total)) * 100)))
passed_test_str = "Passed: {passed_tests}\n".format(passed_tests=passed_tests)
failed_tests_str = "Failed: {failed_tests}".format(failed_tests=tests_total-passed_tests)
print "-----\n{0}{1}{2}{3}".format(total_tests_str, perc_tests_str, passed_test_str, failed_tests_str)
