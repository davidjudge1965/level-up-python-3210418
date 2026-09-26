def get_prime_factors(n):
    if n <= 1:
        return []
    
    factors = []
    
    # 1. Pull out all the 2s by repeatedly trying with 2
    while n % 2 == 0:
        factors.append(2)
        n //= 2
        
    # 2. Pull out odd prime factors up to sqrt(n)
    factor = 3
    while factor * factor <= n:
        while n % factor == 0:
            factors.append(factor)
            n //= factor
        factor += 2
        
    # 3. If n is still greater than 1, the remaining n must be prime
    if n > 1:
        factors.append(n)
        
    return factors




# commands used in solution video for reference
if __name__ == '__main__':
    print(get_prime_factors(630))  # [2, 3, 3, 5, 7]
    print(get_prime_factors(13))  # [13]