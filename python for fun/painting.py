import pyfiglet
from termcolor import colored
text = pyfiglet.figlet_format("Hello, World!", font="slant")

print(colored(text, "red"))