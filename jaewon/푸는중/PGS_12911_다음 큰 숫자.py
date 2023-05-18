def solution(n):
    n_bin = bin(n)
    n_bin_cnt = n_bin.count("1")
    
    while (1):
        n += 1
        m_bin = bin(n)
        m_bin_cnt = m_bin.count("1")
        if n_bin_cnt == m_bin_cnt:
            return n

print(solution(78))
print(solution(15))