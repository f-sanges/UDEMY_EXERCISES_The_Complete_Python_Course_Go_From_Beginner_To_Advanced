# list

list1 = ['uno', 'due', 3, 'quattro', 5]

length = len(list1)

print(list1[1:4])

print(length)

list2 = list1 * 2  # repetition
print(list2)

# tuple

tup1 = (1, 2, 'tre')
print(tup1)

tup2 = (4,)                 # the comma at the end is necessary
tup3 = tup1 + tup2
print(tup3)
for element in tup3:        # for loop
    print(element)

for elements in [0, 1, 2]:
    print('xxx')
del tup3                    # delete a tuple
# print(tup3)
