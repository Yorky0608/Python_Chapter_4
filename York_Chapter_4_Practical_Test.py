People = [["Michael Buchanan", "Hersey"], ["Seth Johns", "Gummy Bears"], ["Yaseen Kedio", "Snickers"], ["Trace Likens", "Candy Corn"], ["Miguel Moreno", "Reese's"], ["Josue Roque", "Twix"], ["Julian-Jordan Starks", "Sour Patch Kids"]]
for p in People:
    for c in p:
        if c == "Gummy Bears":
            print(f"This is the candy we chose: {c}")
            selected_candy = c
Prices = [["Hersey", "$1.32"],["Gummy Bears", "$1.24"],["Snickers", "$1.32"],["Candy Corn", "$2.48"],["Reese's", "$2.37"],["Twix", "$1.97"]]
for p in People:
    for c in p:
        for m in Prices:
            for a in m:
                if c == a:
                    print(c, m[1])
alt_candy = People[:]

alt_candy.append("Almond Joy")
alt_candy.append("Btterfinger")
print(f"If {selected_candy} is not available the replace it with {alt_candy[7]} ")
print(f"If {selected_candy} is not available the replace it with {alt_candy[8]} ")
print(alt_candy)
print(People)