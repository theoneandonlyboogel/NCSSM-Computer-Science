weather = {
    "sunny": "Maybe you should put some sunscreen on.",
    "rainy": "Maybe you should bring an umbrella.",
    "snowy": "Maybe you should wear thicker clothes and some snow boots.",
    "foggy": "Please use fog lights while driving."
}

while True:
    userInput = input("\nType exit to stop reporting weather.\nWhat's the Weather Like? ").lower()
    try:
        if userInput in weather:
            print(f"{weather[userInput]}")
            continue
        elif userInput == "exit":
            exit()
        else:
            print("I'm sorry, I don't understand that type of weather.")
    except(EOFError, ValueError, KeyError):
        exit()