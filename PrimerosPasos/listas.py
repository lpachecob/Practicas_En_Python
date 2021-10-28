lista = [1, "hola", 1.34, True, [1, 2, 3]]
colors = ["red", "green", "blue"]

numerlist = list((1, 2, 3, 4, 5))
# print(numerlist)

ListaRango = list(range(1, 101))
# print(ListaRango)

# print(dir(colors))
# print(len(colors))
print(lista[4])
print(lista[4][1])
print("green" in colors)
colors[1] = "yellow"
print(colors)
colors.append("black")
print(colors)
colors.extend(["white", "black"]) 
print(colors)
colors.extend(("pink","violet"))
print(colors)
colors.insert(1, "orange")
print(colors)
colors.pop()
print(colors)
colors.remove("red")
print(colors)
colors.sort(reverse=True)
print(colors)

print(colors.index("yellow"))
print(colors.count("yellow"))

