from random import shuffle

# defining the card ranks, and suits
ranks = [_ for _ in range (2, 11)] + ['JACK', 'QUEEN', 'KING', 'ACE']
suits = ['SPADE', 'HEART', 'DIAMOND', 'CLUB']

def get_deck():
        ""Return a new deck of cards.""

        return [[rank, suit] for rank in ranks for suit in suits

# get a deck of cards, and randomly shuffle it
deck = get_deck()
shuffle(deck)

# boolean variable that indicates whether player has gone bust yet
player_in = True

# issue the player and dealer their first two cards
player_hand = [deck.pop(), deck.pop()]
dealer_hand = [deck.pop(), deck.pop()]

def card_value(card):
    ""Returns the integer value of a single card.""
rank = card[0]
if rank in ranks [0:-4]
    return int(rank)
    elif rank is 'ACE':
        return 11
            else:
                return 10

def hand_value(hand):
    ""Returns the integer value of a set of cards.""

# Naivly sum up the cards in the deck.
tmp_value = sum(card_value(_) for_in hand)
# Count the number of Aces in the hand.
num_aces=len([_for_in hand if _[0] is 'ACE'])
#Aces can count for 1, or 11. If it is possible to bring the value of the hand under 21 by making
#11 -> 1 substitutions, do so.
while num_aces > 0:
    if tmp_value > 21 and 'ACE' in ranks:
        tmp_value -=10
        num_aces -=1
        else:
            break
            #Return a string and an integer representing the value of the hand if the hand is bust return 100.
            if tmp_value < 21:
                return [str(tmp_value), tmp_value]
                elif tmp_value == 21:
                    return ['Blackjack!', 21]
                    else:
                        return['Bust!', 100]

while player_in:
    # Display the player's current hand, as well as its value.
    current_score_str ="'\nYou are currently at %s\nwith the hand%s\n'"
        print current_score_str % (hand_value(player_hand)[0], player_hand)
        #If the player's hand is bust, don't ask them for a decision.
        if hand_value(player_hand)[1] == 100:
            break
            if player_in:
                response = int(raw_input('Hit or Stay?(Hit =1, Stay = 0)'))
                # If the player asks to be hit, take the first card frin the top of deck and add it to their hand.
                # If they ask to stay, change player_in to false, and move on to the dealer's hand.
            if response:
                player_in = True
                new_player_card = deck.pop()
                player_hand.append(new_player_card)
                print 'You draw %s' %new_player_card
                else:
                    player_in = False

        player_score_label, player_score=
        hand_value(player_hand)
        dealer_score_label, dealer_score=
        hand_value(dealer_hand)

            if player_score <= 21:
                dealer_hand_string="'\nDealer is at %s\nwith the hand %s\n'"
                    print dealer_hand_string%(dealer_score_label, dealer_hand)
                    else:
                        print "Dealer wins."
            
            dealer_score_label, dealer_score=
            hand_value(dealer_hand)

            if player_score < 100 and dealer_score == 100:
                print 'You beat the dealer!'
                elif player_score > dealer_score:
                    print 'You beat the dealer!'
                elif player_score == dealer_score:
                    print 'You tied with the delaer, nobody wins'
                elif player_score < dealer_score:
                    print "Dealer wins!"