age= input("I see you'd like to buy some cigarettes. How old are you?")
age= int(age)

def paymentmethod(x):
        print("Here is your receipt. Thanks and have a great day!")

def paymentmethod2(x):
    payment2 = input("I'm sorry, please enter either a 1 for Cash or 2 for Credit.")
    y = int(payment2)
    if y == 1:
        print("Thanks! Have a nice day!")
    elif y == 2:
        print("Thanks! Have a nice day!!")
    else:
        paymentmethod2(y)

def savingspace(x):
    x = int(payment)
    if x == 1:
        paymentmethod(x)
    elif x == 2:
        paymentmethod(x)
    else:
        paymentmethod2(x)


if age < 21:
    if age >= 13:
        print("You're too young to buy these things!")
        print("Go find something else to buy.")
    else:
        print("This ain't a place for midgits son.")
        print("Come back with your parents next time.")

elif age < 125:
    if age <= 40:
        print("Sorry for the trouble. Pesky new laws in this county make us have to check.")
        payment= input("How'd you like to pay? Press 1 on the numpad for Cash or 2 for Credit.")
        savingspace(payment)
    else:
        print("Those good ol' cowboys amiright hehe, wouldn't be Texas without em!")
        payment= input("How'd you like to pay? Press 1 on the numpad for Cash or 2 for Credit.")
        savingspace(payment)
else:
    print("It's amazing that you're still smoking at this ripe old age. It's on the house. Enjoy.")

