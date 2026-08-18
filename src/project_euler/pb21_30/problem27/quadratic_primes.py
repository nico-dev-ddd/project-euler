def product_the_coefficients_with_maximum_number_of_primes(a_max: int, b_max:int) -> int:
    max = 0
    for a in range(-a_max, a_max+1):
        for n in range(b_max):
            
            if n > max:
                max = n   
    
    return 0


