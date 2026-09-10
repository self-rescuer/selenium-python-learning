def find_evens(numbers):
    evens = []
    for number in numbers:
        if number % 2 == 0:
            evens.append(number)
    return evens
print(find_evens([1, 2, 3, 4, 5, 6]))

print(find_evens([1, 3, 5]))
