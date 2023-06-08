import random

print("\n\n\n\t\t\t\t\tBlackjack\n\n\ ")
print("""Rules:\n
Try to get as close to 21 without going over.
Kings, Queens, and Jacks are worth 10 points.
Aces are worth 1 or 11 points.
Cards 2 through 10 are worth their face value.
(H)it to take another card.
(S)tand to stop taking cards.
On your first play, you can (D)ouble down to increase your bet but must hit exactly one more time before standing.
In case of a tie, the bet is returned to the palyer.
The dealer stops at hitting at 17
      """)




class Card(object):

    card_values = {
        'Ace': 11,  # value of the ace is high until it needs to be low
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        'Jack': 10,
        'Queen': 10,
        'King': 10
    }

    def __init__(self, suit, rank):
        """
        :param suit: The face of the card, e.g. Spade or Diamond
        :param rank: The value of the card, e.g 3 or King
        """
        self.suit = suit.capitalize()
        self.rank = rank
        self.points = self.card_values[rank]

def ascii_version_of_card(cards:list, return_string=True):
    """
    :param cards: One or more card objects
    :param return_string: By default we return the string version of the card, but the dealer hide the 1st card and we
    keep it as a list so that the dealer can add a hidden card in front of the list
    """
    # we will use this to prints the appropriate icons for each card
    suits_name = ['Spades', 'Diamonds', 'Hearts', 'Clubs']
    suits_symbols = ['♠', '♦', '♥', '♣']

    # create an empty list of list, each sublist is a line
    lines = [[] for i in range(9)]

    for index, card in enumerate(cards):
        # "King" should be "K" and "10" should still be "10"
        if card.rank == '10':  # ten is the only one who's rank is 2 char long
            rank = card.rank
            space = ''  # if we write "10" on the card that line will be 1 char to long
        else:
            rank = card.rank[0]  # some have a rank of 'King' this changes that to a simple 'K' ("King" doesn't fit)
            space = ' '  # no "10", we use a blank space to will the void
        # get the cards suit in two steps
        suit = suits_name.index(card.suit)
        suit = suits_symbols[suit]

        # add the individual card on a line by line basis
        lines[0].append('┌─────────┐')
        lines[1].append('│{}{}       │'.format(rank, space))  # use two {} one for char, one for space or char
        lines[2].append('│         │')
        lines[3].append('│         │')
        lines[4].append('│    {}    │'.format(suit))
        lines[5].append('│         │')
        lines[6].append('│         │')
        lines[7].append('│       {}{}│'.format(space, rank))
        lines[8].append('└─────────┘')

    result = []
    for index, line in enumerate(lines):
        result.append(''.join(lines[index]))

    # hidden cards do not use string
    if return_string:
        return '\n'.join(result)
    else:
        return result


def ascii_version_of_hidden_card(cards:list):
    """
    :param cards: A list of card objects, the first will be hidden
    :return: A string, the nice ascii version of cards
    """
    # a flipper over card. # This is a list of lists instead of a list of string becuase appending to a list is better then adding a string
    lines = [['┌─────────┐'], ['│░░░░░░░░░│'], ['│░░░░░░░░░│'], ['│░░░░░░░░░│'], ['│░░░░░░░░░│'], ['│░░░░░░░░░│'], ['│░░░░░░░░░│'], ['│░░░░░░░░░│'], ['└─────────┘']]

    # store the non-flipped over card after the one that is flipped over
    cards_except_first = ascii_version_of_card(cards[1:], return_string=False)
    for index, line in enumerate(cards_except_first):
        lines[index].append(line)

    # make each line into a single list
    for index, line in enumerate(lines):
        lines[index] = ''.join(line)

    # convert the list into a single string
    return '\n'.join(lines)



def get_deck():
    suits_symbols = ['♠', '♦', '♥', '♣']
    suits_name = ['Spades', 'Diamonds', 'Hearts', 'Clubs']
    card_values = {
            'Ace': 11,  # value of the ace is high until it needs to be low
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
            '10': 10,
            'Jack': 10,
            'Queen': 10,
            'King': 10
        }
    card_list = []
    for name in suits_name:
        for values in card_values:
            card_list.append(Card(name, values))
    return card_list

def getCards(cards):
    choice = random.choice(cards)
    cards.remove(choice)
    return choice

def get_points(cards):
    hand = 0
    aces = []
    for i,card in enumerate(cards):
        if card.rank=='Ace':
            aces.append(i)
        hand+=card.points
    again = True
    while again:
        if hand>21 and len(aces)>0:
            hand -=10
            aces.pop()
        else:
            again = False

    return hand

def printCards(DealerCards,PlayerCards,dealershow=False):
    if dealershow:
        dealerhand = get_points(DealerCards)
        print(f"DEALER: {dealerhand}")
        print(ascii_version_of_card(DealerCards))
        playerhand = get_points(PlayerCards)
        print(f"PLAYER: {playerhand}")
        print(ascii_version_of_card(PlayerCards))
    else:
        print("DEALER: ???")
        print(ascii_version_of_hidden_card(DealerCards))
        playerhand = get_points(PlayerCards)
        print(f"PLAYER: {playerhand}")
        print(ascii_version_of_card(PlayerCards))


card_list = get_deck()
total_money = 5000
bet = input("How much do you bet? (1-5000, or Quit):\t")
if bet.lower() !="quit" or bet.lower()!="q":
    bet = int(bet)
    if bet <=5000:
        print(f"Bet: {int(bet)}")
        dealerCards=[getCards(card_list) for i in range(2)]
        playerCards=[getCards(card_list) for i in range(2)]
        
        
            
        printCards(DealerCards=dealerCards,PlayerCards=playerCards)

        play = True
        while play:
            inp = input("(H)it ,(S)tand, (D)double down:\t")
            if inp.lower()=="h" or inp.lower()=="hit":
                playerCards.append(getCards(card_list))
                printCards(DealerCards=dealerCards,PlayerCards=playerCards)
            if inp.lower()=="s" or inp.lower()=="stand":
                play = False
            if inp.lower()=="d" or inp.lower()=="double" or inp.lower()=="double down":
                more = input(f"How much do you want to increase your bet? (1-{5000-bet}:\t")
                bet += int(more)
                
                playerCards.append(getCards(card_list))
                play = False
                printCards(DealerCards=dealerCards,PlayerCards=playerCards)
        printCards(DealerCards=dealerCards,PlayerCards=playerCards,dealershow=True)
        showagain=False
        while get_points(dealerCards)<17:
            dealerCards.append(getCards(card_list))
            showagain = True
        if showagain:
            printCards(DealerCards=dealerCards,PlayerCards=playerCards,dealershow=True)
        dealerhand = get_points(dealerCards)
        playerhand = get_points(playerCards)
        
        won = False
        tie = False
        if dealerhand>21:
            won = True
        elif playerhand>21:
            won = False
        elif playerhand >dealerhand:
            won = True
        elif playerhand ==dealerhand:
            tie = True
            won = False
        else:
            won = False
        
        if tie:
            print(f"Game tied. You gained back your bet (Rs {bet})")
        else:
            if won:
                print(f"You won  ${bet}")
            else:
                print(f"You lost  ${bet}")
            
    else:
        print("You have excedded the bet limit ")


else:
    print("Thanks for playing")