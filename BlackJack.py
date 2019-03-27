import random
name1 = input("Insert Player1's name: ")
name2 = input("Insert Player2's name: ")
card_conversions = {
    'Ace': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'ten': 10,
    'Jack': 10,
    'Queen': 10,
    'King': 10
}

card1 = ['Ace', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'Jack', 'Queen', 'King']
card1 = random.choice(card1)
card3 = ['Ace', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'Jack', 'Queen', 'King']
card3 = random.choice(card3)
deal1 = input(name1 + " would you like two cards? (Yes/No): ")
Player1 = 0
Player2 = 0

if deal1 == "Yes":
    Player1 += card_conversions.get(card1) + card_conversions.get(card3)
    print(card1)
    print(card3)
    print(str(Player1) + " points")
    if Player1 > 21:
        print("You lose, " + name2 + " wins!")
        quit()
else:
    print("Your score is" + str(Player1) + " points")
    if Player1 >= Player2:
        print("You are beating " + name2)
    elif Player1 == Player2:
        print("You are tied with " + name2)
    else:
        print("You are losing to " + name2)


card2 = ['Ace', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'Jack', 'Queen', 'King']
card2 = random.choice(card2)
card4 = ['Ace', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'Jack', 'Queen', 'King']
card4 = random.choice(card4)

deal2 = input("\n" + name2 + " would you like two cards? (Yes/No): ")

if deal2 == "Yes":
    Player2 += card_conversions.get(card2) + card_conversions.get(card4)
    print(card2)
    print(card4)
    print(str(Player2) + " points")
    if Player2 > 21:
        print("You lose, " + name1 + " wins!")
        quit()
else:
    print("Your score is " + str(Player2) + " points")
    if Player2 >= Player1:
        print("You are beating " + name1)
    elif Player2 == Player1:
        print("You are tied with " + name1)
    else:
        print("You are losing to " + name1)


card5 = ['Ace', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'Jack', 'Queen', 'King']
card5 = random.choice(card5)
deal3 = input("\n" + name1 + "  would you like another card? (Yes/No): ")

if deal3 == "Yes":
    Player1 += card_conversions.get(card5)
    print(card5)
    print(str(Player1) + " points")
    if Player1 > 21:
        print("You lose, " + name2 + " wins!")
        quit()
else:
    print("Your score is " + str(Player1) + " points")
    if Player1 >= Player2:
        print("You are beating " + name2)
    elif Player1 == Player2:
        print("You are tied with " + name2)
    else:
        print("You are losing to " + name2)


card6 = ['Ace', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'Jack', 'Queen', 'King']
card6 = random.choice(card6)
deal4 = input("\n" + name2 + " would you like another card? (Yes/No): ")
if deal4 == "Yes":
    Player2 += card_conversions.get(card6)
    print(card6)
    print(str(Player2) + " points")
    if Player2 > 21:
        print("You lose, " + name1 + " wins!")
        quit()
else:
    print("Your score is " + str(Player2) + " points")
    if Player2 >= Player1:
        print("You are beating " + name1)
    elif Player2 == Player1:
        print("You are tied with " + name1)
    else:
        print("You are losing to " + name1)


card7 = ['Ace', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'Jack', 'Queen', 'King']
card7 = random.choice(card7)
deal5 = input("\n" + name1 + " would you like another card? (Yes/No): ")

if deal5 == "Yes":
    Player1 += card_conversions.get(card7)
    print(card7)
    print(str(Player1) + " points")
    if Player1 > 21:
        print("You lose, " + name2 + " wins!")
        quit()
else:
    print("Your score is " + str(Player1) + " points")
    if Player1 >= Player2:
        print("You are beating " + name2)
    elif Player1 == Player2:
        print("You are tied with " + name2)
    else:
        print("You are losing to " + name2)


card8 = ['Ace', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'Jack', 'Queen', 'King']
card8 = random.choice(card8)
deal6 = input("\n" + name2 + " would you like another card? (Yes/No): ")
if deal6 == "Yes":
    Player2 += card_conversions.get(card8)
    print(card8)
    print(str(Player2) + " points")
    if Player2 > 21:
        print("You lose, " + name1 + " wins!")
        quit()
else:
    print("Your score is " + str(Player2) + " points")
    if Player2 >= Player1:
        print("You are beating " + name1)
    elif Player2 == Player1:
        print("You are tied with " + name1)
    else:
        print("You are losing to " + name1)
