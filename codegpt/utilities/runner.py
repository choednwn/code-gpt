import os
import subprocess
from utilities.display import *

class Runner:
    def __init__(self, file):
        self.file = file

    def run(self):
        self.check_language()

    def check_language(self):
        dot_idx = self.file.rfind(".")
        if dot_idx == -1:
            error_message("File type cannot be read.", help=False) 
            sys.exit()
        
        extension = self.file[dot_idx:]
        