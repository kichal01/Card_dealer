from Board import Deck,Card,Hand,Board
import random
deck=Deck()
N= Hand()
E= Hand()
S= Hand()
W= Hand()

board1=Board(N,E,S,W,1)
#N.points_deal(0,3,deck)
N.many_conditions_deal(deck, min_points=15, max_points = 17,max_clubs = 2, max_diamonds = 2, min_hearts = 2, min_spades = 2)
S.many_conditions_deal(deck, min_points=8, max_points = 9,min_clubs = 2, min_diamonds = 2, min_hearts = 2, min_spades = 2)
E.many_conditions_deal(deck, max_points = 9)
W.many_conditions_deal(deck, max_points = 9)


print('N: ')
N.show()
print('Liczba punktow: ' + str(N.number_of_points))
print('Liczba kart: ' + str(N.number_of_cards))   

print('E: ')
E.show()
print('Liczba punktow: ' + str(E.number_of_points))
print('Liczba kart: ' + str(E.number_of_cards))   


print('S: ')
S.show()
print('Liczba punktow: ' + str(S.number_of_points))
print('Liczba kart: ' + str(S.number_of_cards))   

print('W: ')
W.show()
print('Liczba punktow: ' + str(W.number_of_points))
print('Liczba kart: ' + str(W.number_of_cards))  
deck.show()
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

