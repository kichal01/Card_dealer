from klasa1 import Deck,Card,Hand,Board
import random
deck=Deck()
N= Hand()
E= Hand()
S= Hand()
W= Hand()

board1=Board(N,E,S,W,1)
N.points_deal2(10,10)

# board1.random_deal(deck)
print('N: ')
N.show()
print('Liczba punktow: ' + str(N.number_of_points))
print('Liczba kart: ' + str(N.number_of_cards))
# print('Talia: ')
# deck.show()

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

