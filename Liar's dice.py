# Python Child's Dice (Dice blackjack to 18, Dealer can go forever within 18.)
# (Dice are held secret until both stand.)
# cannot have more than 4 hits
# If your Dice Deck only has 2 2's 2 3's 2 4's 2 5's or 2 6's, You automatically win. (1/36, Chance)
# Everytime you want another dice you must place another bet that is higher then your previous one.

import random
import time

# Game constants
MAX_HITS = 4
TARGET = 18
DECK_COUNTS = {2: 2, 3: 2, 4: 2, 5: 2, 6: 2}  # 2 of each 2-6

def check_deck_win(dice):
    """Check if player's dice match the auto-win condition"""
    from collections import Counter
    counts = Counter(dice)
    for num, required in DECK_COUNTS.items():
        if counts[num] >= required:
            return True
    return False

def calculate_total(dice):
    """Sum of dice values"""
    return sum(dice)

# Player's ante bet
AnteBet = int(input("What is your ante bet?: "))
bets = [AnteBet]  # Track all bets

# Initialize player dice and dealer total (secret until end)
player_dice = []
dealer_total = random.randint(1, 25)  # Dealer secret total (1-25)

# Deal starting two dice to player
dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)
player_dice.extend([dice1, dice2])
print(f"Starter Dice: {player_dice}")

hits = 2  # Already have 2 dice

# Check auto-win after starter dice
if check_deck_win(player_dice):
    print("Your Dice Deck only has 2 2's, 2 3's, 2 4's, 2 5's or 2 6's! You automatically win. (1/36 chance)")
    print("Player wins!")
    exit()

# Player turn - up to 4 total dice (2 more hits max)
while hits < MAX_HITS:
    choice = input(f"Current total: {calculate_total(player_dice)}. Hits used: {hits}/{MAX_HITS}. Another die? (Y/N): ").strip().upper()
    
    if choice == "N":
        print("Player stands.")
        break
    elif choice == "Y":
        # Must place higher bet
        next_bet = int(input(f"Current bets: {bets}. Place next bet > {bets[-1]}: "))
        if next_bet <= bets[-1]:
            print("Bet must be higher than previous! Standing.")
            break
        bets.append(next_bet)
        
        # Roll additional die
        additional = random.randint(1, 6)
        player_dice.append(additional)
        print(f"Additional die: {additional}. Updated dice: {player_dice}")
        hits += 1
        
        # Check auto-win after each hit
        if check_deck_win(player_dice):
            print("Your Dice Deck now has 2 2's, 2 3's, 2 4's, 2 5's or 2 6's! You automatically win.")
            print("Player wins!")
            exit()
    else:
        print("Invalid input! Standing.")
        break

# Reveal dealer total and resolve
print(f"\nPlayer final dice: {player_dice}")
print(f"Player total: {calculate_total(player_dice)}")
print(f"Dealer total: {dealer_total}")

player_total = calculate_total(player_dice)

if player_total > TARGET:
    print("Player busts! Dealer wins.")
elif dealer_total > TARGET:
    print("Dealer busts! Player wins.")
elif dealer_total == TARGET:
    print("Dealer hits 18! Dealer wins.")
elif dealer_total > player_total:
    print("Dealer wins.")
elif dealer_total < player_total:
    print("Player wins!")
else:
    print("Push! Draw between player and dealer.")

# Show total bet for fun
print(f"Total bet placed: {sum(bets)}")