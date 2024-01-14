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

cards3 =[Card(14,1),Card(13,1),Card(3,1),Card(9,1),Card(11,2),Card(9,2),Card(6,2),Card(8,2),Card(2,2),Card(11,3),Card(8,3),Card(4,3),Card(2,3)]

N= Hand("N")
E= Hand("E")
S= Hand("S")
W= Hand("W")
E.particular_cards(cards3,deck)

results_E = {'NT':{'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0},
    'S':{'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0},
    'H':{'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0},
    'D':{'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0},
    'C':{'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0}}

results_W = {'NT':{'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0},
    'S':{'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0},
    'H':{'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0},
    'D':{'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0},
    'C':{'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0}}

points = {
"0":0,
"1":0,
"2":0,
"3":0,
"4":0,
"5":0,
"6":0,
"7":0,
"8":0,
"9":0,
"10":0,
"11":0,
"12":0,
"13":0,
"14":0,
"15":0,
"16":0,
"17":0,
"18":0,
"19":0,
"20":0,
"21":0,
"22":0,
"23":0,
"24":0,
"25":0,
"26":0,
"27":0,
"28":0,
"29":0,
"30":0,
"31":0,
"32":0,
"33":0,
"34":0,
"35":0,
"36":0,
"37":0
}

for i in range(10000):
    print(i)
    board1=Board(N,E,S,W,i+1,'N')
    board1.deal(deck,
                # {'max_points': 11,'max_spades':5,'max_hearts':5,'max_diamonds':5, 'max_clubs':5},#N
                # {'max_points': 0},#E
                # {'max_points': 10,'min_points':6,'major':6,'max_diamonds' : 4,'max_clubs' : 4},#S
                # {'max_points': 16,'min_points':11,'min_spades' :5, 'max_spades':7}#W,
                {'min_points': 0},
                {'min_points': 0},
                {'min_points': 0},
                {'min_points': 0}

                )
    #board1.show()
    pkt = board1.N.number_of_points
    points[str(pkt)] += 1
print(points)

     

#     pbn = board1.to_pbn()
#     ile = board1.double_dummy(pbn)
#     board1.stats(ile,results_W,'W')
#     board1.stats(ile, results_E,'E')
# print('W:')
# print('NT: '+str(results_W.get('NT')))
# print('piki: '+str(results_W.get('S')))
# print('kiery: '+ str(results_W.get('H')))
# print('kara: ' + str(results_W.get('D')))
# print('trefle' + str (results_W.get('C')))
# print(' ')
# print('E:')
# print('NT: '+str(results_E.get('NT')))
# print('piki: '+str(results_E.get('S')))
# print('kiery: '+ str(results_E.get('H')))
# print('kara: ' + str(results_E.get('D')))
# print('trefle' + str (results_E.get('C')))
# print(' ')


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

