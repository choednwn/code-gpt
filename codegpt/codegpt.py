import sys
import getopt

from utilities.display import *
from utilities.chatgpt import *
from utilities.runner import *

def main(argv):
    if len(argv) == 0:
        error_message("File not specified.")
        sys.exit()
    else:
        try:
            opts, args = getopt.getopt(argv, "h", ["help", "max_tokens="])
        except:
            error_message("Unknown argument.")
            sys.exit()
        
        # File
        if len(args) > 1:
            error_message("Too many arguments.")
            sys.exit()
        # todo: runner.py -> chatgpt.py
        runner = Runner(args[0])
        runner.run()
        
        
        # Arguments
        max_token_size = 4000
        for opt, arg in opts:
            if opt in ("-h", "--help"):
                help_message(default_token_size=max_token_size)
                sys.exit()
            elif opt == "--max_tokens":
                if not arg.isnumeric():
                    error_message("'max_tokens' must be an Integer.")
                    sys.exit()
                max_token_size = int(arg)


if __name__ == "__main__":
    main(sys.argv[1:])
    