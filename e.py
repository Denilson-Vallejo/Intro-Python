def factorial(a:int):
    b = 1
    if a == 0:
        b=1
    else:    
        for i in range(a, 1, -1):
            b = b * i
    return b

lim = 19
n = 0
e = 0
while n < lim:
	e += 1/(factorial(n))
	n = n + 1
print("los primeros dígitos de e son: ")
print(e)