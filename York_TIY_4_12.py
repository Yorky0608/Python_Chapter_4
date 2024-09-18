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