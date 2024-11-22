def dec(x: str):
    n = len(x)
    p2 =1
    num = 0
    
    for i in range(n - 1 ,-1 ,-1):
        if x[i] == '1':
            num += p2
        p2 = p2*2
    
    return num

print(dec('101101'))