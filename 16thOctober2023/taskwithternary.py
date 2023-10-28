# difference between = and ==
# The equal-to operator ( == ) returns true if both operands have the same value;
# oherwise, it returns false .
# The not-equal-to operator ( != ) returns true if the operands don('t have the same value; otherwise, '
# 'it returns false)
###Area
radius = float(input("enter the radius\n"))
area = 3.14 * (radius)
print((area))

# Ternary operation
num1 = float(input("enter num1\n"))
num2 = float(input("enter num2\n"))
num3= float(input("enter num3\n"))

result = num1 if (num1>num2 and num1>num3)else(num2 if num2>num3 and num2>num1 else num3)
print(f"max{num1},{num2},and {num3} is{result}")


#calculate the square and cube
number=float(input("enter the number"))
square=number**2
cube=number**3
print(square)
print(cube)