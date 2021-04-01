import random
array = []
for i in range(4):
    r = random.randint(1, 4)
    array.append(r)
print(array)
count_1 = array.count(1)
if (count_1 == 2):
    print("False")
count_2 = array.count(2)
if (count_2 == 2):
    print("False")
count_3 = array.count(3)
if (count_3 == 2):
    print("False")
count_4 = array.count(4)
if (count_4 == 2):
    print("False")