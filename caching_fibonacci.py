'''Реалізуйте функцію, яка створює та використовує кеш для 
зберігання і повторного використання вже обчислених значень чисел Фібоначчі.

Ряд Фібоначчі - це послідовність чисел виду: 0, 1, 1, 2, 3, 5, 8, ..., де кожне 
наступне число послідовності виходить додаванням двох попередніх членів ряду.'''


def caching_fibonacci():
    cache = {}
    def fibonacci(n: int) -> int:
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache:
            #print(cache)
            return cache[n]

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n] 

    return fibonacci


fib = caching_fibonacci()

print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610
print(fib(8))
print(fib(4))