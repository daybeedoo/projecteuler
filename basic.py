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

def largestpalindromeproduct(num):
    biggest = 1
    while num > 0:
        for i in range(num, 0, -1):
            curr = i * num
            if str(curr) == str(curr)[::-1]:
                if curr > biggest:
                    biggest = curr
        num -= 1

    return biggest

print("problem 4: ", largestpalindromeproduct(999))

def smallestmultiple(num):
    result = 1
    lst = [x for x in range(1, num + 1)]
    while lst:
        print(lst)
        curr = lst[0]
        result *= curr
        for i in range(len(lst)):
            if lst[i] % curr == 0:
                lst[i] = lst[i] // curr
        lst = [x for x in lst if x > 1]

    return result

print("problem 5: ", smallestmultiple(20))

