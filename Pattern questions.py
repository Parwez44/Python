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

