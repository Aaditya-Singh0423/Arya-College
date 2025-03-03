def print_divisible_by_3(numbers):
    for n in numbers:
        if n % 3 != 0:
            continue
        print(n)
lst =[x for x in range (1,31)]
print(lst)
print_divisible_by_3(lst)
