'''System log analyzer'''
import re
import sys
from collections import Counter
from pathlib import Path
from colorama import Fore, Style
from log_level import LogLevel

def parse_log_line(line: str) -> dict:
    '''Parse log line'''
    pattern = r"(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) ([A-Z]+) (.*)"
    match = re.search(pattern, line)
    if match:
        result = dict(zip(['date', 'time', 'level', 'message'], match.group(1,2,3,4)))
    else:
        result = {}
    return result

def load_logs(file_path: str) -> list:
    '''Load logs from file to list'''
    if Path(file_path).exists():
        with open(file_path, "r", encoding="utf-8") as file:
            result = [parse_log_line(line) for line in file.readlines()]
    else:
        raise FileNotFoundError("Invalid file path specified")
    return result

def filter_logs_by_level(logs: list, level: str) -> list:
    '''Filters logs by level'''
    return filter(lambda x: x.get("level") == level.upper() ,logs)

def count_logs_by_level(logs: list) -> dict:
    '''Сalculates дщпі statistics'''
    return dict(Counter([x.get("level") for x in logs]))

def mark_text(text: str, flag: bool) -> str:
    '''Mark text with color'''
    return Fore.YELLOW + text + Style.RESET_ALL  if flag else text

def display_log_counts(counts: dict, level: str = None):
    '''Display results'''
    res = "\n"
    res += f'{'Рівень логування':<17}{'|':^3}{'Кількість':<10}\n'
    res += f'{'-'*17:<17}{'-|-':^3}{'-'*10:<10}\n'
    for k, v in counts.items():
        res += mark_text(f'{k:<17}{'|':^3}{v:>10}\n', level == k)
    print(res)

def display_log_details(logs: list, level: str):
    '''Display detail logs'''
    res = f"Деталі логів для рівня {mark_text(level,True)}:\n"
    for l in logs:
        res += " ".join(l.values()) + "\n"
    print(res)

def parse_sys_params() -> tuple:
    '''Parse params'''
    is_error, path, level = True, Path(), None
    args = sys.argv
    if 1 < len(args) < 4:
        path = Path(args[1])
        if path.exists() and path.is_file():
            is_error = False
        else:
            print("The specified path is not correct or file does not exist")
        if len(args) == 3:
            level = str(args[2]).upper()
            if level not in LogLevel:
                is_error = True
                print("Parameter 'level' should be in the list", [l.value for l in LogLevel]) 
    else:
        print("The script requires one or two parameters")
    return (is_error, path, level)

def main():
    '''App runtime'''
    is_error, path, level = parse_sys_params()
    if is_error is False:
        all_logs = load_logs(path)
        display_log_counts(count_logs_by_level(all_logs),level)
        if level:
            display_log_details(filter_logs_by_level(all_logs,level),level)

if __name__ == "__main__":
    main()
