import os
import subprocess

minishell_path = "/Users/arthurtainmont/goinfre/my/minishell/minishell"
os.chdir(os.getcwd() + "/test/test")
output = subprocess.run(["echo " + " | " + minishell_path], shell=True, capture_output=True, encoding="utf-8", executable="/bin/zsh", timeout=1)
print(output.stdout)
