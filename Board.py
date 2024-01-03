from Hand import Hand,Deck,Card
import copy, datetime

                
class Board:
    def __init__ (self,N:Hand,E:Hand,S:Hand,W:Hand,n:int,dealer):
        self.N=N
        self.E=E
        self.S=S
        self.W=W
        self.number = n
        self.dealer=dealer
    def random_deal(self,deck:Deck):
        self.N.random_deal(deck)
        self.E.random_deal(deck)
        self.S.random_deal(deck)
        self.W.random_deal(deck)
    def show (self):
        print('Nr boarda: '+str(self.number))
        print('N: ')
        self.N.show()
        print('E: ')
        self.E.show()
        print('S: ')
        self.S.show()
        print('W: ')
        self.W.show()
        print('')
    def to_pbn(self):
        pass
    def deal(self,deck:Deck,N,E,S,W): 



        #Run the loop till current time exceeds end time
        i=0
        while i <10000:

            i+=1
            copy_deck = copy.deepcopy(deck)
            copy_N = copy.deepcopy(self.N)
            copy_E = copy.deepcopy(self.E)
            copy_S = copy.deepcopy(self.S)
            copy_W = copy.deepcopy(self.W)
        
            a = copy_N.many_conditions_deal(copy_deck,**N)

            b = copy_E.many_conditions_deal(copy_deck,**E)

            c = copy_S.many_conditions_deal(copy_deck,**S)

            d = copy_W.many_conditions_deal(copy_deck,**W)

            if( a==0 or b==0 or c==0 or d==0):
                print(i)
                continue
            else:                
                self.N = copy_N
                self.E = copy_E
                self.W = copy_W
                self.S = copy_S
                i=10
                break
                


            
        
    






