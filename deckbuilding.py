#1 card preparations
suits    = ['S', 'H', 'D', 'C']
order    = ['A','2','3','4','5','6','7',
            '8','9','10','J','Q','K']
fulldeck = ['%s%s'%(suit,index) for suit in suits
            for index in order]
restdeck = fulldeck


#2 money preparations (under construction)
#2 should make the input integer.
rdymoney = input('Hom much money do you prepare to start? ')
print('')
print('you\'re in with %s Won.' %rdymoney)


# ============================================================
# print(len(fulldeck))
# use this printing to check if 52 cards are in the full deck.
# fulldeck2 = ['%s%s'%(suit,index) for index in order
#            for suit in suits]
# using this makes the order of full deck
# different from fulldeck.
# ============================================================


#3 distributing cards for the game
import random as r
def dealing():
    a = r.randint(0,len(fulldeck))
    b = fulldeck[a]
    del fulldeck[a]
    return b

print('')
print('game start.')
p1 = dealing()
d1 = dealing()
p2 = dealing()
d2 = dealing()
pdealed = [p1, p2]
ddealed = [d1, d2]
ddealed_to_player = [d1, '?']


#4 card scoring
def scoring(a):
    if   a[1] == 'A':
        return 11
    elif a[1] in ['J', 'Q', 'K']:
        return 10
    else :
        return int(a[1:])


#5 calculating total score
def total(a):
    s = 0
    for x in a:
        s += scoring(x)
    return s


#6 request for betting
#6 (constructing, should make the input integer.)
#6 (construction needed: the betting money cannot be more than the ready money.)
bet = input('How much money would you bet? ')
print('You bet %s won.' %bet)
print('')


#7 printing the initial deal
turn = 0
def cardreveal(a):
    a = a + 1
    if a = 1:
        print(str(pdealed) + ", player's current score is",
          total(pdealed))
        print(str(ddealed_to_player) + ", dealer's announced score is",
          total(ddealed))
        print('')
    else    :
        print(str(pdealed) + ", player's current score is",
          total(pdealed))
        print(str(ddealed) + ", dealer's announced score is",
          total(ddealed))
        print('')
    return a

cardreveal(turn)


#8 a function to request player's following action
def action():
    print('Choose an action by typing the given number.')
    print('1. Hit')
    print('2. Stand')
    print('3. Double Down')
    if scoring(p1) == scoring(p2):
        print('4. Split')
    a = input()
    print('')
    if   a == '1':
        print('Player choosed to hit.')
        hit()
    elif a == '2':
        print('Player choosed to stand.')
        stand()
    elif a == '3':
        print('Player choosed to double down.')
        doubledown()
    elif a == '4':
        if scoring(p1) == scoring(p2):
            print('Player choosed to split.')
            split()
        else:
            print('invalid choice. Please try again.')
    else:
        print('invalid choice. Please try again.')


# 9, 10, 11, 12 card is dealt to dealer and player each.
class dealing:
    def hit(self):
        pdealed.append(dealing())
        cardreveal(turn)
        if   total(pdealed) > 21:
            print('Burst! Player lost this game.')
        elif total(pdealed) == 21:
            print('BlackJack! Player won this game.')
        else :
            action()
    def stand(self)
    
player = dealing()
dealer = dealing()




#9 designing game step after Hitting(incorporated into 8.5)
# def hit():
#     pdealed.append(dealing())
#     cardreveal(turn)
#     if   total(pdealed) > 21:
#         print('Burst! Player lost this game.')
#     elif total(pdealed) == 21:
#         print('BlackJack! Player won this game.')
#     else :
#         action()

action()


#10 designing game step after Standing(constructing)
# def stand():
#     dealer starts cardhitting...


#11 designing game step after Doubling Down(constructing)
# def doubledown():
#     pdealed.append(dealing())
#     판돈 거는걸 반영해야함!
    

#12 designing game step after Splitting(constructing)
# def split():

action()


