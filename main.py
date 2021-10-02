#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 12:29:24 2021

@author: kakao
"""

from __init__ import *

if __name__ == '__main__':

    rdymoney = input('Hom much money do you prepare to start? ')
    print('')
    print('you\'re in with %s Won.' %rdymoney)    

    print('')
    print('game start.')

    admin = Admin()
    player = Player()
    dealer = Dealer()
    for person in [player, dealer]:
        admin.add_two_cards(person)

    bet = input('How much money would you bet? ')
    print('You bet %s won.' %bet)
    print('')
    
    admin.reveal_all(player, dealer)
    
    # action은 player만 하는 줄 알고 구현했네. 직접 고쳐보면 좋을듯
    
    admin.action(player, dealer)