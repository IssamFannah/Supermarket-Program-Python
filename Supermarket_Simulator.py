
# Product selection
a = "Milk"
b = "Bread"
c = "Egg"
print("good morning sir, what you want. we have: Milk, Bread, Egg")

d = input("I want: ")

while d != "a" and d != "b" and d != "c":
    print("Product not found")
    d = input("I want: ")

if d == "a":
    a = "Milk"
    print(f"you want {a}")
elif d == "b":
    b = "Bread"
    print(f"you want {b}")
elif d == "c":
    c = "Egg"
    print(f"you want {c}")


# Quantity selection
quantity = int(input("Enter how much product you want: "))
print(f"you want {quantity}? ")
answer = input("(yes/no) ")

# Accepting quantity
if answer == "yes":
    if d == "a":
        a = "e"
        e = 10
        price = e * quantity
        print(f"you have {price}$ ")
    elif d == "b":
        b = "f"
        f = 20
        price = f * quantity
        print(f"you have {price}$ ")
    elif d == "c":
        c = "g"
        g = 15
        price = g * quantity
        print(f"you have {price}$ ")

# Quantity rejected
else:
    while answer == "no":
        quantity = int(input("Enter quantity again: "))
        print(f"you want {quantity}? ")
        if d == "a":
            a = "e"
            e = 10
            price = e * quantity
            print(f"you have {price}$ ")
        elif d == "b":
            b = "f"
            f = 20
            price = f * quantity
            print(f"you have {price}$ ")
        elif d == "c":
            c = "g"
            g = 15
            price = g * quantity
            print(f"you have {price}$ ")
        answer = input("are you sure about the quantity? (yes/no): ")
if answer == "yes":
        print("Ok let's continue")

        # Owning a loyalty card
        loyal = input("Does the customer have a loyalty card? (yes/no): ")
        if loyal == "yes":
            price = price - 5
            print(f"Ok, so your price is {price}$ ")

        # Not having a loyalty card
        else:
            print("No discount applied ")

        # Calculating the tax value on the product (in French language)
        # TVA = Value Added Tax
        # TTC = All Taxes Included
        print("TVA est 20% ")
        TVA = price * 0.20
        TTC = price + TVA

        # Total price
        print(f"Total price to pay is: {TTC}$ ")

        # The customer was expelled
else:
    print("Ok goodbye. You don't want to buy anything, just leave")
