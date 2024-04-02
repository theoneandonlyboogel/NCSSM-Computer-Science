#Chapter 1
for step in range(1, 6):
  print(step)

#Chapter 2
def decode_riddle(letter, times):
    if times == 0:
       return ""
    else:
       return letter + decode_riddle(letter, times-1)

print(decode_riddle("C", 3))

#Chapter 3
def reveal_code(base, exponent):
    return base ** exponent

print(reveal_code(2,3))

#Chapter 4
gold = 10
silver = 20
combination = gold + silver
print(f"The vault opens with combination: {combination}")

#Chapter 5
def final_function(c1, c2, c3, c4):
    if c1 + c2 + c3 + c4 == 46:
        print("You have crafted the Code Key!")
    else:
        return "Keep trying, Coder!"

print(final_function(5, 3, 8, 30))
