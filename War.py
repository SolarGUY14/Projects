import random

class War:
    def __init__(self,card1,card2) -> None:
        self.card1 = card1
        self.card2 = card2
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
        def draw():
            number,n = War.DrawCard.getnumber()
            suite = War.DrawCard.getsuite()
            return f"the {number} of {suite}",n
    def War():
        card1,Player1 = War.DrawCard.draw()
        print(f"Player 1 has drew {card1}")
        card2,Player2 = War.DrawCard.draw()
        while card1 == card2:
            card2,Player2 = War.DrawCard.draw()
        print(f"Player 2 has drew {card2}")
        

       
        if Player1 > Player2:
            print(f"Since {card1} is greater than {card2}, Player 1 wins!!")
        elif Player2 > Player1:
            print(f"Since {card2} is greater than {card1}, Player 2 wins!!")
        elif Player1 == Player2:
            print("We have a draw. TIME FOR ANOTHER WAR!")
            War.War()

War.War()



                  
