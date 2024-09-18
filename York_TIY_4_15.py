foods = ('orange chicken', 'fired rice', 'pizza', 'steak', 'shrimp')
([print(i) for i in foods])
#foods[0] = 'lo mein'

print()

foods = ('lo mein', 'fired rice', 'pizza', 'steak', 'shrimp cocktail')
([print(i) for i in foods])


my_foods = ['pizza', 'falafel', 'carrot cake']

friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
for i in my_foods:
    print(i)
print("\nMy friend's favorite foods are:")
for i in friend_foods:
    print(i)


my_foods = ['pizza', 'falafel', 'carrot cake']

# This doesn't work:
friend_foods = my_foods
my_foods.append('cannoli')
friend_foods.append('ice cream')

print("\nMy favorite foods are:")
[print(i) for i in my_foods]
print("\nMy friend's favorite foods are:")
[print(i) for i in friend_foods]


list = []

for i in range(1,11):
    list.append(i**3)
for i in list:
    print(i)

print(f"The first three items in the list are: {list[0:3]}")
print(f"Three items from the middle of the list are: {list[4:7]}")
print(f"The last three items in the list are: {list[7:10]}")