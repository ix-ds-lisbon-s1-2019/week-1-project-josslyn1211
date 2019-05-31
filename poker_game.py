#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 29 23:40:52 2019

@author: josslyngao
"""

 
names = []
cards = {2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, "J": 11,
                "Q": 12,
                "K": 13,
                "A": 14}

print(sorted(cards.values()))

cards_of_players = []

number_of_players = int(input("Please enter the number of players:\n"))

for player in range(number_of_players):
    temp_name = input("Please enter player name：\n")
    names.append(temp_name)
dict_list = []   
for player in range(number_of_players):
    import random
    cards_of_players = random.choices(cards, k=5)
    print(cards_of_players)
    for name in names:
        dict_list[name] = cards_of_players
    print(dict_list)
    for name, hand in dict_list.items():
        for i in hand:
            i = cards[i]
        dict_list[name] = hand.sort(reverse=True)


        
  
            

    
    



    

