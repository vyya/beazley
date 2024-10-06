# unpacking list to a set of variables, you may throw away variable name using _ underscore


data = ['MSFT', 50, 90.15, (2024, 12, 21)]
name, shares, price, (_, month, day) = data
print(f"I've bought {shares} of {name} shares for {price}$ on {day}/{month}" )

# unpacking works for any iterables, including strings
s = "Hello"
a, b, c, d, e = s
print(b, d)

