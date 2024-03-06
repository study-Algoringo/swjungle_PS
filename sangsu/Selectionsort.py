def HyunSelection(numbers):
    for i in range(len(numbers)):
        mn = 999999999
        for j in range(i, len(numbers)):
            if numbers[j] < mn:
                mn = numbers[j]
                mn_idx = j
        numbers[i], numbers[mn_idx] = numbers[mn_idx], numbers[i]
    return numbers