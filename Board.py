from re import I
from Hand import Hand,Deck,Card
import copy, datetime
from ddstable import ddstable


                
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
        order = [self.N,self.E,self.S,self.W]
        for i in range(4):
            if order[0].name ==self.dealer: break
            else: 
                var = order[0]
                order.remove(var)
                order.append(var)
            
        pbn = str()
        pbn = pbn+self.dealer+':'
        for i in range (4):
            spades = order[i].spades()
            for j in range (len(spades)):
                pbn = pbn+str(spades[j].number)
            pbn = pbn +'.'
            hearts = order[i].hearts()
            for j in range (len(hearts)):
                pbn = pbn+str(hearts[j].number)
            pbn = pbn +'.'                
            diamonds = order[i].diamonds()
            for j in range (len(diamonds)):
                pbn = pbn+str(diamonds[j].number)
            pbn = pbn +'.' 
            clubs = order[i].clubs()
            for j in range (len(clubs)):
                pbn = pbn+str(clubs[j].number)
            pbn = pbn +' ' 
        pbn = pbn[:-1]
        return pbn

    def double_dummy(self,pbn):
        PBN = pbn.encode('utf-8')
        all = ddstable.get_ddstable(PBN)
        # print("{:>5} {:>5} {:>5} {:>5} {:>5} {:>5}".format("", "S", "H", "D", "C", "NT"))
        # # may use  card_suit=["C", "D", "H", "S", "NT"]
        # for each in all.keys():
        #     print("{:>5}".format(each),end='')
        #     for suit in ddstable.dcardSuit:
        #         trick=all[each][suit]
        #         if trick>7:
        #             print(" {:5}".format(trick - 6),end='')
        #         else:
        #             print(" {:>5}".format("-"),end='')
        #     print("")
        return all.get('W').get('S')-6 # ten fragment liczy tylko grê w piki gracza W, do poprawy
            
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
            
            if (copy_N.is_full()==0):
                a = copy_N.many_conditions_deal(copy_deck,**N)
            else:
                a = 1
            if (copy_E.is_full()==0):
                b = copy_E.many_conditions_deal(copy_deck,**E)
            else: b = 1
            if (copy_S.is_full()==0):
                c = copy_S.many_conditions_deal(copy_deck,**S)
            else: c = 1
            if (copy_W.is_full() ==0):
                d = copy_W.many_conditions_deal(copy_deck,**W)
            else: d = 1
            
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
                


            
        
    






