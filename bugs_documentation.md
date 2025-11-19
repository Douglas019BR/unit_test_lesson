# Calculator Bugs Documentation

This file contains the intentional bugs placed in the calculator for unit testing lessons.

## Bugs List:

### 1. divide() method
- **Bug**: Doesn't handle division by zero
- **Expected behavior**: Should raise ZeroDivisionError or return appropriate error

### 2. square_root() method  
- **Bug**: Doesn't handle negative numbers
- **Expected behavior**: Should raise ValueError for negative inputs

### 3. factorial() method
- **Bug**: Doesn't handle negative numbers or decimal numbers
- **Expected behavior**: Should raise ValueError for negative or non-integer inputs

### 4. average() method
- **Bug**: Doesn't handle empty list
- **Expected behavior**: Should raise ZeroDivisionError or return appropriate error for empty lists

### 5. absolute() method
- **Bug**: Incorrect implementation for zero (works but could be simplified)
- **Expected behavior**: Should return 0 for input 0 (currently works but implementation is unnecessarily complex)

### 6. is_prime() method
- **Bug**: Returns True for number 1 (1 is not prime) and doesn't handle negative numbers properly
- **Expected behavior**: Should return False for 1 and handle negative numbers

### 7. maximum() method
- **Bug**: Doesn't return anything when both numbers are equal
- **Expected behavior**: Should return the number when both are equal (returns None currently)

## Teaching Notes:
These bugs are designed to teach students how to:
- Test edge cases (zero, negative numbers, empty inputs)
- Handle exceptions properly
- Test boundary conditions
- Verify return values for all possible scenarios
