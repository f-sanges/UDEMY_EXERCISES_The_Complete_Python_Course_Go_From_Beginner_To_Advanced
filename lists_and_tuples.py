# list

list1 = ['uno', 'due', 3, 'quattro', 5]

length = len(list1)

print(list1[1:4])

print("list1 length: " + str(length))  # length

print("Index of the element 'quattro': " + str(list1.index('quattro')))  # index
del list1[3]  # delete an element
print("list1 after deletion of the third element: " + str(list1))

list1.insert(3, 'quattro')
print("list1 after insert of the element 'quattro' at the 3th position: " + str(list1))

list2 = list1 * 2  # repetition
print(list2)

list3 = [x ** 2 for x in range(1, 11)]
print(list3)

# list comprehension

a = [1, 2, 3, 4, 5]
b = []
for numbers in a:
    b.append(numbers)
print("list b: " +str(b))

# ====================== tuple ======================

tup1 = (1, 2, 'tre')
print(tup1)

tup2 = (4,)  # the comma at the end is necessary
tup3 = tup1 + tup2
print(tup3)
for element in tup3:  # for loop
    print(element)

for elements in [0, 1, 2]:
    print('xxx')
del tup3  # delete a tuple
# print(tup3)
