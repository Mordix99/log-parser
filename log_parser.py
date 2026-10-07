import re
from collections import Counter
import argparse
import sys


# Ten wzorzec szuka:
# 1. IP na samym początku linii (?P<ip>\S+) - zapisuje go do zmiennej (grupy) 'ip'
# 2. Ignoruje środek aż do cudzysłowów
# 3. Szuka 3 cyfr oznaczających status (?P<status>\d{3}) - zapisuje do grupy 'status'
LOG_PATTERN = re.compile(r'^(?P<ip>\S+).*?"[A-Z]+ .*?" (?P<status>\d{3})')

def read_log_file(file_path: str):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                yield line
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.", file=sys.stderr)
        sys.exit(1)

def parse_log_line(line: str) -> dict | None:
    match = LOG_PATTERN.match(line)
    if match:
        return {
            "ip": match.group("ip"),
            "status": int(match.group("status"))
        }
    return None



def main():

    arg_parser = argparse.ArgumentParser(description="Log Parser")
    arg_parser.add_argument("--logfile", type=str, default="server.log", help="Path to the log file")
    args = arg_parser.parse_args()
    log_file_path = args.logfile

    total_requests = 0
    error_ips = Counter()


    for log in read_log_file(log_file_path):
        total_requests += 1
        parsed_line = parse_log_line(log)
        if parsed_line:
            if parsed_line["status"] >= 400:
                error_ips[parsed_line["ip"]] += 1

    print(f"Total requests: {total_requests}")
    print("IP addresses with errors:")
    print(error_ips.most_common(3))  # Zwraca 3 najczęściej występujących IP z błędami



if __name__ == '__main__': 
    main()
    