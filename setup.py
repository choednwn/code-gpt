import sys
import subprocess
import codegpt.utilities.format as fmt
try:
    import getch as gh
except:
    subprocess.run([sys.executable, "-m", "pip", "install", "getch", "--use-pep517"])
    import getch as gh
    
def option_menu(options: list, add_quit: bool = False) -> int:
    def get_key():
        first_char = gh.getch()
        if first_char == "\x1b":
            return {"[A": "up", "[B": "down", "[C": "right", "[D": "left"}[gh.getch() + gh.getch()]
        else:
            return first_char

    selected_option = 0
    if add_quit:
        options.append("Quit setup")

    while True:
        for idx, message in enumerate(options):
            message = f"{idx + 1}. " + message
            if idx == selected_option:
                print(f"{fmt.UNDERLINE}{fmt.GREEN}" + message + "\033[0m")
            else:
                print(message)
        
        input_key = get_key()
        match input_key:
            case "up":
                if selected_option > 0:
                    selected_option -= 1
            case "down":
                if selected_option < len(options) - 1:
                    selected_option += 1 
            case "\n":
                if add_quit and selected_option == len(options) - 1:
                    sys.exit()
                else:
                    sys.stdout.write("\n")
                    return selected_option

        for idx in range(len(options)):
            sys.stdout.write("\033[F\033[K")

def main():
    # Check installed Python version
    if sys.version_info[:3] < (3, 0 , 0):
        print("Code-GPT requires Python 3 to run.")
        sys.exit()

    # Create a virtual environment to install modules
    print("> Would you like to create a virtual environment?")
    venv_options = [
        "Create a virtual environment for this project",
        "Use current environment (global)"
    ]
    venv_input = option_menu(venv_options, add_quit=True)

    if venv_input == 0:
        subprocess.run([sys.executable, "-m", "venv", "./venv"])

    # Install packages
    print("> The following package(s) are required to run Code-GPT.")
    required_packages = [
        "openai",
        "pygments"
    ]
    for idx, package in enumerate(required_packages):
        print(f"{idx + 1}. {package}")
    sys.stdout.write("\n")

    print("> Would you install the following packages?")
    package_options = [
        "Install listed packages",
        "No. I will install them myself"
    ]
    package_input = option_menu(package_options, add_quit=False)

    if package_input == 0:
        for package in required_packages:
            if venv_input == 0:
                subprocess.run(["./venv/bin/pip", "install", package])
            else:
                subprocess.run([sys.executable, "-m", "pip", "install", package])

    # Create api.key file
    api_file = open("api.key", "a")   

    # Complete message
    print("Setup is complete.")

if __name__ == "__main__":
    main()