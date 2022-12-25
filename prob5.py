# 5.Write a Python program to swap two variables without temp variable?

x = int(input("Enter the value of x : "))
y = int(input("Enter the value of y : "))

x,y = y,x

print("x =",x)
print("y =",y)