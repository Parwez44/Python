##QN. PRINT STAR* IN RIGHT ANGLE TRIANGLE FORM
# n=5
# for i in range(1,n+1):
#     print("*"*i)

##QN2. PRINT STAR* AS PYRAMID
# n=5
# for i in range(1,n+1):
#     print(" "*(n-i)+"* "*i) #look very consiously (about spaces) space betn inverted coma and after star
##QN3. print reverse pyramid
# def star(n):
#     for i in range(n,0,-1):
#         print(" "*(n-i)+"* "*i)
# star(5)

##QN4. PRINT STAR AS DIAMOND
# n=5
# for i in range(1,n+1):
#     print(" "*(n-i)+"* "*i)
# for j in range(n-1,0,-1):
#         print(" "*(n-j)+"* "*j)

##QN. HOLLOW DIAMOND STAR
# n=5
# for i in range(1,n+1):
#     if i==1:
#         print(" "*(n-i)+"*"*i)
#     else:
#         print(" "*(n-i)+"*"+" "*(2*i-3)+"*")
# for j in range(n-1,0,-1):
#     if i==1:
#         print(" "*(n-j)+"*")
#     else:
#         print(" "*(n-j)+"*"+" "*(2*j-3)+"*")

#QN. HOLLOW SQUARE
# n=5
# for i in range(1,n+1):
#     if i==1 or i==n:
#         print("*" * n)
#     else:
#         print("*" + " " * (n-2) + "*")
# n = 5

#QN. HOLLOW TRIANGLE
# n=5
# for i in range(1,n+1):
#     if i==1 or i==n:
#         print("*"*i)
#     else:
#         print("*" + " "*(i-2)+"*")

# Function to add two matrices
# def add_matrices(matrix1, matrix2):
#     result = []
    
#     for i in range(len(matrix1)):
#         row = []
#         for j in range(len(matrix1[0])):
#             row.append(matrix1[i][j] + matrix2[i][j])
#         result.append(row)
    
#     return result

# # Function to take matrix input from the user
# def input_matrix(rows, cols):
#     matrix = []
#     print("Enter the elements row by row:")
#     for i in range(rows):
#         row = []
#         for j in range(cols):
#             # Input each element for the matrix
#             element = int(input(f"Element [{i}][{j}]: "))
#             row.append(element)
#         matrix.append(row)
#     return matrix

# # Main program
# # Step 1: Get matrix dimensions from user
# rows = int(input("Enter the number of rows: "))
# cols = int(input("Enter the number of columns: "))

# # Step 2: Input both matrices
# print("Enter elements for the first matrix:")
# matrix1 = input_matrix(rows, cols)

# print("Enter elements for the second matrix:")
# matrix2 = input_matrix(rows, cols)

# # Step 3: Add the matrices
# result = add_matrices(matrix1, matrix2)

# # Step 4: Display the result
# print("\nThe result of matrix addition is:")
# for row in result:
#     print(row)





##OTP GENERATION
# import math
# import random
# def generateotp():
#     digits="0123456789"
#     otp= ""
#     for i in range(4):
#         otp+=digits[math.floor(random.random()*10)]
#     return otp
# result=generateotp()
# print("your otp is",result)


## Python program to print all  the possible combinations 

# a,b,c=map(int,input("enter three number separated by space").split())
# n=a,b,c
# for i in range(len(a)): 
# 	for j in range(len(b)): 
# 		for k in range(len(c)): 
# 			if (i!=j and j!=k and i!=k): 
# 				print(i, j, k) 
					


m= input("enter number")
sum=0
for i in m:
	sum+=int(i)
print(sum)
