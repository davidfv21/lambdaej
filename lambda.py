lambda_factorial = lambda i:1 if i==0 else i*lambda_factorial(i-1)
print(lambda_factorial(4)) # 4 * 3 * 2 * 1 = 12 * 2 = 24

def fun(x, y, z):
    return x*y+z
a = 1
b = 2
c = 3

# logical jump
d = fun(a, b, c)
print(d)

d = (lambda x, y, z: x*y+z)(1, 2, 3)
print(d)       
