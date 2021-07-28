from functools import cache

@cache
def factorial(n: int) -> int:
  return 1 if (n==1 or n==0) else n * factorial(n - 1);

@cache
def fibonacci(n: int) -> int:
  if n <= 1:
    return n
  elif n == 2:
    return 1
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)