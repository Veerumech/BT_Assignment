# BT_Assignment

This Framework is of Hybrid framework using Pytest and POM methods.

Intial Setting
1. Requirement (Install):
   1. Pytest : pip install pytest
   2. selenium : pip install selenium
   3. pytest-html     
2. Terminal path setting:
   1. cd "path up to Test_Script"

Execution:
1. Write below command and press enter key in terminal to run or generate report
   1. pytest test_11.py -rp --html=".\Report\assets\{Report}.html"         ---- change file name everytime 

2. If any testcase failed:
   1. use: pytest --last-failed -rp --html=".\Report\assets\{Report}.html"        ---- change file name everytime

