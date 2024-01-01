from Board import Deck,Card,Hand,Board
import random
deck=Deck()
N= Hand()
E= Hand()
S= Hand()
W= Hand()

board1=Board(N,E,S,W,1)
board1.deal(deck,
            {'min_points':4,'max_points':8,'spades':7},#N
            {'min_points': 13,'max_points' :17,'min_clubs': 2, 'min_diamonds' : 2, 'min_hearts' : 2, 'max_spades' :1 },#E
            {'min_points': 6,'max_points' :10,'min_spades':2},#S
            {'min_points': 0}   #W     
            )

cond = {'min_points': 15,
        'max_points' :17}

#N.points_deal(0,3,deck)
# N.many_conditions_deal(deck, **cond)
# S.many_conditions_deal(deck, min_points=8, max_points = 9,min_clubs = 2, min_diamonds = 2, min_hearts = 2, min_spades = 2)
# E.many_conditions_deal(deck, max_points = 9)
# W.many_conditions_deal(deck, max_points = 9)


print('N: ')
board1.N.show()
print('Liczba punktow: ' + str(board1.N.number_of_points))
print('Liczba kart: ' + str(board1.N.number_of_cards))   

print('E: ')
board1.E.show()
print('Liczba punktow: ' + str(board1.E.number_of_points))
print('Liczba kart: ' + str(board1.E.number_of_cards))   


print('S: ')
board1.S.show()
print('Liczba punktow: ' + str(board1.S.number_of_points))
print('Liczba kart: ' + str(board1.S.number_of_cards))   

print('W: ')
board1.W.show()
print('Liczba punktow: ' + str(board1.W.number_of_points))
print('Liczba kart: ' + str(board1.W.number_of_cards))  

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

