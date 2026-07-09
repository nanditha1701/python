# x = int(input("enter a number"))

# if x <=1 :
#     print("x is not a prime number")
# for i in range(2,x):
#     if x % i ==0:
#         print("x is not a prime number")
#         break 
# else:
#     print("x is a prime number")

# x = int(input("enter a number"))
# prime = []

# for num in range(2, x+1):
#     for i in range(2, num):

#         if num % i == 0:
#             break
#     else:
#         prime.append(num)
# print(prime)

# x= int(input("enter a number"))
# original = x
# reverse = 0
# while x>0:
#     reminder = x % 10
#     reverse = (reverse * 10) + reminder
#     x = x//10
# if reverse == original :
#     print("palindrome")
# else:
#     print("not palindrome")

# x = int(input("enter the number: "))
# x = str(x)
# len = len(x)
# x = int(x)
# original = x
# armstrong = 0
# while x > 0:
#     reminder = x % 10
#     armstrong = armstrong + reminder ** len
#     x = x // 10
# if armstrong == original:
#     print("armstrong number")
# else:
#     print("not armstrong number")


# x = int(input("enter the number:"))
# fib = []
# for i in range(x):
#     if i <=1:
#         fib.append(i)
#     else:
#         fib.append(fib[i-1] + fib[i-2])
# print(fib)

# x = int(input("enter a number: "))
# y = int(input("enter a number: "))
# gcd = 1
# for i in range(1, min(x,y)+1):
#     if x %i ==0 and y %i==0:
#         gcd = i
# print(gcd)
# lcm = (x*y)//gcd
# print(lcm)

# x = int(input("enter a number: "))
# reminder = 0
# counteven = 0
# countodd = 0
# while x >0:
#     reminder = x % 10
#     if reminder %2 ==0:
#         counteven +=1
#     else:
#         countodd +=1
#     x = x//10
# print("even", counteven)
# print("odd", countodd)



# x = int(input("enter a number: "))
# fact = []
# for i in range(1, x+1):
#     if x % i ==0:
#         fact.append(i)
# print(fact)

x = int(input("enter a number: "))
original = x
perfect = 0
for i in range(1, x):
    if x %i ==0:
        perfect = perfect + i

if perfect == original:
    print("perfect number")
else:
    print("not perfect number")