'''Utils module'''
from colorama import Fore, Style

def parse_input(user_input):
    '''Parsing user input'''
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def format_cmd(text: str) -> str:
    '''Formating command name'''
    return Fore.CYAN + text + Style.RESET_ALL

def format_param(text: str) -> str:
    '''Formating parameter name'''
    return Fore.YELLOW + text + Style.RESET_ALL

def format_greeting(text: str) -> str:
    '''Formating greeting'''
    return Fore.GREEN + text + Style.RESET_ALL

def generate_input_invite() -> str:
    '''Generate input invite'''
    return Fore.GREEN + "\nEnter a command >>> " + Style.RESET_ALL