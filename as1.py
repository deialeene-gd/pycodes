while True:
    row = int(input("Enter row: "))
    col = int(input("Enter column: "))
    srch = int(input("Enter search number: "))

    if row <= 0 or col <= 0:
        print("Both numbers must be greater than 0. Exiting... ")
        break

    for i in range(1, row + 1):
        for o in range(1, col + 1):
            product = i * o
            if product == srch:
                print(f"[{product:2}]", end=" ")
            else:
                print(f"{product:4}", end=" ")
        print()
    print()
