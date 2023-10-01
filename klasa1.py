from ast import List
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
    
    def colour_to_number(self):
        if(self.colour == 'trefl'): return 0
        elif(self.colour == 'karo'): return 1
        elif(self.colour == 'kier'): return 2
        elif(self.colour == 'pik'): return 3
        
class Deck:
    def __init__ (self,*args):
        self.deck=[]
        self.honors=[] #additional list, it'd be helpful while dealing under particular conditions
        self.numbers=[] 
        if (len(args)==0):
            for i in range (4):
                for j in range(13):
                    c = Card(j+2,i+1)
                    self.deck.append(c)
                    if(j+2>10):self.honors.append(c)
                    else:self.numbers.append(c)
        else:
            for i in range (len(args[0])):
                self.deck.append(args[0][i])


    def show(self):
        for i in range(len(self.deck)):
            self.deck[i].show()  
     
    def put_cards(self,x:list): #x is a list of random indexes which should be used to grab cards from the deck
        s=[] #list of prepared cards

        for i in range (len(x)):
            s.append(self.deck[x[i]])
        self.deck = [self.deck[i] for i in range(len(self.deck)) if i not in x]
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
    def random_deal(self,d:Deck):
        num=random.sample(range(0,len(d.deck)),13)
        cards = d.put_cards(num)
        for i in range(len(cards)):
            self.hand.append(cards[i])
            self.number_of_cards+=1
            self.number_of_points+=cards[i].points()
    def random_deal(self,d:Deck, n_of_cards:int):
        num=random.sample(range(0,len(d.deck)),n_of_cards)
        cards = d.put_cards(num)
        for i in range(len(cards)):
            self.hand.append(cards[i])
            self.number_of_cards+=1
            self.number_of_points+=cards[i].points()
    # def random_deal(self,cards:List, n_of_cards:int):
    #     num=random.sample(range(0,len(cards)),n_of_cards)
    #     cards = d.put_cards(num)
    #     for i in range(len(cards)):
    #         self.hand.append(cards[i])
    #         self.number_of_cards+=1
    #         self.number_of_points+=cards[i].points()
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
        while(pom==0):
            deck_copy = copy.copy(deck)
            sample_hand = Hand()
            sample_hand.random_deal(deck_copy,13)
            if((sample_hand.number_of_points>=min) and (sample_hand.number_of_points<=max)): pom=1
        deck.remove_distinct_cards(sample_hand.hand)
        cards = sample_hand.hand
        for i in range(len(cards)):
            self.hand.append(cards[i])
            self.number_of_cards+=1
            self.number_of_points+=cards[i].points()

    # def points_deal2(self,min:int,max:int):
    #     deck = Deck()

    #     if(min<0 or max>37 or min>max):
    #         print('pojebalo cie')
    #         return 0

    #     #prepare an array of indexes to exclude from later on
    #     availableIndexes=[]
    #     for i in range(52):
    #         availableIndexes.append(i)

    #     while(self.number_of_cards<13):
    #         #choose a random card
    #         randomIndex=random.choice(availableIndexes)
    #         card=deck.deck[randomIndex]
    #         points=card.points()
    #         if(self.number_of_points + points <= max): #if not too much points after adding a new card then add
    #             self.hand.append(card)
    #             self.number_of_points += points
    #             self.number_of_cards += 1
    #         availableIndexes.remove(randomIndex)

    #     while(self.number_of_points < min): #if not enough points keep drawing until you draw enough
    #         randomIndex = random.choice(availableIndexes)
    #         card = deck.deck[randomIndex]
    #         points = card.points()
    #         if(self.number_of_points + points <= max):
    #             self.hand.append(card)
    #             self.number_of_points += points
    #             self.number_of_cards += 1
    #         availableIndexes.remove(randomIndex)

        
    #     while(self.number_of_cards>13):
    #         pointsToDelete=0
    #         if[self.hand[i].points()==pointsToDelete]:
    #             self.number_of_cards -= 1
    #             self.number_of_points -= self.hand[i].points()
    #             self.hand.remove(self.hand[i])
    #             i=0
    #         if[i==12]:
    #             i = 0
    #             pointsToDelete+=1
    #         i+=1
    def direct_deal(self, deck, clubs, diamonds, hearts, spades): #using particular number for each color, if doesnt matter then -1
        
        self.clubs=clubs
        self.diamonds=diamonds
        self.hearts=hearts
        self.spades=spades
        array=[clubs,diamonds,hearts,spades]
        num_of_color = 0
        rest_of_cards=[]
        for i in range(4):
            deck_copy = copy.copy(deck)
            cards_in_colour = []
            for j in range (len(deck_copy.deck)):
                if deck_copy.deck[j].colour_to_number()==i:
                    cards_in_colour.append(deck_copy.deck[j]) #cards in particular colour possible to get from the deck
                deck_particular = Deck(cards_in_colour)    
            if array[i]>0:
                sample_hand = Hand()
                sample_hand.random_deal(deck_particular,array[i])   
                cards = sample_hand.hand
                for k in range(len(cards)):
                    self.hand.append(cards[k])
                    cards_in_colour.remove(cards[k])
                    self.number_of_cards+=1
                    self.number_of_points+=cards[k].points()   
            else:
                for k in range(len(cards_in_colour)):
                    rest_of_cards.append(cards_in_colour[k])
                    
        l = len(self.hand)
        num =random.sample(range(0,len(rest_of_cards)),13- l )
        for i in range (13-l):
            self.hand.append(rest_of_cards[num[i]])
            self.number_of_cards+=1
            self.number_of_points+=rest_of_cards[num[i]].points()
        deck.remove_distinct_cards(self.hand)    
                
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

            
        
    






