# Unit Testing Lesson with Python

This project is a hands-on lesson for learning unit testing with pytest in Python.

## Objective

Learn to write comprehensive unit tests for a Calculator class that contains intentional bugs. You'll discover these bugs through proper testing and fix them.

## Getting Started

1. Clone this repository:
```bash
git clone <repository-url>
cd unit_test_lesson
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Your Task

Create unit tests for all methods in the `src/calculator.py` file. The Calculator class includes:

- Basic operations: `add`, `subtract`, `multiply`, `divide`
- Advanced operations: `power`, `square_root`, `factorial`
- Utility functions: `percentage`, `average`, `absolute`
- Logic functions: `is_even`, `is_prime`, `maximum`, `minimum`

### Testing Guidelines

- Test normal cases
- Test edge cases (zero, negative numbers, empty inputs)
- Test error conditions
- Aim for 90% code coverage or more
- Use descriptive test names

### Expected Structure

```
tests/
├── __init__.py
├── test_calculator.py
└── conftest.py (if needed)
```

## CI/CD Pipeline Requirements

Set up a GitHub Actions pipeline that runs on every PR to main branch:

1. **Code Formatting**: Use `black` to format code
2. **Import Organization**: Use `isort` to organize imports
3. **Static Code Analysis**: Use `pylint` for linting
4. **Automated Testing**: Run pytest with coverage report

### Pipeline should:
- Format code with black
- Sort imports with isort
- Check code quality with flake8
- Run all tests with pytest
- Generate coverage report
- Fail if coverage is below 90%

## Learning Outcomes

By completing this lesson, you will:
- Write effective unit tests
- Handle edge cases and exceptions
- Set up automated testing pipeline
- Use code quality tools
- Achieve high test coverage

## Notes

The Calculator class contains intentional bugs. Finding and fixing these bugs through testing is part of the learning process.
