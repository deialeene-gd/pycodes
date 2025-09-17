cart = {0: "underware",
        1: "tank top",
        2: "jacket"}

print("Matrix size: ", len(cart))
for i in range(len(cart)):
    print(f"{i}: {cart[i]}")

while True:

    action = input("What would you like to do [A]dd item, [C]hange item, [R]emove item, [D]isplay item, [S]earch item? ").lower()

    sorry = "I'm sorry, not in the cart."

    if action == "a":
        key = input("Enter key: ")
        value = input("Enter value: ")
        if key.isdigit():
            cart[int(key)] = value
            print("Item added.")
        else:
            print("Invalid key.")

    elif action == "c":
        key = input("Enter key to search: ")
        if key.isdigit():
            keys = int(key)
            if keys in cart:
                new_value = input("Enter new value: ")
                cart[keys] = new_value
                print("Item updated.")
            else:
                print(f"{sorry}")
        else:
            print("Invalid key.")

    elif action == "d":
        print("Displaying value")
        print("Key \t Value")
        for key, value in cart.items():
            print(f"{key} \t {value}")

    elif action == "r":
        key = input("Enter key to search:")
        if key.isdigit():
            keys = int(key)
            if keys in cart:
                value = cart[keys]
                del cart[keys]
                print(f"The key {keys} with value {value} has been deleted.")
            else: 
                print(f"{sorry}")
        else:
            print("Invalid key.")

    elif action == "s":
        srch = input("Enter key/item to search: ")
        if srch in cart.values():
            print(f"Found {srch} item.")
        elif srch.isdigit():
            if int(srch) in cart.keys():
                print(f"Found key {srch}")
            else:
                print(f"{sorry}")
        else:
            print("Invalid key.")

    elif action == "*":
        print("Bye.")
        break

    else:
        print("Invalid action. Please choose A, C, D, R, or S.")

