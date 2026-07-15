# Printer Hole Calibration

These instructions are for slic3r forks. I have only tested on BambuStudio.

1. Print `./PHC-test_jig.3mf` using your slicer's default settings
2. Measure the holes with a caliper
3. Run calibration script as follows:
```
$(which python3) calibrate.py result1 result2 ... result5
```
Note: The order of results should be put in the order of smallest hole to
largest from the expected results.
4. Set the `Quality` -> `Precision` -> `X-Y hole/contour compensation` to the
output of the script
