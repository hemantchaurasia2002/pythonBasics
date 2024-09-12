list=[]
n=int(input("Number of elements = "))
for i in range(0, n):
    element=int(input())
    list.append(element)
    print(list)
even_digit_count = 0
for number in list:
    digit_str = str(number)
    if len(digit_str) % 2 == 0:
        even_digit_count += 1
print(even_digit_count)