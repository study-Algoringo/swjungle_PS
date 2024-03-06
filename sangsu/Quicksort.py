def HyunQuick(numbers):
    if len(numbers) <= 1:
        return numbers
    pivot = numbers[len(numbers)//2]
    left, right, equal = [], [], []
    for num in numbers:
        if num < pivot:
            left.append(num)
        elif num > pivot:
            right.append(num)
        else:
            equal.append(num)
    return HyunQuick(left) + equal + HyunQuick(right)