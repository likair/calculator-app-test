# Calculator Robot Test

This project contains tests for Calculator application in OS X system with Robot Framework. A third-party library Atomacos enables GUI testing of macOS applications via the [Apple Accessibility API](https://developer.apple.com/library/archive/documentation/Accessibility/Conceptual/AccessibilityMacOSX/).

## Prerequisites

- Python3
- robotframework
- atomacos

```bash
pip install -r requirements.txt
```

## Test cases

### Test the app’s basic operations

- Check if all the numbers are working (0 to 9)
- Check if the clear key is working
- Check if the sum or equal key is working

### Test the app’s functionality

- Check the addition of two integer numbers
- Check the subtraction of two negative numbers
- Check the multiplication of two integer numbers
- Check the division of two integer numbers
- Check the division of a number by zero
- Check the division of zero by any number

## Running test

### Run robot test in a debug mode

```bash
robot -L debug calc.robot
```

Example results are in ./results folder.

### Run the python script directly (only a basic test case is given)

```bash
python lib_calc.py
```
