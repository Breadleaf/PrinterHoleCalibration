# Printer Hole Calibration

These instructions are for slic3r forks. I have only tested on BambuStudio.

1. Print the model
2. Measure the holes
3. Run calibration script as follows:
```
$(which python3) calibrate.py result1 result2 ... result5
```
4. Set the `Quality` -> `Precision` -> `X-Y hole/contour compensation` to the
output of the script
