def average(numbers):
    total = 0
    for i in range(0, len(numbers)):
        total += numbers[i]
    return total / len(numbers)


scores = [10, 20, 30, 40]
result = average(scores)
print("Среднее:", result)
