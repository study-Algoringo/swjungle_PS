def HyunInsertion(numbers):
    for i in range(1, len(numbers)):
        target = numbers[i]
        for j in range(i, 0, -1):
            if numbers[j-1] > target:
                numbers[j], numbers[j-1] = numbers[j-1], numbers[j]
            else:
                break
    return numbers