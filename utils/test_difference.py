import os


def exception(test, output_m, output_b):
    if test == "base64 /dev/urandom | head -c 1000\n":
        if len(output_b) == len(output_m):
            return True
    return None

def equal_to_bash(minishell_line, output_b):
    bash_lines = output_b.split("\n")
    for bash_line in bash_lines:
        if minishell_line == bash_line:
            return True
    return False

def check_text_differences(test, output_m, output_b):
    if output_m == None or output_b == None:
        if output_b == None and output_m == None:
            return True
        return False
    if exception(test, output_m, output_b) != None:
        return exception(test, output_m, output_b)
    minishell_lines = output_m.split("\n")
    for minishell_line in minishell_lines:
        if equal_to_bash(minishell_line, output_b) == False:
            return False
    return True

def initial_file_cleanup(files):
    try:
        files.remove(".DS_Store")
    except:
       pass
    try:
        files_neglect = ["get_next_line.c", "get_next_line_utils.c", "get_next_line.h", "main.c", "main2.c", "main3.c", "a.out", "a.out2"]
        for file in files_neglect:
            files.remove(file)
    except ValueError:
        files.remove("t")
    return files

def final_file_cleanup(files):
    for file in files:
        os.remove(file)

def get_created_files(test):
     text = ""
     files = os.listdir()
     files = initial_file_cleanup(files)
     for file in files:
        with open(file, 'r') as fd:
            text += str(fd.readlines())
     final_file_cleanup(files)
     return text, files

def files_equal_to_bash(file_m, files_b):
    for file_b in files_b:
        if file_m == file_b:
            return True
    return False

def check_created_files(files_m, files_b):
    for file_m in files_m:
        if files_equal_to_bash(file_m, files_b) == False:
            return False
    return True
