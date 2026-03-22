import re
from typing import Callable, Iterator

text = '''Загальний дохід працівника складається з декількох частин: 
1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів.'''

def generator_numbers(text: str) -> Iterator[float]:
  
    pattern = r'(?<!\S)[+-]?\d+(?:\.\d+)?(?!\S)'
    
    for match in re.finditer(pattern, text):
        yield float(match.group())

def sum_profit(text: str, func: Callable[[str], Iterator[float]]) -> float:
    return sum(func(text))

generator = generator_numbers(text)

print(next(generator))  # 1000.01
print(next(generator))  # 27.45
print(next(generator))  # 324.0

total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")

