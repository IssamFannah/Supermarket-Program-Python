
a = "game controller"
b = "gaming headset"
c = "gaming mouse"

print("Wrlcome to Arcade Game Shop!")
print("We have:")
print("a - game controller: 250DH")
print("b - gaming headset: 180DH")
print("c - gaming mouse: 120DH")


d = input("Chosse your product: ")

while d != "a" and d != "b" and d != "c":
    print("Product not found")
    d = input("Chosse your product: ")

if d == "a":
    d = 250
    a = "game controller"
    print(f"You selected: {a}")

elif d == "b":
    d = 180
    b = "gaming headset"
    print(f"You selected: {b}")

elif d == "c":
    d = 120
    c = "gaming mouse"
    print(f"You selected: {c}")


# Quantity of product
quantity = int(input("Enter quantity: "))

product = quantity * d


print(f"You want {quantity} products?")
e = input("(yes/no)")

if e == "yes":
    price = d * quantity
    print(f"Your price is {price} DH ")

    print("Do you have a membership card? ")
    f = input("(yes/no)")
    if f == "yes":
        print("A discount of 20 DH has been applied!")
        price = price - 20
        print(f"Your price after discount is {price} DH")

    else:
        print(f"So, your price is still {price} DH")
    
else:
    while e == "no":
        quantity = int(input("Enter quantity: "))

        product = quantity * d


        print(f"You want {quantity} products?")
        e = input("(yes/no)")

        if e == "yes":
            price = d * quantity
            print(f"Your price is {price} DH ")

            print("Do you have a membership card? ")
            f = input("(yes/no)")
            if f == "yes":
                print("A discount of 20 DH has been applied!")
                price = price - 20
                print(f"Your price after discount is {price} DH")

            else:
                print(f"So, your price is still {price} DH")
        
        

print("TVA est 20%")
TVA = price * 0.20
print(f"TVA est {TVA}")

TTC = price + TVA
print(f"Total price: {TTC} DH")
print("Thank you for shopping with us!")


        
