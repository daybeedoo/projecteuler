def mult3or5(num):
    total = 0
    for i in range(1, num + 1):
        if i % 3 == 0 or i % 5 == 0:
            total += i

    return total

print("problem 1: ", mult3or5(999))

def evenfib(term):
    total = 0
    even = 2
    first = 1
    second = 2
    if term == 1 or term == 2:
        return (term // 2) * 2
    while total < 4000000:
        total = first + second
        if total % 2 == 0:
            even += total
        first = second
        second = total

    return even

print("problem 2: ", evenfib(10))

def largestprimefactor(num):
    biggest = 1
    check = 2
    while num > 0 and num != 1:
        if num % check == 0:
            num = num // check
            if check > biggest:
                biggest = check
            check = 2
        else:
            check += 1

    return biggest

print("problem 3: ", largestprimefactor(600851475143))

def largestpalindromeproduct():
    print()

print("problem 4: ", largestpalindromeproduct())