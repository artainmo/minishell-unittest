import os
import sys
import subprocess
from utils.test_difference import *
from utils.show_result import *

minishell_pwd = "/Users/arthurtainmont/goinfre/my/minishell/minishell"
#minishell path towards your minishell executable

def parse_minishell(output):
    i = 0
    l = 0
    while i < len(output) and output[i - 1] != ' ':
        i += 1
    prompt = output[0:i]
    l = output.find(prompt, i)
    output = output[i:l]
    return output

def parse_err(output):
    i = 0
    l = 0
    ret = ""
    output = output.split("\n")
    for err in output:
        while i < len(err) and err[i - 1] != ' ':
            i += 1
        ret += err[i:len(err)] + "\n"
    return ret

def parse_quotes(test):
    i = 0
    while i < len(test):
        if test[i] == "'":
            return '"' + test + '"'
        elif test[i] == '"':
            return "'" + test + "'"
        i += 1
    return "'" + test + "'"

def test_minishell(shell_command):
    shell_command = shell_command[0:-1]
    shell_command = parse_quotes(shell_command)
    try:
        output = subprocess.run(["echo " + shell_command + " | " + minishell_pwd], shell=True, capture_output=True, encoding="utf-8", executable="/bin/zsh", timeout=1)
    except:
        output = None
    if output != None:
        output.stdout = parse_minishell(output.stdout)
        output.stderr = parse_err(output.stderr)
        output = output.stderr + output.stdout
    return output


def test_bash(shell_command):
    try:
        output = subprocess.run([shell_command], shell=True, capture_output=True, encoding="utf-8", executable="/bin/bash", timeout=1)
    except:
        output = None
    if output != None:
        output.stderr = parse_err(output.stderr)
        return output.stderr + output.stdout
    return output

def test_in_dir(test, dir, fd_result, fd_check):
    output_m = test_minishell(test)
    file_output_m, files_m = get_created_files(test)
    output_b = test_bash(test)
    file_output_b, files_b = get_created_files(test)
    ret1 = check_text_differences(test, output_m, output_b)
    ret2 = check_text_differences(None, file_output_m, file_output_b)
    ret3 = check_created_files(files_m, files_b)
    show_result(dir, fd_result, fd_check, ret1, ret2, ret3, test, output_m, output_b, files_b, files_m, file_output_m, file_output_b)



if __name__ == "__main__":
    try:
        os.remove("errors.txt")
        os.remove("check.txt")
    except:
        pass
    if os.path.isfile("test/test/a.out") == 0 or os.path.isfile("test/test/a.out2") == 0:
        print("ERROR: use make env to create test files")
        quit();
    print(colored("\nDIRECTORY".ljust(15) + "TEST".ljust(65) + "RESULT", "yellow"))
    with open("test/tests.txt", "r") as fd_tests, open("errors.txt", "a+") as fd_result, open("check.txt", "a+") as fd_check:
        tests = fd_tests.readlines()
        for test in tests:
            if test[0] != '#':
                main_pwd = os.getcwd()
                os.chdir(main_pwd + "/test/test")
                test_in_dir(test, "NOT empty", fd_result, fd_check)
                if test.find("./") != -1 or test.find(".txt") != -1 or test.find(".c") != -1 or test.find(" t ") != -1:
                    os.chdir(main_pwd + "/test/empty")
                    test_in_dir(test, "empty", fd_result, fd_check)
                os.chdir(main_pwd)
    print("\n")
