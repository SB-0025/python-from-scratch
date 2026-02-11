# type casting
score = "100" 
print(score ,type(score)) # string 
val = int(score)
print(val, type(val)) # int

price = 19.635
price_in_int = int(price)
print(price_in_int, type(price_in_int))


# Arithmetic Operators 
# +, -, /, *, %, **, //

a = 20
b = 3

# addition
print("Add: ", a+b)

# subtraction
sub = a-b
print("Sub:" , sub)

# divide
div = a/ b
print("Div: ", div)

# floor division(gives the integer part only)
print(f"Floor Division: {a//b}")

# modulus(remainder)
print(f"Remainder: {a%b}")

# power
print(f"Power: {a**b}")

