x = int(input("Enter the number : "))
z = x
num=0
num2=0
while x > 0:
    y=x%10
    num=num*10+y
    x=x//10
print(num)

while num > 0:
    on = num%10
    num2=num2*10+on
    num=num//10
print(num2)
print(z)

if num2 == z:
    print("True")
else:
    print("False")




# effective approach
class Solution(object):
    def isSameAfterReversals(self, num):
        """
        :type num: int
        :rtype: bool
        """
        
        if num == 0: 
            return True
        elif num%10!=0:
            return True
        else: 
            return False