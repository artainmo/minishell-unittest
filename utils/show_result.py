from termcolor import colored
from main import *

def show_result(dir, fd_result, fd_check, ret1, ret2, ret3, test, output_m, output_b, files_b, files_m, file_output_m, file_output_b):
    if files_m == []:
        files_m = None
    if files_b == []:
        files_b = None
    if test[len(test) - 1] == '\n':
        test = test[0:-1]
    if ret1 and ret2 and ret3:
        print(dir.ljust(15) + test.ljust(65), end = "")
        print(colored("CORRECT", "green"))
        fd_check.write("\n****************************************\ncommand in %sdir:\n%s\n****************************************\n" % (dir, test))
        fd_check.write("==========output==========\nYOU:\n%s\nBASH:\n%s" % (output_m, output_b))
        if ret2 == False or ret3 == False:
            fd_check.write("==========files==========\nYOU:\n%s\nBASH:\n%s\n" % (files_m, files_b))
            fd_check.write("==========cat_files==========\nYOU:\n%s\nBASH:\n%s\n" % (file_output_m, file_output_b))
    else:
        print(dir.ljust(15) + test.ljust(65), end="")
        print(colored("WRONG", "red"))
        fd_result.write("\n****************************************\ncommand in %sdir:\n%s\n****************************************\n" % (dir, test))
        fd_result.write("==========output==========\nYOU:\n%s%d\n\nBASH:\n%s%d\n" % (output_m, len(output_m), output_b, len(output_b)))
        if ret2 == False or ret3 == False:
            fd_result.write("==========files==========\nYOU:\n%s\nBASH:\n%s\n" % (files_m, files_b))
            fd_result.write("==========cat_files==========\nYOU:\n%s\nBASH:\n%s\n" % (file_output_m, file_output_b))
