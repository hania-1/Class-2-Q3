# Python Operators
 
# Arithmetic Operators
# # 1.Add
a=5
b=2
print(a+b)

# 2.Subtraction
print(a-b)

#  3.Multiplication
print(a*b)

# 4.Division
print(a/b)

# # 5.Floor Division
print(a//b)

# # 6.Modulus
print(a%b)
  
# # 7.Exponent
print(a**b)

# Comparison Operators

# # 1.Equal
c=7
d=5
print(c==d)

# # 2.Not Equal
print(c!=d)

# # 3.Greater Than
print(c>d)

# # 4.Less Than
print(c<d)

# # 5.Greater Than or Equal To
print(c>=d)

# # 6.Less Than or Equal To
print(c<=d)

# # Logical Operators

# # 1.And
e=6
f=5
print(e > f and f < e)

# # 2.Or
print(e > f or f < e)

# # 3.Not
print(not(e > f or f < e))

# Assignment Operators

# 1.Simple Assignment
g=6
print("g=",g)

# 2.Addition Assignment
g+=5
print("g=",g)

# 3.Subtraction Assignment
g-=2
print("g=",g)

# 4.Multiplication Assignment
g*=2
print('g=',g)

# 5.Division Assignment
g/=2
print('g=',g)

# 6.Floor Division Assignment
g//=2
print("g=",g)

# g = int(g)  # Convert to integer
# print("g =", g)  # Output: g = 4

# Modulus Assignment
g%=3
print('g=',g)

# # Exponent Assignment
g**3
print("g=",g)

# # Membership Operators

# # 1.In

fruits=["apple","banana","cherry"]
print("banana" in fruits)

# # 2.Not In

fruits=["apple","banana","cherry"]
print("mango" not in fruits)

student={"name":"hania","age":20}
print("name" in student)

print("rollno" in student)

# Identity Operators
 
#  1.Is
o=[1,2,3]
p=o
q={1,2,3,}

print(o is p)

# 2.Is Not
print(o is not q)