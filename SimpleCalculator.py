num1 = int(input("First number: "))
opp = input("Opperation: ")
num2 = int(input("Second number: "))

match opp:
    case "+":
        print(num1+num2)
    case "-":
        print(num1-num2)
    case "*":
        print(num1*num2)
    case "/":
        print(num1/num2)