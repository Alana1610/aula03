a = int (input("insira o numero de a"))
b = int(input("insira o numero de b"))

print(f"a = {a} b = {b}")

aux = a
a = b
b = aux

print(f"a = {a} b = {b}")