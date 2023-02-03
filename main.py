import random

#Higher or Lower

#card constants
SUIT_TUPLE = ('Spades','Hearts','Clubs','Diamonds')
RANK_TUPLE = ('Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King')

NCARDS = 8

#Pass in a deck and this function returns a random card form the deck
def getCard(deckListIn):
    thisCard = deckListIn.pop() #Pop one off the top of the deck and return
    return thisCard

#Pass in a deck and this function returns a shuffled copy of the deck
def shuffle(deckListIn):
    deckListOut = deckListIn.copy()
    random.shuffle(deckListOut)
    return deckListOut

#Main Code
print('Welcome to Higher or Lower.')
print('You have to choose whether the next card to be shown will be higher or lower')
print('Getting it right add 20 points; get it wrong and you lose 15 points')
print('You have 50 points to start')
print()

startingDeckList = []

for suit in SUIT_TUPLE:
    for thisValue, rank in enumerate(RANK_TUPLE):
        cardDict = {'rank':rank, 'suit':suit, 'value':thisValue+1}
        startingDeckList.append(cardDict)

score = 50


while True: #play multiple games
    print()
    gameDeckList = shuffle(startingDeckList)
    currentCardDict = getCard(gameDeckList)
    currentCardRank = currentCardDict['rank']
    currentCardSuit = currentCardDict['suit']
    currentCardValue = currentCardDict['value']

    print('Starting card is ', currentCardRank + ' of'+currentCardSuit)
    print()

    for cardNumber in range(0,NCARDS): #play one game of this many cards
        answer = input('Will the next card be higher or lower than the' +currentCardRank + 'of ' + currentCardSuit +'? (enter h or l):')
        answer = answer.casefold() # force lower case
        nextCardDict = getCard(gameDeckList)
        nextCardRank = nextCardDict['rank']
        nextCardSuit = nextCardDict['suit']
        nextCardValue = nextCardDict['value']
        print('Next card is: ', nextCardRank +' of ' + nextCardSuit)
    
        if answer == 'h':
            if nextCardValue > currentCardValue:
                print('you got it right, it was higher. ')
                score += 20
            else:
                print('you got it wrong, it was higher. ')
                score -= 15
        elif answer == 'l':
            if nextCardValue < currentCardValue:
                print('you got it right, it was lower')
                score += 20
            else:
                print('you got it wrong, it was lower')
                score -= 15
        
        print('Your score is ', score)
        print()
        currentCardRank = nextCardRank
        currentCardSuit = nextCardSuit
        currentCardValue = nextCardValue
    
    goAgain = input('To play agian, press ENTER, or "q" to quit: ')

    if goAgain == 'q':
        break

print('Ok, Bye')
        




