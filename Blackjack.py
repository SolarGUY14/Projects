import random
global player_hand
global dealer_hand
global p_score
global d_score
p_score = []
d_score = []
player_hand = []
dealer_hand = []
global Winner
global money 
money = [500]
class BlackJack:
    def __init__(self):
        pass
        
    class DrawCard:
        def __init__(self,suite = None,number = None):
            self.suite = suite
            self.number = number
        def getsuite(Suites = ["Hearts","Clubs","Diamonds","Spades"]):
            suite = random.choice(Suites)
            return suite
        def getnumber(Numbers = list(range(2,15))):
            n = random.choice(Numbers)
            if n == 11:
                number = "Jack"
            elif n == 12:
                number = "Queen"
            elif n == 13:
                number = "King"
            elif n == 14:
                number = "Ace"
            else:
                number = n
            number = str(number)

            return number,n
        def draw(hand):
            number,n = BlackJack.DrawCard.getnumber()
            suite = BlackJack.DrawCard.getsuite()
            card = f"{number} of {suite}"
            if n == 14:
                n = 11
            elif n == 11 or n == 12 or n == 13:
                n = 10
            if card in hand:
                BlackJack.DrawCard.draw(hand)
            hand.append(card)
            return n
    def Make_Bet():
        print("Bets can only be made as multiples of 5.")
        bet = input(f"\nPlease make a bet. \nYou have ${money[0]}.  ")
        while True:
            try:
                if bet.lower() == "all in":
                    break
                elif bet.isdigit():
                    bet = int(bet)
                else:
                    bet = int(bet)
            except:
                print("\nNot a valid bet. Pleas try again.")
                bet = input(f"\nPlease make a bet. \nYou have ${money[0]}.  ")
            else:
                break
        try:
            if bet.lower() == "all in":
                bet = money[0]
                money[0]= money[0] - bet
                print("\nYOU'VE GONE ALL IN!!!!")
                return bet
        except:
            pass
        while bet <= 0 or bet % 5 != 0 or bet > money[0]:
            print("\nNot a valid bet. Pleas try again.")
            bet = int(input(f"\nPlease make a bet. \nYou have ${money[0]}.  "))
        money[0]= money[0] - bet
        return bet
    def Change_Money(Winner,bet):
        if Winner ==True:
            money[0] = money[0] + bet*2
        elif Winner == None:
            print("It's a tie. Your money is unchanged")
            money[0]  = money[0] + bet
        
    def Play():
        bet = BlackJack.Make_Bet()
        p_score.append(BlackJack.DrawCard.draw(player_hand))
        p_score.append(BlackJack.DrawCard.draw(player_hand))
        d_score.append(BlackJack.DrawCard.draw(dealer_hand))
        d_score.append(BlackJack.DrawCard.draw(dealer_hand))
        print("\nYour Cards are: ",end = '')
        for i in player_hand:
            print(i,end = '. ')
        print(f"\nYour score is: {sum(p_score)}")
        if sum(p_score) == 21:
            print("\nYOU'VE HIT BLACKJACK!")
        decision  = input("\nWould you like to hit or stand? h/s: ")
        while decision != "h" and decision != "s":
                print("Error! Try again.")
                decision  = input("\nWould you like to hit or stand? h/s: ")
        while decision == "h":
            p_score.append(BlackJack.DrawCard.draw(player_hand))
            if sum(p_score) > 21:
                if 11 in p_score:
                    for i in p_score:
                        if i == 11:
                            p_score.remove(i)
                            p_score.append(1)
                            if sum(p_score) <=21:
                                break
                    if sum(p_score) >21:
                        print("\nYour cards are: ")
                        for i in player_hand:
                            print(i,end = '. ')
                        print(f"\nYour score is: {sum(p_score)}. You've gone bust.")
                        break

                else:
                    print("\nYour cards are: ")
                    for i in player_hand:
                        print(i,end = '. ')
                    print(f"\nYour score is: {sum(p_score)}. You've gone bust.")
                    break
            if sum(p_score) == 21:
                print("\nYour cards are: ")
                for i in player_hand:
                    print(i,end = '. ')
                print("\n\nYOU'VE HIT BLACKJACK!")
                break
            if sum(p_score) < 21:
                print("\nYour cards are: ")
                for i in player_hand:
                    print(i,end = '. ')
                print(f"\nYour score is: {sum(p_score)}")
            decision  = input("\nWould you like to hit or stand? h/s: ")
            while decision != "h" and decision != "s":
                print("Error! Try again.")
                decision  = input("\nWould you like to hit or stand? h/s: ")
        while sum(d_score) < 17:
            d_score.append(BlackJack.DrawCard.draw(dealer_hand))
        print(f"\nThe dealer has scored {sum(d_score)}.")
        if sum(p_score) == 21 and sum(d_score) == 21:
            Winner = None
            BlackJack.Change_Money(Winner,bet)
            return "Both of you hit Blackjack. This round ends in a tie"
        elif sum(p_score) > 21 and sum(d_score) <=21:
            Winner = False
            BlackJack.Change_Money(Winner,bet)
            return "Dealer wins!"
        elif sum(p_score) <= 21 and sum(p_score) > sum(d_score):
            Winner = True
            BlackJack.Change_Money(Winner,bet)
            return "You win!"
        elif sum(p_score) < 21 and sum(d_score)<=21 and sum(p_score) < sum(d_score):
            Winner = False
            BlackJack.Change_Money(Winner,bet)
            return "Dealer wins!"
        elif sum(p_score) > 21 and sum(d_score) > 21:
            Winner = False
            BlackJack.Change_Money(Winner,bet)
            return "Both you and the dealer have gone bust. Dealer automatically wins!"
        elif sum(p_score) <= 21 and sum(d_score) > 21:
            Winner = True
            BlackJack.Change_Money(Winner,bet)
            return "You win!"
        elif sum(p_score) == sum(d_score):
            Winner = None
            BlackJack.Change_Money(Winner,bet)
            return "You both have the same score. This round ends in a tie"
print("""  These are the rules of Blackjack:
      
      You and the Dealer are dealt 2 cards each, each card is assigned their already displayed numerical value.
      Face cards are assigned the value 10, and the Ace switches between 11 and 1, whichever number works better.
      You will have to decide whether you choose to hit, or stand. If you hit you recieve another card. 
      If you stand you choose to stay at your current score.
      If you go over 21, you bust and you lose.
      If your score totals to be 21, then that means you got "Blackjack."
      You cannot see the dealers cards, only their score at the end.
      You win as long as you do not bust and score higher than the dealer. If the dealer busts and you do not, then you also win that way.
          """)            
play = input("Would you like to play Blackjack? y/n ").lower()
while play != "y" and play != "n":
    print("Error! Try again.")
    play = input("\nWould you like to play Blackjack? y/n ").lower()
while play == "y":
    print(BlackJack.Play())
    print(f"\nYou now have ${money[0]}.")
    if money[0] <= 0:
        print("\nYOU'VE GONE BANKRUPT XD")
        print("\nThat's the end of the line.")
        break
    player_hand = []
    p_score = []
    dealer_hand = []
    d_score = []
    play = input("\nWould you like to play another round? y/n ").lower()
    while play != "y" and play != "n":
        print("Error! Try again.")
        play = input("\nWould you like to play another round? y/n ").lower()
if play == "n":   
    print("\nThanks for your time!")