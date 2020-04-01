"""
This tool only responsible for printing our banner when starting the program.
this tool use the pyfiglet library for that.
pyfiglet - It takes ASCII text and renders it in ASCII art fonts
"""

from pyfiglet import Figlet


def print_banner():
    custom_fig = Figlet(font='avatar')
    print(custom_fig.renderText('GH0ST  REC0N'))
    print("##### Port Scanner #####")