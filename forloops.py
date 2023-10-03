letters = ['p', 'a', 'r', 'a', 'd', 'i', 'g', 'm']

for item in letters:
    print(item)

for i in range(5):
    print(i)

AnimalList = ['Cat','Dog', 'Tiger', 'Cow']

for item in AnimalList:
    print(item)

flowers = ['Jasmine', 'Lotus', 'Rose', 'Sunflower']

for item in flowers:
    print(item)
else:
    print("Done")

list1 = [5, 10, 15, 20]
list2 = ['Tomatoes', 'Potatoes', 'Carrots', 'Cucumbers']

for i in list1:
    for j in list2:
        print(i,j)

vehicles = ['Car','Cycle','Bus','Tempo']

for item in vehicles:
    if item == 'Bus':
        break
    print(item)

vehicles = ['Car','Cycle','Bus','Tempo']

for item in vehicles:
    if item > 'Bus':
        pass
    continue
print(item)

numbers = [12,3,56,67,89,90]
count = 0

print(sum(1 for i in numbers))

numbers = [12,3,56,67,89,90]
sum = 0

for i in numbers:
    sum += i

print(sum)

numbers = [2,5,6,10,15,20,25]

for i in numbers:
    if (i % 5 ==0):
        print(i)

list1 = ['Mango','Banana','Orange']
list2 = []

list2 = list1.copy()

print(list2)

numbers4 = [1,4,50,80,12]
for i in numbers4:
    print(max(numbers4))
    break
    
numbers = [1,4,50,80,12]
for i in numbers:
    print(min(numbers))
    break

numbers = [1,4,50,80,12]
for i in numbers:
    print(sorted(numbers))
    break

numbers = [1,4,50,80,12]
for i in numbers:
    print(sorted(numbers, reverse=True))
    break

for i in range(3, 21):
    if (i % 3 == 0):
        print(i)

for i in range(5, 20):
    if (i % 5 == 0):
        print(i)

for i in reversed(range(11)):
    print(i)