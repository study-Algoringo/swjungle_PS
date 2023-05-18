def solution(fees, records):
    answer = {}
    for record in records:
        time, number, entr = record.split()
        if number not in answer:
            answer[number] = []
        answer[number].append([time,entr])

    for temp in answer:
        for t in temp:
            print(t)
    return answer

print(solution([180, 5000, 10, 600],["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))