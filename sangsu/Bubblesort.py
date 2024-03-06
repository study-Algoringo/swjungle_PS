def HyunBubble(numbers):
    for i in range(len(numbers), 1, -1):
        for j in range(i-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers