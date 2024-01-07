from Deck import Deck, Card
import random
import copy

class Hand:
    def __init__ (self,name = None):
        self.hand = []
        self.number_of_cards=0
        self.number_of_points=0 
        if (name=='N' or name =='E' or name =='S' or name =='W'):
            self.name = name
    def particular_cards(self, cards, deck:Deck):
        for i in range(len(cards)):
            self.hand.append(cards[i])
            self.number_of_cards+=1
            self.number_of_points+=cards[i].points()
        deck.remove_distinct_cards(cards)
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
    def is_full(self):
        if self.number_of_cards == 13:
            return 1
        else: return 0
    def spades(self):
        spades=[]
        for i in range(len(self.hand)):
            if self.hand[i].colour == 'pik': spades.append(self.hand[i])
        spades = sorted(spades, key=lambda x: x.counter*(-1))
        return spades
    def hearts(self):
        hearts=[]
        for i in range(len(self.hand)):
            if self.hand[i].colour == 'kier': hearts.append(self.hand[i])
        hearts = sorted(hearts, key=lambda x: x.counter*(-1))    
        return hearts
    def clubs(self):
        clubs=[]
        for i in range(len(self.hand)):
            if self.hand[i].colour == 'trefl': clubs.append(self.hand[i])
        clubs = sorted(clubs, key=lambda x: x.counter*(-1))
        return clubs
    def diamonds(self):
        diamonds=[]
        for i in range(len(self.hand)):
            if self.hand[i].colour == 'karo': diamonds.append(self.hand[i])
        diamonds = sorted(diamonds, key=lambda x: x.counter*(-1)) 
        return diamonds
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
    def check_conditions(self,key,value):
        if (key =='min_points'):
            if(self.number_of_points >= value): return 1
            else: return 0 
        elif(key =='max_points'):
            if(self.number_of_points<= value): return 1
            else: return 0 
        elif (key == 'min_clubs'):
            trefle = 0
            for i in range (len(self.hand)):
                if (self.hand[i].colour == 'trefl'):
                    trefle+=1
            if (trefle >= value): return 1 
            else: return 0
        elif (key == 'max_clubs'):
            trefle = 0
            for i in range (len(self.hand)):
                if (self.hand[i].colour == 'trefl'):
                    trefle+=1
            if (trefle <= value): return 1 
            else: return 0            
        elif (key == 'clubs'):
            trefle = 0
            for i in range (len(self.hand)):
                if (self.hand[i].colour == 'trefl'):
                    trefle+=1
            if (trefle == value): return 1 
            else: return 0
        elif (key == 'min_diamonds'):
            kara = 0
            for i in range (len(self.hand)):
                if (self.hand[i].colour == 'karo'):
                    kara+=1
            if (kara >= value): return 1 
            else: return 0
        elif (key == 'max_diamonds'):
            kara = 0
            for i in range (len(self.hand)):
                if (self.hand[i].colour == 'karo'):
                    kara+=1
            if (kara <= value): return 1 
            else: return 0            
        elif (key == 'diamonds'):
            kara = 0
            for i in range( len(self.hand)):
                if (self.hand[i].colour == 'karo'):
                    kara+=1
            if (kara == value): return 1 
            else: return 0 

        elif (key == 'min_hearts'):
            kiery = 0
            for i in range (len(self.hand)):
                if (self.hand[i].colour == 'kier'):
                    kiery+=1
            if (kiery >= value): return 1 
            else: return 0
        elif (key == 'max_hearts'):
            kiery = 0
            for i in range (len(self.hand)):
                if (self.hand[i].colour == 'kier'):
                    kiery+=1
            if (kiery <= value): return 1 
            else: return 0            
        elif (key == 'hearts'):
            kiery = 0
            for i in range (len(self.hand)):
                if (self.hand[i].colour == 'kier'):
                    kiery+=1
            if (kiery == value): return 1 
            else: return 0     

        elif (key == 'min_spades'):
            piki = 0
            for i in range (len(self.hand)):
                if (self.hand[i].colour == 'pik'):
                    piki+=1
            if (piki >= value): return 1 
            else: return 0
        elif (key == 'max_spades'):
            piki = 0
            for i in range (len(self.hand)):
                if (self.hand[i].colour == 'pik'):
                    piki+=1
            if (piki <= value): return 1 
            else: return 0            
        elif (key == 'spades'):
            piki = 0
            for i in range(len(self.hand)):
                if (self.hand[i].colour == 'pik'):
                    piki+=1
            if (piki == value): return 1 
            else: return 0     

            
    def many_conditions_deal(self, deck, **kwargs):
        #points
        #cards_in_color (min/max cards in color)
        i=0
        check_box=0
        while check_box==0:
            d=copy.copy(deck)
            sample_hand = Hand()
            i+=1
            if(i>1000):
                return 0
            sample_hand.random_deal(d,13)
            for key, value in kwargs.items():
                result = sample_hand.check_conditions(key,value);
                if result==0:
                    check_box = 0
                    break
                else: 
                    check_box = 1
        deck.remove_distinct_cards(sample_hand.hand)
        cards = sample_hand.hand
        for i in range(len(cards)):
            self.hand.append(cards[i])
            self.number_of_cards+=1
            self.number_of_points+=cards[i].points()
    
    
                
                
            
        