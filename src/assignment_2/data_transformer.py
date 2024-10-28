import re
from collections import defaultdict

class LogEntry:
    def __init__(self, date, time, flag, desc):
        self.date = date
        self.time = time
        self.flag = flag
        self.desc = desc
    
    def __repr__(self):
        return f"LogEntry(date={self.date}, time={self.time}, flag={self.flag}, description={self.desc})"

    def formatted(self):
        return f"[{self.date} {self.time}] {self.flag}: {self.desc}"

def classify_logs(log_entries):
    warn_logs = []
    err_logs = []
    info_logs = []
    success_logs = []

    for entry in log_entries:
        if entry.flag == "WARNING":
            warn_logs.append(entry)
        elif entry.flag == "ERROR":
            err_logs.append(entry)
        elif entry.flag == "INFO":
            info_logs.append(entry)
        elif entry.flag == "SUCCESS":
            success_logs.append(entry)

    return warn_logs, err_logs, info_logs, success_logs

def ascii_line():
    return f"\n{"="*40}\n"

def write_header (header, file):
        file.write(ascii_line())
        file.write(header)
        file.write(ascii_line())

def transform_logs(file_path):
    date_pattern = r'\d{4}-\d{2}-\d{2}'  # Matches date in YYYY-MM-DD format
    time_pattern = r'\d{2}:\d{2}:\d{2}'  # Matches time in HH:MM:SS format
    flag_pattern = r'[A-Z]+'              # Matches the flag (uppercase word)
    log_pattern = fr'({date_pattern})\s+({time_pattern})\s+({flag_pattern})\s+(.*)' # Matches the entire log, including the description

    log_entries = []
    log_stats = defaultdict(int)

    with open(file_path, 'r') as log_file:
        logs = log_file.readlines()
        for log in logs:
            match = re.search(log_pattern, log)
            if match:
                date = match.group(1)
                time = match.group(2)
                flag = match.group(3)
                desc = match.group(4)
                log_stats[flag] += 1
                log_entry = LogEntry(date, time, flag, desc)        
                log_entries.append(log_entry)

    return log_entries, log_stats

def write_logs(file_path, log_entries, log_stats):
    warn_logs, err_logs, info_logs, success_logs = classify_logs(log_entries)

    with open(file_path, 'w') as log_file:
        for i, (key, value) in enumerate(log_stats.items()):
            log_file.write(f"{key}: {value}{", " if i < len(log_stats.items())-1 else ""}")
        
        write_header(f"WARNINGS: ({log_stats['WARNING']})", log_file)
        log_file.writelines(log.formatted() + "\n" for log in warn_logs)
        write_header(f"ERRORS: ({log_stats['ERROR']})", log_file)
        log_file.writelines(log.formatted() + "\n" for log in err_logs)
        write_header(f"INFO: ({log_stats['INFO']})", log_file)
        log_file.writelines(log.formatted() + "\n" for log in info_logs)
        write_header(f"SUCCESS: ({log_stats['SUCCESS']})", log_file)
        log_file.writelines(log.formatted() + "\n" for log in success_logs)
    
    print("Write Complete")

def main():
    root = "src/data/"
    log_entries, log_stats = transform_logs(f'{root}assignment_2_log.txt')
    write_logs(f'{root}assignment_2_processed_log.txt', log_entries, log_stats)