myStr = "String simple"

print(myStr.upper())
print(myStr.lower())
print(myStr.swapcase())
print(myStr.capitalize())
print(myStr.replace(" ", ""))
print(myStr.count("i"))
print("Se encontro en la posición: ", myStr.find("i"))
print(myStr.startswith("String"))
print(myStr.endswith("e"))
print(myStr.split(" "))
print(myStr.split(" ")[1])
print(len(str(myStr)))
print(myStr.index("i"))
print(myStr.isnumeric())
print(myStr.isalpha())
print(myStr[3])
print(myStr[3:7])
print(myStr[3:7:2])
print(myStr[::-1])
print(myStr[::-2])
print(myStr[::-3])
print(myStr[myStr.find("i")])

print("Mi texto es: " + myStr)
print(f"Mi texto es: {myStr}")
