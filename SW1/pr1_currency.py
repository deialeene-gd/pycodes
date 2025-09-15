def convert_currency(dollar):
    ruppe = dollar * 88.21
    pound = dollar * 0.74
    yuan = dollar * 7.12
    return (ruppe, pound, yuan)

while True:
    str = input("\nEnter dollar amount: ")
    print("Dollar ($)\tIndian Ruppe (₹)\tBritish Pound(£)\tChina (Y)")
    if str == '*':
        print("Bye.")
        break

    money = str.split("@")
    for amount in money:
        if amount.isdigit():
            dollar = float(amount)
            ruppe, pound, yuan = convert_currency(dollar)
            print(f"{dollar:.2f}\t\t{ruppe:.2f}\t\t\t{pound:.2f}\t\t\t{yuan:.2f}")
        else:
            print("Invalid amount.")
