def get_primes(n):
    arr = []
    for i in range(2, n):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            arr.append(i)
    return arr


print(get_primes(23))



# camelCase js
# PascalCase
# CONSTCASE
# snake_case python


