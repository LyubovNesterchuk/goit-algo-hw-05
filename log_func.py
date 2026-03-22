
'''Файли логів – це файли, що містять записи про події, які відбулися в операційній системі,
програмному забезпеченні або інших системах. Вони допомагають відстежувати та аналізувати 
поведінку системи, виявляти та діагностувати проблеми.
'''
from pathlib import Path
import sys

# Парсинг рядка логу, приймає рядок з логу як вхідний параметр і повертає словник з 
# розібраними компонентами: дата, час, рівень, повідомлення. 

def parse_log_line(line: str) -> dict:

    try:
        parts = line.strip().split(" ", 3) # розділити рядок максимум на 4 частини (3 розділення)
        date = parts[0]
        time = parts[1]
        level = parts[2]
        message = parts[3]

        return {
            "date": date,
            "time": time,
            "level": level.upper(),
            "message": message
        }
    except IndexError:
        # Якщо рядок має неправильний формат
        return None


# Завантаження лог-файлів, відкриває файл, читає кожен рядок і 
# застосовує до нього функцію parse_log_line, зберігаючи результати в список.

def load_logs(file_path: str) -> list:
    logs = []

    path = Path(file_path)
    if not path.is_absolute():
        path = Path(__file__).parent / path

    try:
        with open(path, "r", encoding="utf-8") as file:
            logs = [log for line in file if (log := parse_log_line(line))] # := це оператор моржа (walrus operator)

        ''' logs = []
            for line in file:
            log = parse_log_line(line)
            if log:
                logs.append(log)'''

    except FileNotFoundError:
        raise FileNotFoundError(f"Файл не знайдено: {path}")

    except OSError as e:
        raise RuntimeError(f"Помилка читання файлу: {e}")

    return logs

# Фільтрує логи за рівнем
def filter_logs_by_level(logs: list, level: str) -> list:
    level = level.upper()
    return [log for log in logs if log["level"] == level]
    #return list(filter(lambda log: log["level"] == level, logs))


# проходить по всім записам і підраховує кількість записів для кожного рівня логування

def count_logs_by_level(logs: list) -> dict:

    counts = {}

    for log in logs:
        level = log["level"]
        counts[level] = counts.get(level, 0) + 1

    return counts

# виводить статистику у вигляді таблиці
def display_log_counts(counts: dict):

    print("\nРівень логування | Кількість")
    print("-----------------|----------")

    for level in sorted(counts.keys()):
        print(f"{level:<16} | {counts[level]}")



def display_filtered_logs(logs: list, level: str):

    if not logs:
        print(f"\nНемає записів для рівня '{level.upper()}'")
        return

    print(f"\nДеталі логів для рівня '{level.upper()}':")

    for log in logs:
        print(f"{log['date']} {log['time']} - {log['message']}")



def main():
    if len(sys.argv) < 2:
        print("Використання: python main.py <шлях_до_файлу> [рівень]")
        sys.exit(1)

    file_path = sys.argv[1]
    level = sys.argv[2] if len(sys.argv) > 2 else None

    try:
        logs = load_logs(file_path)
    except Exception as e:
        print(f"Помилка: {e}")
        sys.exit(1)

    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    if level:
        filtered_logs = filter_logs_by_level(logs, level)
        display_filtered_logs(filtered_logs, level)


if __name__ == "__main__":
    main()


# в терміналі:
# python log_func.py logfile.log
'''
Рівень логування | Кількість
-----------------|----------
DEBUG            | 3
ERROR            | 2
INFO             | 4
WARNING          | 1 
'''

# python log_func.py logfile.log error 
'''Деталі логів для рівня 'ERROR':
2024-01-22 09:00:45 - Database connection failed.
2024-01-22 11:30:15 - Backup process failed.'''
# python log_func.py logfile.log warning
# python log_func.py logfile.log debug
# python log_func.py logfile.log info


    

