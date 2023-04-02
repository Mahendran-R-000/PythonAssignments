def Assignment3(i):
     if i% 3== 0 and i%5==0:
        return "FizzBuzz"
     elif i %3==0:
        return "Fizz"
     elif i% 5 == 0:
        return "Buzz"
     else:
        return i
print(Assignment3(int(input('Enter number : '))))