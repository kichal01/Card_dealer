from Board import Deck,Card,Hand,Board
import random
from ddstable import ddstable


# PBN = b"N:KQ862.T754.Q.QT5 T9.AJ9.9532.K982 A7543.Q83.AKJ87. J.K62.T64.AJ7643"
# all = ddstable.get_ddstable(PBN)
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
# print(PBN)

Spades_winners = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0}

deck=Deck()
cards = [Card(14,2),Card(13,2),Card(11,2),Card(8,2),Card(7,2),Card(12,3),Card(8,3),Card(3,3),Card(14,4),Card(7,4),Card(5,4),Card(4,4),Card(3,4)]
cards2 = [Card(12,1),Card(10,1),Card(4,1),Card(11,2),Card(6,2),Card(2,2),Card(6,3),Card(5,3),Card(2,3),Card(14,4),Card(12,4),Card(11,4),Card(8,4)]
N= Hand("N")
E= Hand("E")
S= Hand("S")
W= Hand("W")
W.particular_cards(cards2,deck)

for i in range(1000):
    print(i)
    board1=Board(N,E,S,W,i+1,'N')
    board1.deal(deck,
                {'max_points': 12,'max_spades' : 5,'max_hearts' : 5,'max_diamonds' : 5,'max_clubs' : 5},#N,
                {'max_points': 14,'min_points':11, 'diamonds':5,'spades' : 4},#E
                {'max_points': 12,'max_spades' : 5,'max_hearts' : 5,'max_diamonds' : 5,'max_clubs' : 5},
                {'max_points': 0}#W
                
             
                )
    #board1.show()
    pbn = board1.to_pbn()
    ile = board1.double_dummy(pbn)
    if(ile>0):
        Spades_winners[str(ile)]= Spades_winners[str(ile)] + 1
print(Spades_winners)
#N.points_deal(0,3,deck)
# N.many_conditions_deal(deck, **cond)
# S.many_conditions_deal(deck, min_points=8, max_points = 9,min_clubs = 2, min_diamonds = 2, min_hearts = 2, min_spades = 2)
# E.many_conditions_deal(deck, max_points = 9)
# W.many_conditions_deal(deck, max_points = 9)


# print('N: ')
# board1.N.show()
# print('Liczba punktow: ' + str(board1.N.number_of_points))
# print('Liczba kart: ' + str(board1.N.number_of_cards))   

# print('E: ')
# board1.E.show()
# print('Liczba punktow: ' + str(board1.E.number_of_points))
# print('Liczba kart: ' + str(board1.E.number_of_cards))   


# print('S: ')
# board1.S.show()
# print('Liczba punktow: ' + str(board1.S.number_of_points))
# print('Liczba kart: ' + str(board1.S.number_of_cards))   

# print('W: ')
# board1.W.show()
# print('Liczba punktow: ' + str(board1.W.number_of_points))
# print('Liczba kart: ' + str(board1.W.number_of_cards))  

# print('E: ')
# E.show()
# print('Liczba punktow: ' + str(E.number_of_points))
# print('Liczba kart: ' + str(E.number_of_cards))   
# print('S: ')
# S.show()
# print('Liczba punktow: ' + str(S.number_of_points))
# print('Liczba kart: ' + str(S.number_of_cards))   
# print('W: ')
# W.show()
# print('Liczba punktow: ' + str(W.number_of_points))
# print('Liczba kart: ' + str(W.number_of_cards))   

# print('Pozostale honory: ')
# for i in range(len(deck.honors)):
#     print(str(deck.honors[i].colour)+str(deck.honors[i].number)+ ' ')

