# taking lst input from user
a =[]
n = int(input("Enter the number of elements: "));
for i in range(n):
    a.append(int(input("Enter the element: ")));
target = int(input("Enter the target element: "));
for i in range(n):
    for j in range(i+1, n):
        if a[i] + a[j] == target:
            print("The elements are: ", a[i], a[j]);



# # Nested Lists
# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# # print(matrix[2][0]);
# for i in range(3):
#     for j in range(3):
#         print(matrix[i][j])
#     print("\n")



# lists:- CRUD operations
# C - Create
# R - Read
# U - Update
# D - Delete
# Iterate over the list
# lst = [1,2,3,4,5,6,7,8,9,10];
# for element in lst:
#     print(element);



# Remove the elements from the list
# 1. remove() - remove the first occurance of the element
# lst = [1,2,3,3,3,4,4,4,4,111,1,1,1,1]
# list.remove(lst, 3);
# print(lst);

# 2. pop() - remove the element at the specified index
# lst  = [1,2,3,4,5,6,7,8,9,10];
# lst.pop(5);
# print(lst);

# 3. del statement - delete the element at the specified index
# del lst[3];
# print(lst);


# updatig an elemtn in list
# lst = [1,2,3,4,5,6,7,8,9,10];
# lst[70] = 100;
# print(lst);



# Additon of elements
# # 1.append() - add the element at the end of the list
# lst = [1,2,3,4,5,6,7,8,9,10];
# lst.append(11);
# print(lst);
# # 2. extend() - add the elements of the list at the end of the list
# lst.extend([12,13,14,15]);
# print(lst);
# # 3. insert() - add the element at the specified index
# lst.insert(70,2000);
# print(lst);



# Access the elemets for the list
# lst = [1,2,3,4,5,6,7,8,9,10];
# print(lst[0]);
# print(lst[1]);
# print(lst[2]);
# print(lst[3]);
# print(lst[4]);
# print(lst[5]);



# creating a list
# a = [1,2,3,4, True, "Akhil", 3.14, 1,2,3,4,5,6,7,8,9,10];
# a = list((1,2,3,4, True, "Akhil", 3.14, 1,2,3,4,5,6,7,8,9,10));
# repeated elements
# a = [2]*10;
# print(a);
# print( a);