# n = int(input("input enter the number"))

# for i in range(n+1):
#     print(i, end = " ")

# n = int(input("enter a number"))
# for i in range(n, -1, -1):
#     print(i, end = " ")

# n = int(input("enter the number"))
# for i in range(n+1):
#     if i % 2 == 0:
#         print(i, end = " ")

# n = int(input("enter the number"))
# for i in range(n+1):
#     if i % 2 != 0:
#         print(i, end = " ")


# n = int(input("enter the number "))
# sum = 0
# for i in range(n+1):
#     sum = sum +i
# print(sum)

# n = int(input("enter the number"))
# fact = 1
# for i in range(1,n+1):
#     fact =  fact*i
# print(fact)


# n = int(input("enter th numer"))
# for i in range(n,n+1):
#     for j in range(1,11,1):
#         print(i, "*" , j, "=", i*j)

# n  = int(input("enter the numbers"))
# count = 0
# while n>0:
#     n=n//10
#     count = count+1
# print(count)

# n = int(input("enter the numbers "))
# reverse = 0
# while n >0:
#     reminder = n%10
#     reverse = reverse*10+ reminder
#     n = n//10
# print(reverse)

n = int(input("enter the numbers"))
sum = 0
while n>0:
    reminder = n%10
    sum = sum +reminder
    n = n//10
print(sum)