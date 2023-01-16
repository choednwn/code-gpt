import sys
import utilities.format as fmt

def error_message(message: str, help: bool = True):
    print(f"{fmt.RED}Error{fmt.RESET}: {message}")
    if help:
        print(f"{fmt.GREEN}Help{fmt.RESET}: python codegpt.py -h")

def help_message(default_token_size: str):
    print(f"{fmt.GREEN}Code-GPT{fmt.RESET}")
    print(f"A simple program that explain code / errors using OpenAI's ChatGPT.\n")
    print(f"{fmt.DIM}ChatGPT: https://openai.com/blog/chatgpt")
    print(f"Project repository: https://github.com/yonnsdev/code-gpt{fmt.RESET}\n")

    print(f"{fmt.GREEN}-h, --help{fmt.RESET}")
    print(f"{fmt.TAB}Shows help menu.\n")

    print(f"{fmt.GREEN}--max_tokens {fmt.DIM}(default: {default_token_size}){fmt.RESET}")
    print(f"{fmt.TAB}The max_tokens parameter sets an upper bound on how many tokens the API will return.")
    print(f"{fmt.TAB}CodeGPT uses <text-davinci-003> {fmt.DIM}$0.02 / 1k tokens{fmt.RESET}")
    print(f"{fmt.TAB + fmt.GREEN}Example{fmt.RESET}: python codegpt.py {fmt.GREEN}--max_tokens=2000{fmt.RESET} test.py\n")
    
    print(f"{fmt.GREEN}Usage{fmt.RESET}")
    print(f"{fmt.TAB}python codegpt.py [args..] [file]")