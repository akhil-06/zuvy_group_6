# pattern program:- traingle pattern
# n = int(input("enter number: "))
# for i in range(1,n+1):
#     print("*" * i)

# num=int(input("Enter a no."))

# for i in range(num):
#     for j in range (i+1):
#         print("*",end=" ")
#     print("\n")




# print tables
# for i in range(1, 21):
#     for j in range(1, 11):
#         print(i * j)
#     print()

# for i in range(10,21):
#     for j in range(1,11):
#         print (i*j, end=" ")

# for i in range(10,21):
#     for j in range(1,11):
#         print(j*i, end=" ")
#     print("\n")



# count number of digits
# n = int(input("Enter a number: "))
# count =0;
# while n!=0:
#     n = n//10;
#     count+=1;
# print(count)

# Sum of number of digits
# n = int(input("Enter a number: "))
# sum = 0;
# while n!=0:
#     sum = sum + n%10;
#     n = n//10;
# print(sum)


# fibonacci series
# a = 0;
# b = 1;
# for i in range(0,10):
#     print(a)
#     sum = a+b;
#     a = b;
#     b = sum;
    # a,b = b,a+b


# guess the number
# guess = 0;
# while True:
#     n = int(input("Enter a number: "))
#     if n == guess:
#         break;



# celcius to farhenite
# n = float(input("Enter the temperature in celcius: "))
# f = (n*9/5)+32
# print(f)



# Divisible by 7 and multiple of 5
# for i in range(1500,2701):
#     if i%7==0 and i%5==0:
#         print(i)