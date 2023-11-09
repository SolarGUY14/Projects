import random

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
        number,n = DrawCard.getnumber()
        suite = DrawCard.getsuite()
        return f"You drew the {number} of {suite}!"
print(DrawCard.draw())



                  


            