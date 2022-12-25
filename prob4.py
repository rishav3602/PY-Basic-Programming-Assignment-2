# 4. Write a Python program to solve quadratic equation?

import cmath


class Quadratic:
    def __init__(self):
        self.a = int(input("Enter the value of a : "))
        self.b = int(input("Enter the value of b : "))
        self.c = int(input("Enter the value of c : "))
        self.d = (self.b**2) - (4*self.a*self.c)
        self.sol1 = (-self.b-cmath.sqrt(self.d))/(2*self.a)
        self.sol2 = (-self.b+cmath.sqrt(self.d))/(2*self.a)
        print (f"The solutions of the equation is {self.sol1} and {self.sol2}")

eqn = Quadratic()

    