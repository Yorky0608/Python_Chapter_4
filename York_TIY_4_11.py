from Examples.York_Working_with_Part_of_a_List import friend_foods

pizzas = ["no cheese", "supreme", "taco"]
for i in pizzas:
    print(f"I like {i} pizza!")
print("I really love pizza (eh, its meh).")
friend_pizzas = pizzas[:]
pizzas.append("sausage")
friend_pizzas.append("cheese")
print(f"My favorite pizzas are:", end=' ')
[print(pizzas[i], end=', ') for i in range(len(pizzas)-1)]
print(pizzas[len(pizzas)-1], end='')
print(f"\nMy friend's favorite pizzas are:", end=' ')
[print(friend_pizzas[i], end=', ') for i in range(len(friend_pizzas)-1)]
print(friend_pizzas[len(friend_pizzas)-1], end='')
