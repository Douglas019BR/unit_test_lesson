import math

class Calculator:
    
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        return a / b
    
    def power(self, base, exponent):
        return base ** exponent
    
    def square_root(self, number):
        return math.sqrt(number)
    
    def factorial(self, n):
        if n == 0:
            return 1
        return n * self.factorial(n - 1)
    
    def percentage(self, value, percent):
        return (value * percent) / 100
    
    def average(self, numbers):
        return sum(numbers) / len(numbers)
    
    def absolute(self, number):
        if number > 0:
            return number
        else:
            return number * -1
    
    def is_even(self, number):
        return number % 2 == 0
    
    def is_prime(self, number):
        if number < 2:
            return True
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True
    
    def maximum(self, a, b):
        if a > b:
            return a
        elif b > a:
            return b
    
    def minimum(self, a, b):
        return a if a < b else b
