import os
import subprocess
from main import *

os.chdir(os.getcwd() + "/test/test")
output = subprocess.run(["echo " + " | " + minishell_path], shell=True, capture_output=True, encoding="utf-8", executable="/bin/zsh", timeout=1)
print(output.stdout)
