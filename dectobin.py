def bin(n):
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n //=  2
        
    return binary


print(bin(45))