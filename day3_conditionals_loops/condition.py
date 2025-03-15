# prime or not
num = int(input("Enter a number: "));
if num ==0 or num ==1:
    print("Number is not prime");
elif num > 1:
    for i in range(2,num):
        if num%i == 0:
            print("Number is not prime");
            break;
    else:
        print("Number is prime");



# Pass keyword
# n = 10;
# if n>0:
#     pass

# for i in range(5):
#     pass


# num =int(input("Enter a number: "));
# while num!=0:
#     print("You entered: ", num);
#     num =int(input("Enter a number: "));
    
# print("You entered 0, so loop is terminated");




# while loop
# num = 1;
# while(num <10):
#     print(num);
#     num += 1;# increment num by 1


# Nested Loops
# for i in range(0,2):
#     for j in range(0,2):
#         print(i, j);
#     print("________________________")


# Loops
# for(int i=0;i<10;i++){}
# for i in range(5):
#     if i==3:
#         break;    # continue;
#     print("akhil sharma", i)


# print("akhil sharma")
# print("akhil")
# print("akhil")
# print("akhil")
# print("akhil")
# print("akhil")
# print("akhil")
# print("akhil")
# print("akhil")
# print("akhil")
# print("akhil")
# print("akhil")
# print("akhil")





# no.ofdays:- till 5days=2rps/day, 6-10days:- 3/day,  11-15:-4/day, after 15:- 5/day
# 20:- 70rps
# nd = int(input("Enter the number of days: "));
# if nd <= 5:
#     amt = nd * 2;
# elif nd > 5 and nd <= 10:
#     amt = 10 + (nd-5) * 3;
# elif nd > 10 and nd <= 15:
#     amt = 25 + (nd-10) * 4;
# else:
#     amt = 45 + (nd-15) * 5;
# print("Amount is: ", amt);




# if
# age  = 10;
# if age > 18:
#     print("You are an adult");
    
# if else
# age  = 10;
# if age >= 18:
#     print("You are an adult");
# else:
#     print("You are a child");
    
# Nested If-else :- elif
# age = 65;
# if age <= 5:
#     print("You are a baby");
# elif age<=12:
#     print("You are a kid");
# elif age<=19:
#     print("You are a teenager");
# elif age<=59:
#     print("You are an adult");
# else:
#     print("You are a senior citizen");

# Nested if statements and else
# age = 70;
# is_member = True;
# if age >= 65:
#     if is_member:
#         print("30% discount")
#     else:
#         print("10% discount")
# else:
#     print("No discount") 

# Match Case
# number = 11;
# match number:
#     case 5:
#         print("Number is 5");
#     case 6:
#         print("Number is 6");
#     case 7:
#         print("Number is 7");
#     case 8:
#         print("Number is 8");
#     case 9:
#         print("Number is 9");
#     case 10|11|12:
#         print("Number is 10 or 11 or 12");
#     case _:
#         print("other number")