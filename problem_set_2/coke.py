coke = 50

while coke > 0:
    print(f"Amount Due: {coke}")
    coin = int(input("Insert Coin: "))
    if coin == 5 or coin == 10 or coin == 25:
        coke -= coin

print(f"Change Owed: {abs(coke)}")
