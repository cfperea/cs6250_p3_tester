# CS 6250: Computer Networks
# Project 3 Tester/Validator

By: Carlos Perea (carlos.perea@gatech.edu)

### What Is This?

Tester.py allows you to automatically test your implementation of DistanceVector.py against a few reference log files. You can also add new test topologies!

The tester is order insensitive for individual lines.

For example:

```VZ:TWC-99,GSAT-6,UGA-99,ATT2,VZ0,CMCT-99,VONA-9```

Is considered the same as:

```VZ:VONA-9,TWC-99,GSAT-6,UGA-99,ATT2,VZ0,CMCT-99```

### IMPORTANT

This code is not endorsed nor sponsored by the university and the reference log files are **NOT** official: **A 100% pass does not guarantee a 100% grade**.

### How to Install

  - Download or clone this repository in the same folder where your DistanceVector.py file is located.

### How to Run
Run the tester by typing ```python Tester.py```

The output will look like this:

```
Topology: ComplexTopo
Total lines in log: 4312
Result: Failed

Topology: DoubleNegativeTopo
Total lines in log: 112
Result: Passed

Topology: OutgoingTopo
Total lines in log: 70
Result: Passed

Topology: RouteMapTopo
Total lines in log: 806
Result: Passed

Topology: SimpleNegativeCycle
Total lines in log: 1206
Result: Passed

Topology: SimpleTopo
Total lines in log: 18
Result: Passed

Topology: SingleLoopTopo
Total lines in log: 18
Result: Passed

-----
Total tests: 7
Percentage pass: 86.0%
Passed: 6
Failed: 1
```

### How to Add New Topologies

You need to add the reference log file for your new topology inside the **reference_logs** folder and edit **test_list.txt** to include the name of the new topology (without the .txt extension).
