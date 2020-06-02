# minishell_unittest
Info:
  This is a unittest for minishell primarily focused on tokens and parsing, you can add tests in the tests.txt file if you want to.
  The program will compare your minishell and bach's terminal output, files you created and content inside those files.
  To isolate one case you can modify the test/test.txt file and modify tests.txt into test.txt inside main.py
  To put a test in comment or deactivate it use #

Prerequisites:
  To run this unit-test you need python3.7 and pip installed

Usage:
  First execute make env to create adequate environment
  Open main.py and add in str format the absolute directory to your minishell program
  execute with make
  You can look at your error log in errors.txt, use check.txt to look at correct answer outputs

Errors:
  Does not support and cannot test multiline
  
  Does not support ;
  
  Doesn't seem to support this commandi: echo '$USER'
  
  UnicodeDecodeError: Delete the test/test/get_next_line.h.gch
  
  ./a.out: Exec format error -> make re or change computer
