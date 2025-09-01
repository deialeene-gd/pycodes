# print("hello")

# # name=input("Enter your name:")
# # print("Hello " + name)

# for i in range(1, 11):
#     print(f"{i}", end=" ")
#     if i%5==0:
#         print()


# print(" ")

# for i in range(10, 0, -1):
#     for o in range(1, i + 1):
#         print(f"{o}", end=" ")
#     print()

# row=5
# for i in range(1, row+1):
#     for space in range(row-i):
#         print(" ", end=" ")
#     for o in range(1, i + 1):
#         print(f"{o}", end=" ")
#     print()

# for i in range(1, row+1):
#     print(" " * (row - i) + " ".join(str(x) for x in range(1, i + 1)))

# for i in range(1, row+1):
#     print(" " * (row - i) + "* " * i)

# for i in range(row-1, 0, -1):
#     print(" " * (row - i) + "* " * i)

# while True:
#     name=input("Enter your name:")
#     if name.lower()=="exit":
#         break
#     print("Hello " + name)

# while True:
#     x=int(input("Enter number: "))
#     if x==0:
#         break
#     if x%2==0:
#         print(f"{x} is even")
#     else:
#         print(f"{x} is odd")

# while True:
#     x=str(input("Enter your name: "))
#     if x.lower()=="exit":
#         break
#     print("Hello " + x)

# for i in range(1, 21):
#     if i%3==0 and i%5==0:
#         print('FIzzBuzz')
#     elif i%3==0:
#         print('Fizz')
#     elif i%5==0:
#         print('Buzz')
#     else:
#         print(i)
# while True:
#     x=int(input("Enter positive integer: "))
#     if x==0:
#         break
    
#     if x%2==0:
#         for i in range(2, x + 1, 2):
#             print(i)
#     else:
#         print("odd number")
"""
        
x, y, z="Mike"
print(x)
print(y)   
print(z)
        
        """

""" 
print("Hello World")
x=y=z="Mike"
print(x + y + z)
x,y,z="Mike", "Esteron", "Acosta"
print(x + y + z)
course=["IT", "Math", "EE"]
x,y,z=course
print(x + y + z)
a=10
print(f"The number is: {a}")



print("Enter number1: ")
num1=int(input())
num2=int(input("Enter number2: "))

print(f"The number is: {num1+num2}") """

""" str1="Mike Acosta"
print(str1[5])
print(str1[-5])
print(str1[5:8])
print(str1[-5:-1])
print(str1[:])
print(str1[::-1])
print(str1[1:7:3])
print(str1[-6:-1:2])
print(str1[-6:-10:-2])

print(len(str1))

for y in str1:
    print(y)
    
str1=str1.split(" ")
for x in str1:
    print(x)
    
str2="Mike\'s \"Esteron\" Acosta"
print(str2) 



for x in range(1,101):
    print(f"{x}", end=" ")
    if x%5==0:
        print()
        print()
        
for x in range(1,6):
    for y in range(6,11):
        print(f"{x}{y}", end=" ")
    print()


for x in range(10,0,-1):
    print(f"{x}", end=" ")
        
while True:
    print("Enter number: ")
    x=int(input())
    if x<=0:
        break
"""





# for n in range(1, 15):
#     print(f'{n}', end=' ')
#     if n%5==0:
#         print()
#         print()
#         print()
#     if n%2==0:
#         print("0", end='')       
#     else:
#         print("*", end='') 

# for x in range(1,11):
#     print(f"{x}", end=" ")
#     if x%5==0:
#         print()
#         print()

# for i in range(1, 11):
#     for o in range(1, i + 1):
#         print(f"{o}", end=" ")
#     print()


# for i in range(3):
#     for o in range(5):
#         if o % 2 == 0:
#             print("*", end = " ")
#         else:
#             print("0", end=" ")
#     print()



mylist=["honda", "toyota", "nissan", "mitsubishi"]

print(mylist[2])

print(mylist[-1])

print(mylist[1:3])

print(mylist[-3:-1])

print(mylist[:3:2])

print(mylist[::2])

print(mylist[::-1])