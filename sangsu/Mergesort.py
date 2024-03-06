def HyunMerge(left, right):
    result = []
    i,j = 0,0
    while True:
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
        if i >= len(left) or j >= len(right):
            break
    result = result + right[j:] if i==len(left) else result + left[i:]
    return result

def HyunMergeSort(numbers):
    if len(numbers) <= 1:
        return numbers

    mid = len(numbers)//2
    left = HyunMergeSort(numbers[:mid])
    right = HyunMergeSort(numbers[mid:])
    return HyunMerge(left, right)