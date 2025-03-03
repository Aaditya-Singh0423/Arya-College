def fibonacci_sequence(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence
num_terms = int(input("Enter the number of terms: "))
result = fibonacci_sequence(num_terms)
print(f"Fibonacci sequence up to {num_terms} terms:")
print(result)
