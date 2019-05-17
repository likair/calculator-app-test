*** Settings ***
Documentation    Basic functionality testing for calculator application via the Apple Accessibility API.

Library             Process
Library             OperatingSystem
Library             Collections
Library             lib_calc.py

Variables           var_calc.py

Suite Setup         Suite Setup
Suite Teardown      Suite Teardown
Test Setup          Test Setup
Test Teardown       Test Teardown


*** Test Cases ***
Check if all the numbers are working (0 to 9)
    [Tags]    basic   number
    :FOR    ${i}    IN RANGE    10
    \    Clear All
    \    Check Number    ${i}

Check if the clear key is working
    [Tags]    basic    clear
    ${button}    Get Button    ${LABEL_CLEAR}
    Press Button      ${button}

Check if the sum or equal key is working
    [Tags]    basic    equal
    ${button}    Get Button    ${LABEL_ADD}
    Press Button      ${button}

    ${button}    Get Button    ${LABEL_EQUALS}
    Press Button      ${button}

Check the addition of two integer numbers
    [Tags]    function
    [Template]    Check Binary Calc
    1      +     1     2
    10     +     -5    5
    -1     +     1     0

Check the subtraction of two negative numbers
    [Tags]    function
    [Template]    Check Binary Calc
    -2     -     -4     2
    -1     -     -8     7
    -30    -     -2     -28

Check the multiplication of two integer numbers
    [Tags]    function
    [Template]    Check Binary Calc
    3      *      2     6
    10     *     -2    -20
    -3     *      1    -3

Check the division of two integer numbers
    [Tags]    function
    [Template]    Check Binary Calc
    5      /      5     1
    40     /      -2    -20
    5      /      2     2,5

Check the division of a number by zero
    [Tags]    function
    [Template]    Check Binary Calc
    4      /      0     ${ERROR_DIV_ZERO}
    10     /      0     ${ERROR_DIV_ZERO}
    -3     /      0     ${ERROR_DIV_ZERO}

Check the division of zero by any number
    [Tags]    function
    [Template]    Check Binary Calc
    0      /      1      0
    0      /      -2     0
    0      /      30     0


*** Keywords ***
Suite Setup
   Start Calc

Suite Teardown
   Stop Calc

Test Setup
   Clear All

Test Teardown
   Clear All
