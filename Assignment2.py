def sumofnumbers(num):
    sum=0
    for i in num:
        sum+=(int(i)*int(i))
    return sum
num=input("Enter list : ").split()
print(sumofnumbers(num))