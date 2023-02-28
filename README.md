# minishell_unittest

### Info
 This is a unittest for [minishell](https://github.com/artainmo/minishell) primarily focused on tokens and parsing, you can add tests in the tests.txt file if you want to.<br>
 The program will compare your minishell and bach's terminal output, files you created and content inside those files.<br>
 To isolate one case you can modify the test/test.txt file and modify tests.txt into test.txt inside main.py.<br>
 To put a test in comment or deactivate it use #.

### Prerequisites:
  To run this unit-test you need python3.7 and pip installed.

### Usage:
  * First:
  ```
  make env
  ```
  * Second:
  
  Open main.py and add in str format the absolute directory to your minishell program.
  
  * Third:
  ```
  make prompt
  ```
  Use make prompt to see the prompt we will use and copy paste your prompt in top main.py minishell_prompt variable.
  
  * Finally:
  ```
  make
  ```
  You can look at your error log in errors.txt, use check.txt to look at correct answer outputs.


### Errors:
  Does not support and cannot test multiline.<br>
  Does not support `;`.<br>
  Doesn't seem to support this command: `echo '$USER'`.<br>
  UnicodeDecodeError: Delete the test/test/get_next_line.h.gch .<br>
  ./a.out: Exec format error -> `make re` or change computer.
