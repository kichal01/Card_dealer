from Board import Deck,Card,Hand,Board
import random
from ddstable import ddstable


PBN = b"E:QJT5432.T.6.QJ82 .J97543.K7532.94 87.A62.QJT4.AT75 AK96.KQ8.A98.K63"
all = ddstable.get_ddstable(PBN)
print("{:>5} {:>5} {:>5} {:>5} {:>5} {:>5}".format("", "S", "H", "D", "C", "NT"))
# may use  card_suit=["C", "D", "H", "S", "NT"]
for each in all.keys():
    print("{:>5}".format(each),end='')
    for suit in ddstable.dcardSuit:
        trick=all[each][suit]
        if trick>7:
            print(" {:5}".format(trick - 6),end='')
        else:
            print(" {:>5}".format("-"),end='')
    print("")
print(PBN)

deck=Deck()
N= Hand()
E= Hand()
S= Hand()
W= Hand()
for i in range(10):
    board1=Board(N,E,S,W,i+1,'N')
    board1.deal(deck,
                {'min_points':6,'max_points':8,'spades':7},#N
                {'min_points': 13,'max_points' :17,'min_clubs': 2, 'min_diamonds' : 2, 'min_hearts' : 2, 'max_spades' :1 },#E
                {'min_points': 6,'max_points' :8,'min_spades':2},#S
                {'min_points': 0}   #W     
                )
    board1.show()

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

