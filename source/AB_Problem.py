# -*- coding: utf-8 -*-

def solve(N,K):
    """
    N:要素数
    K:必要なpair数
    return : 文字列配列
    """
    result = ""
    for base in range(1,N + 1):
        quo = K // base
        rem = K % base
        print(base)
        if base + quo <= N:
            result += 'B' * quo
            result += 'A' * (base - 1)
            result += 'B' * rem
            result += 'A'
            result += 'B' * (N - len(result))
            break 
    return result[::-1]
    
print(solve(11,16))