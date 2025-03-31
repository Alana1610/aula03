time1 = input("digite o nome do primeiro time")
time2 = input("digite o numero do segundo time")
golsm = int (input("diga a quantidade de gols marcados "))
golsv = int(input("diga a quantidade de gols marcados"))

if golsm>golsv:
    print (f"vitoria do {golsm}")

else:
    if golsv>golsm:
        print (f"vitoria do {golsv}")
    else:
        if golsv<=golsm:
            print (f"empate")

