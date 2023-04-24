n = int(input("Enter N: "))

for i in range(1234, n+1):
    s = str(i)
    if s[0]<s[1] and s[1]<s[2] and s[2]<s[3]:
        print(i)

n = int(input("Enter N: "))

for a in range(1, 10):
    for b in range(a+1, 10):
        for c in range(b+1, 10):
            for d in range(c+1, 10):
                number = 1000*a + 100*b + 10*c + d
                if number > n:
                    break
                else:
                    print(number)