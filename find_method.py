value = "cat picture is cat picture plus picture"

# Find first index of the string

i = value.find("picture")
print("First occurrence of picture: " + str(i))

c = value.rfind("picture")  # rfind
print("rfind di picture: " + str(c))

# Find first index of this string after previous index
b = value.find("picture", i + 1)
print("Second occurrence of picture: ", b)

# loop to find the index of every value in a string
location = 0
while True:
    location = value.find("picture", location + 1)

    if location == -1:
        break
    print("location: ", location)

# Other method to loop to find the index of every value in a string
value2 = "cat picture is cat picture plus picture"
locazione = len(value2)
print("length of value2: ", locazione)
while True:

    locazione = value2.rfind("picture", 0, locazione)
    if locazione == -1:
        break
    print("locazione: ", locazione)

# print(value.find("daog"))
if value.find("dog") == -1:
    print("not found")
else:
    print("found")
