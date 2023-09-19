import random
import copy
class Card:
    #number = J,Q,K,A like in the deck
    #counter - J=11,Q=12,K=13,A=14 - for easier enumerating in the future
    #colour 1:clubs, 2:diamonds, 3:hearts, 4:spades
    def __init__ (self,counter:int,colour:int):
        self.counter=counter
        
        if (self.counter == 11):   self.number = 'J'
        elif (self.counter == 12): self.number = 'Q'
        elif (self.counter == 13): self.number = 'K'
        elif (self.counter == 14): self.number = 'A'
        else: self.number = counter
        
        if(colour == 1): self.colour = 'trefl'
        if(colour == 2): self.colour = 'karo'
        if(colour == 3): self.colour = 'kier'
        if(colour == 4): self.colour = 'pik'

    def points(self):
        if (self.counter > 10): return self.counter - 10
        else: return 0
            
    def show(self):
        print('Moja karta to: ' + str(self.number)+' ' +str(self.colour))
        
    def __eq__(self,other):
        return self.colour==other.colour and self.number==other.number
      
class Deck:
    def __init__ (self):
        self.deck=[]
        self.honors=[] #additional list, it'd be helpful while dealing under particular conditions
        self.numbers=[] 
        for i in range (4):
            for j in range(13):
                c = Card(j+2,i+1)
                self.deck.append(c)
                if(j+2>10):self.honors.append(c)
                else:self.numbers.append(c)
    
    def show(self):
        for i in range(len(self.deck)):
            self.deck[i].show()  
     
    def put_cards(self,x:list): #x is a list of random indexes which should be used to grab cards from the deck
        s=[] #list of prepared cards
        h=[] #list of prepared honors
        n=[] #list of prepared numbers
        for i in range (len(x)):
            s.append(self.deck[x[i]])
            if(self.deck[x[i]].counter>10):h.append(self.deck[x[i]])
            else:n.append(self.deck[x[i]])
        self.deck = [self.deck[i] for i in range(len(self.deck)) if i not in x]
        for i in range(len(h)):
           self.honors.remove(h[i])
        for i in range(len(n)):
           self.numbers.remove(n[i])
        return s
    
    def put_honors(self,x:list): #x is a list of random indexes which should be use to grab honors from the deck
        h=[] #list of prepared honors
        for i in range (len(x)):
            h.append(self.honors[x[i]])#get honor from honors list
        self.deck = [self.deck[i] for i in range(len(self.deck)) if i not in x] #actualization of card list 
        for i in range(len(h)):
           self.honors.remove(h[i]) #actualization of honor list
        return h

    def put_numbers(self,x:list): #x is a list of random indexes which should be use to grab honors from the deck
        n=[] #list of prepared numbers
        for i in range (len(x)):
            n.append(self.numbers[x[i]])#get numbers from honors list
        self.deck = [self.deck[i] for i in range(len(self.deck)) if i not in x] #actualization of card list 
        for i in range(len(n)):
           self.numbers.remove(n[i]) #actualization of numbers list
        return n 

    def remove_distinct_cards(self,sample_cards):
        for i in range(len(sample_cards)):
            self.deck.remove(sample_cards[i])
        

    
class Hand:
    def __init__ (self):
        self.hand = []
        self.number_of_cards=0
        self.number_of_points=0
    def random_deal(self,deck:Deck):
        num=random.sample(range(0,len(deck.deck)),13)
        cards = deck.put_cards(num)
        for i in range(len(cards)):
            self.hand.append(cards[i])
            self.number_of_cards+=1
            self.number_of_points+=cards[i].points()
    def show(self):
        spades = []
        hearts = []
        diamonds = []
        clubs = []
        spadesStr = '♠ '
        heartsStr = '♥ '
        diamondsStr = '♦ '
        clubsStr = '♣ '
        for i in range(len(self.hand)):
            if self.hand[i].colour == 'trefl': clubs.append(self.hand[i])
            elif self.hand[i].colour == 'karo': diamonds.append(self.hand[i])
            elif self.hand[i].colour == 'kier': hearts.append(self.hand[i])
            elif self.hand[i].colour == 'pik': spades.append(self.hand[i])
        spades = sorted(spades, key=lambda x: x.counter*(-1))
        hearts = sorted(hearts, key=lambda x: x.counter*(-1))
        diamonds = sorted(diamonds, key=lambda x: x.counter*(-1))
        clubs = sorted(clubs, key=lambda x: x.counter*(-1))

        for i in range(len(spades)):
            spadesStr = spadesStr + str(spades[i].number) + ' '
        print(spadesStr)

        for i in range(len(hearts)):
            heartsStr = heartsStr + str(hearts[i].number) + ' '
        print(heartsStr)

        for i in range(len(diamonds)):
            diamondsStr = diamondsStr + str(diamonds[i].number) + ' '
        print(diamondsStr)

        for i in range(len(clubs)):
            clubsStr = clubsStr + str(clubs[i].number) + ' '
        print(clubsStr)
            #self.hand[i].show()

    def copy(self,hand,board):
        pass
    def points_deal(self,min:int,max:int,deck:Deck):
        pom = 0
        deck_copy = copy.copy(deck)
        while(pom==0):
            sample_hand = Hand()
            sample_hand.random_deal(deck_copy)
            if((sample_hand.number_of_points>=min) and (sample_hand.number_of_points<=max)): pom=1
        deck.remove_distinct_cards(sample_hand.hand)
        cards = sample_hand.hand
        for i in range(len(cards)):
            self.hand.append(cards[i])
            self.number_of_cards+=1
            self.number_of_points+=cards[i].points()

    def points_deal2(self,min:int,max:int):
        deck = Deck()

        if(min<0 or max>37 or min>max):
            print('pojebalo cie')
            return 0

        #prepare an array of indexes to exclude from later on
        availableIndexes=[]
        for i in range(52):
            availableIndexes.append(i)

        while(self.number_of_cards<13):
            #choose a random card
            randomIndex=random.choice(availableIndexes)
            card=deck.deck[randomIndex]
            points=card.points()
            if(self.number_of_points + points <= max): #if not too much points after adding a new card then add
                self.hand.append(card)
                self.number_of_points += points
                self.number_of_cards += 1
            availableIndexes.remove(randomIndex)

        while(self.number_of_points < min): #if not enough points keep drawing until you draw enough
            randomIndex = random.choice(availableIndexes)
            card = deck.deck[randomIndex]
            points = card.points()
            if(self.number_of_points + points <= max):
                self.hand.append(card)
                self.number_of_points += points
                self.number_of_cards += 1
            availableIndexes.remove(randomIndex)

        
        while(self.number_of_cards>13):
            pointsToDelete=0
            if[self.hand[i].points()==pointsToDelete]:
                self.number_of_cards -= 1
                self.number_of_points -= self.hand[i].points()
                self.hand.remove(self.hand[i])
                i=0
            if[i==12]:
                i = 0
                pointsToDelete+=1
            i+=1

class Board:
    def __init__ (self,N:Hand,E:Hand,S:Hand,W:Hand,n:int):
        self.N=N
        self.E=E
        self.S=S
        self.W=W
        self.number = n
    def random_deal(self,deck:Deck):
        self.N.random_deal(deck)
        self.E.random_deal(deck)
        self.S.random_deal(deck)
        self.W.random_deal(deck)
    def point_deal(self,):
        pass
        
    






