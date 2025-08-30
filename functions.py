def apply_operation(numbers, operation):
    return [operation(number) for number in numbers]

# example
numbers = [1, 2, 3, 4, 5]

# double
print("Doubled:", apply_operation(numbers, lambda x: x * 2))

# square
print("Squared:", apply_operation(numbers, lambda x: x ** 2))

# odd numbers
filtered_odds = [x for x in apply_operation(numbers, lambda x: x if x % 2 != 0 else None) if x is not None]
print("Filtered (odd numbers):", filtered_odds)








