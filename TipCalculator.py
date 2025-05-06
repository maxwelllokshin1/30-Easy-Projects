price = float(input("Enter the price of the bill: "))

for tip in range(18, 24, 2):
    print(f"{tip}% --> {price + (price*(tip/100))}")