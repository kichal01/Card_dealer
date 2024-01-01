from Hand import Hand,Deck,Card
        

                
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
    def point_deal(self,**hands): #in hands i want sth like 'E-':10, 'E+':14 meaning E hand is supposed to have min 10 points and max 14 points
        pass

            
        
    






