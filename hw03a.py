
def nthPrime(num):
    for j in range(2,num):
        if num % j == 0:
            return False
    return True

counter = 0

for i in range(2, 110000):
    if nthPrime(i) == True:
        counter = counter + 1;
        if counter == 10001:
            print(i)
