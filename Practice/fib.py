a, b = 0, 1
n = int(input("Enter the value of n : "))
for _ in range(n):
    a, b = b, a + b
print(a)