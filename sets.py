# A set is an unordered collection with no duplicate elements

items = {"arrow", "spear", "arrow", "arrow", "rock"}

print(items)  # it will not print duplicate elements
print(len(items))

if "rocks" in items:
    print("rock found")
else:
    print("rocks not found")

# Create an empty set and use add
a = set()
a.add(1)
a.add(2)
a.add("cinque")
print(a)    # the order is not important

b = set()
b.add(2)

print("a is a superset of b: " + str(a.issuperset(b)))
