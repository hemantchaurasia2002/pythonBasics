list=[1,2,3]
n=len(list)
digit=0
for i in range(0,n):
    if list[i-1] < list[i]:
        list[i]=list[i+1]
print(list)
# lists=digit
# print(lists)
















        # n = len(digits)
        # for i in range(n - 1, -1, -1):
        #     digits[i] += 1
        #     digits[i] %= 10
        #     if digits[i] != 0:
        #         return digits
        # return [1] + digits