



# Numbers in python are called integers (as in many languages)

# Heres some operators you can use in pythn.

x = 1
y = 2

print(x + y) # returns 3 as it adds 2 + 1 together
print(x - y) # returns -1 as it does: 1 - 2
print(x * y) # Returns 2 as it does 2 * 1
print(x/y) # Returns 1/2 (0.5) as it is 1 / 2

# Python also supports the order of operations too

print((x + y) * x * (x - y)) # Returns -3:
# (1 + 2) * 1 * (1 - 2)
# (3) * 1 * (-1)
# 3 * -1
# -3

# In python any number with a decimal point is actually called a float instead of an integers

# When you divide any two numbers EVEN if the result does not have a decimal point, you will always get a float

# If you mix a int and a float it will also always be a float 

# Python always defaults to a float in any operation that uses a float it in, (like dividing)


# In python when you're wriing long numbers, you group digits using underscores to make large unmbers more readable

large_number = 14_000_000_000

# When you print that number it actually removes the underscores from the print:

print(large_number)


