import re
from typing import Callable

text = '''Загальний дохід працівника складається з декількох частин: 
1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів.'''

def generator_numbers(text: str):
    pattern = r'(?:^|\s)([+-]?\d+(?:\.\d+)?)(?=\s|$)'
    
    for match in re.finditer(pattern, text):
        yield float(match.group(1))

generator = generator_numbers(text)
print(next(generator))  # 100.5
print(next(generator))  # 200.0
print(next(generator))  # 300.75
# print(next(generator))  # StopIteration

def sum_profit(text: str, func: Callable):
    return sum(func(text))
        
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}") # Загальний дохід: 1351.46

