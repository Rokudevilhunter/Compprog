nterms = int(input("what do you want your range to be?"))

n1, n2 = 0, 1
count = 0

if nterms <= 0:
    print("please make the number positive")

elif nterms == 1:
    print("Fib up to", nterms,":")
    print(n1)
else:
    while count < nterms:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1