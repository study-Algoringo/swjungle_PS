import sys
input = sys.stdin.readline

n, k = map(int, input().split())

if k < 5:
    result = 0
    
else:
    learn_list = ["a", "c", "i", "n", "t"]
    word_list = []
    for i in range(n):
        w_list = []
        word = input().strip()
        for w in word:
            if not w in learn_list:
                w_list.append(w)
        word = "".join(w_list)
        word_list.append(word)

    word_list2 = []
    for word in word_list:
        word = set(word)
        word = "".join(word)
        word_list2.append(word)
    
    word_list3 = []    
    for word in word_list2:
        if len(word) <= k-5:
            word_list3.append(word)
            
    print(word_list3)