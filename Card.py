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
        