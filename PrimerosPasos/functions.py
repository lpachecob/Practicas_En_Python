def hello(name):
    """devuelve un saludo"""
    print("hello", name)


# hello("Luis")
# hello("ryan")


def Suma(num1, num2):
    """devuelve la suma de dos numeros"""
    return num1 + num2


# print(Suma(50, 3))

add = lambda num1, num2: num1 + num2

print(add(10,30))