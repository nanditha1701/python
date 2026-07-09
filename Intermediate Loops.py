# x = int(input("enter a number"))

# if x <=1 :
#     print("x is not a prime number")
# for i in range(2,x):
#     if x % i ==0:
#         print("x is not a prime number")
#         break 
# else:
#     print("x is a prime number")

x = int(input("enter a number"))
prime = []

for num in range(2, x+1):
    for i in range(2, num):

        if num % i == 0:
            break
    else:
        prime.append(num)
print(prime)