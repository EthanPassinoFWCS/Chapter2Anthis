message = "this is a string variable and you can print this out with print or use it in any method that needs a string"
print(message.title()) 
# The above simply changes the first letter of each word to uppercase.

string = "testing python Stuff Here"
print(string.upper())
# The above simply sets all characters to uppercase
print(string.lower())
# The below simply sets all characters to lowercase

#There are many ways to add two strings together.

first_name = "John"
last_name = "Smith"

print(f"{first_name} {last_name}") 
# This is a way to actually add two strings together. Another way:
print(first_name + " " + last_name)

# The first way is the prefered way as it looks much nicer than the other one.

full_name	=	"{}	{}".format(first_name,	last_name) 
# This is a way to add two strings together

#Next is how to actually add tabs and newlines. This is very simple.

print("This\nis a new line.")
print("This\tis a tab")

# This is how you do them with \ and then a specific character. There are more than just this, but I am not going to list all of them.

# There is also a way to actually remove all whitespace /at the end/at the beggining/both.

msg = " Space "
print(msg)
print(msg.rstrip()) # removes from right
print(msg.lstrip()) # removes from left
print(msg.strip()) # removes from both