# Using the gets function
# (extremely lightweight function with little to no parameters, for reliability and speed)
# gets returns an A record for the domain given, if not available, returns None

from gogdns import gets

res = gets("google.com")

if isinstance(res, None):
    print("Invalid.")
else:
    print(f"The IP is {res}")