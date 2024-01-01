from Card import Card

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
        