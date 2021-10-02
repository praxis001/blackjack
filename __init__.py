#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 12:29:15 2021

@author: kakao
"""
import random as r


class Player:
    def __init__(self):
        self.cards = []

    def card_reveal(self, turn:int) -> list:
        return self.cards

    def ret_card(self, idx:int) -> str:
        return self.cards[idx]

    def is_poss_split(self) -> bool:
        return self.cards[0] == self.cards[1]
        
    
class Dealer(Player):
    def card_reveal(self, turn:int) -> list:
        if turn == 0:
            return self.cards[:1]
        elif turn == 1:
            return self.cards


class Admin:

    def __init__(self):
        """
        객체 생성자. admin = admin()과 같은 코드로 객체를 생성할때 실행되는 함수.
        admin 객체에게 deck을 만들어준다
        """
        ## th
        ## 여분의 deck을 만들고 싶다고 해석
        ## restdeck = fulldeck으로 구현하면, 새로운 덱이 만들어지지 않고 restdeck이 fulldeck을 참조하기만 함.
        ## 즉, fulldeck에서 카드가 빠지면 restdeck도 같은 deck을 참조하기에 카드가 빠짐.
        ## [:]을 사용하면 새로운 list를 할당 가능
        self.suits    = ['S', 'H', 'D', 'C']
        self.orders    = ['A','2','3','4','5','6','7',
                    '8','9','10','J','Q','K']
        self.restdeck = ['%s%s'%(suit,index) for suit in self.suits for index in self.orders]
        self.fulldeck = self.restdeck[:]
        self.turn = 0

    def ret_new_card(self) -> str:
        """
        ret_new_card : return card. 새로 카드 한장을 반환함

        Returns
        -------
        b : string (ex. 'S1')
            player, dealer에게 주는 새로운 카드
        """
        new_card_idx = r.randint(0,len(self.fulldeck))
        new_card = self.fulldeck[new_card_idx]
        del self.fulldeck[new_card_idx]
        return new_card

    def add_two_cards(self, person):
        for i in range(2):
            person.cards.append(self.ret_new_card())
    
    def ret_card_score(self, card):
        if   card[1] == 'A':
            return 11
        elif card[1] in ['J', 'Q', 'K']:
            return 10
        else :
            return int(card[1:])


    def ret_total_score(self, person) -> int:
        """
        person으로 주어진 player, 혹은 dealer의 점수를 
        현재 turn에 맞춰서 반환한다

        Parameters
        ----------
        person : Player or Dealer
            player 혹은 dealer

        Returns
        -------
        total_score : int
            player 혹은 dealer의 현재 오픈하는 점수

        """
        total_score = 0
        for card in person.card_reveal(self.turn):
            total_score += self.ret_card_score(card)
        return total_score

    def reveal_all(self, player, dealer):
        for person, person_str in zip([player, dealer], ['player', 'dealer']):
            print(str(person.card_reveal(self.turn)) + ", " + person_str +"'s current score is",
              self.ret_total_score(person))                    
        self.turn += 1
        
    def action(self, player, dealer):
        print('Choose an action by typing the given number.')
        print('1. Hit')
        print('2. Stand')
        print('3. Double Down')
        if player.is_poss_split():
            print('4. Split')
        player_action = input()
        print('')
        if   player_action == '1':
            print('Player choosed to hit.')
            self.hit(player)
        elif player_action == '2':
            print('Player choosed to stand.')
            self.stand()
        elif player_action == '3':
            print('Player choosed to double down.')
            self.doubledown()
        elif player_action == '4':
            if player.is_poss_split():
                print('Player choosed to split.')
                self.split()
            else:
                print('invalid choice. Please try again.')
        else:
            print('invalid choice. Please try again.')

    def hit(self, player, dealer):
        player.cards.append(self.ret_new_card())
        self.reveal_all(player, dealer)
        if   self.ret_total_score(player) > 21:
            print('Burst! Player lost this game.')
        if   self.ret_total_score(player) == 21:
            print('BlackJack! Player won this game.')
        else :
            self.action()
    
    def stand(self):
        return NotImplemented
    
    def doubledown():
        return NotImplemented

    def split():
        return NotImplemented
       