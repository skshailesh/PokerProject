
from card import Card
from stack_of_cards import StackOfCards
from player import Player

# These are the winning hands in order of strength
WINNING_HANDS = [ "Royal Flush", \
                  "Straight Flush", \
                  "Four of a Kind", \
                  "Full House", \
                  "Flush", \
                  "Straight", \
                  "3 of a Kind", \
                  "Two Pairs", \
                  "Pair (Jacks or better)" ]

# make a PokerCard Class inherit from Card
class PokerCard(Card):

  def __init__(self, rank, suit):
    super().__init__(rank, suit)
  '''
  the getValue fnc overrides its parent getValue fnc in the Card class and returns a value of 14 for A instead of 1
  '''
  def getValue(self):
    if self.rank == 'A':
        return(14)
    elif self.rank == 'J':
        return(11)
    elif self.rank == 'Q':
        return(12)
    elif self.rank == 'K':
        return(13)
    elif self.rank in '23456789' or self.rank == '10':
        return(int(self.rank))
    else:
        raise ValueError('{} is of unkwown value'.format(self.rank))

  '''
  In addition to the __eq__ and __lt__ functions, we added in the rest of the comparing methods to make comparing the cards much easier and convenient
  '''
  def __eq__(self, other):
    return (self.getValue() == other.getValue())

  def __gt__(self,other):
    return (self.getValue() > other.getValue())

  def __lt__(self, other):
    return (self.getValue() < other.getValue())
  
  def __ge__(self,other):
    return (self.getValue() >= other.getValue())
  
  def __le__(self, other):
    return (self.getValue() <= other.getValue())
  

class PokerHand(StackOfCards):

  '''
  PokerHand acts as the basic class for the deck of cards and the player's hand's objects. It also determines the type of hand the player has
  '''
  def __init__(self):
    self.cards = []

  def sort(self):
    self.cards.sort()
  
  def insert(self, pos, str1):
    self.cards.insert(pos, str1)

  def length(self):
    return len(self.cards)
  
  def handType(self):
    '''
    handType is the function which determines the player's hand type by returning the type of hand, in this part it identifies Royal or Straight Flushes
    '''
    self.cards.sort()
    if self.cards[0].getSuit()==self.cards[1].getSuit() and self.cards[1].getSuit()==self.cards[2].getSuit() and self.cards[2].getSuit()==self.cards[3].getSuit()and self.cards[3].getSuit()==self.cards[4].getSuit():
      if (self.cards[0].getValue()+4) == (self.cards[1].getValue()+3) and (self.cards[1].getValue()+3) == (self.cards[2].getValue()+2) and (self.cards[2].getValue()+2) == (self.cards[3].getValue()+1) and (self.cards[3].getValue()+1) == self.cards[4].getValue():
        if self.cards[0].getValue() == 10:
          return "Royal Flush"
        else:
          return "Straight Flush"
      else:
        x = 0
    ''' By counting the number of double, triple, or four repeats, the Four of a Kind and Full House can be both identified without repetitive code 
    '''
    repeat=0
    double =0
    triple =0
    four =0
    for x in range(len(self.cards)-3):
      if self.cards[repeat].getValue() == self.cards[repeat+1].getValue() == self.cards[repeat+2].getValue() == self.cards[repeat+3].getValue():
        four +=1
        repeat+=1
      else:
        repeat +=1
    repeat =0
    for x in range(len(self.cards)-2):
      if self.cards[repeat].getValue() == self.cards[repeat+1].getValue() == self.cards[repeat+2].getValue():
        triple +=1
        repeat +=1
      else:
        repeat +=1
    repeat =0
    for x in range(len(self.cards)-1):
      if self.cards[repeat].getValue() == self.cards[repeat+1].getValue():
        double +=1
        repeat +=1
      else:
        repeat +=1
    if four == 1:
      return "Four of a Kind"
    if triple ==1 and double > 2:
          return "Full House"
    
    elif self.cards[0].getSuit()==self.cards[1].getSuit() and self.cards[1].getSuit()==self.cards[2].getSuit() and self.cards[2].getSuit()==self.cards[3].getSuit()and self.cards[3].getSuit()==self.cards[4].getSuit():
      return "Flush"    
    elif (self.cards[0].getValue()+4) == (self.cards[1].getValue()+3) and (self.cards[1].getValue()+3) == (self.cards[2].getValue()+2) and (self.cards[2].getValue()+2) == (self.cards[3].getValue()+1) and (self.cards[3].getValue()+1) == self.cards[4].getValue():
       return "Straight"
  
    repeat =0
    double=0
    triple=0
    four=0
    for x in range(len(self.cards)-3):
      if self.cards[repeat].getValue() == self.cards[repeat+1].getValue() == self.cards[repeat+2].getValue() == self.cards[repeat+3].getValue():
        four +=1
        repeat+=1
      else:
        repeat +=1
    repeat =0
    for x in range(len(self.cards)-2):
      if self.cards[repeat].getValue() == self.cards[repeat+1].getValue() == self.cards[repeat+2].getValue():
        triple +=1
        repeat +=1 
      else:
        repeat +=1
    repeat = 0
    if triple ==1: 
      return "3 of a Kind"
    for x in range(len(self.cards)-1):
      if self.cards[repeat].getValue() == self.cards[repeat+1].getValue():
        double +=1
        repeat +=1
      else:
        repeat +=1
    if double == 2:
      return "Two Pairs"
    repeat = 0
    double = 0
    for x in range(len(self.cards)-1):
      if self.cards[repeat].getValue() == self.cards[repeat+1].getValue() and self.cards[repeat].getValue() >= 10:
        double +=1
        repeat +=1
      else:
        repeat += 1
    if double==1:
        return "Pair (Jacks or better)"
    else:
      return "None"
        

class PokerPlayer(Player):
  
  '''
  PokerPlayer is the class for the player themselves's object. It stores the player's name, balance, and hand
  '''
  def __init__(self, name, amount, cards):
    super().__init__(name, amount, cards)

  def askHoldChoice(self):
    hold = (input("Which cards would you like to hold? (ex. 1 3) "))
    return(hold)

  def __str__(self):
    return(str(self.getMoney()))


def PokerGame():
  
  '''
  PokerGame is what is called to start the game. It starts the game by asking the player their information such as their name and how many credits they would like to play with. It then creates a shuffled deck of 52 cards and creates the player object. Afterwards, it calls the playRound fnc and asks the player would they like to play again. A new round is played until the player does not wish to play another round and types 'n' when the game asks if they would like to play again.
  '''
  
  print('Welcome to Video Poker!')
  pname = input('What is your name? ')
  pcreds = input('How many credits would you like to play with? ')
  deck = PokerHand()
  for x in range(2, 11):
      for y in ('♣', '♥', '♦', '♠'):
          deck.add(PokerCard(str(x), y))
  for z in ('J', 'Q', 'K', 'A'):
      for y in ('♣', '♥', '♦', '♠'):
          deck.add(PokerCard(z, y))
  deck.shuffle()
  
  hand = PokerHand()
  player1 = PokerPlayer(pname, int(pcreds), hand)
  
  playRound(player1, deck)
  
  playAgain = input('Would you like to play again? (y/n) ')
  print('')
  if playAgain == 'y':
    while playAgain == 'y':
      deck = PokerHand()
      for x in range(2, 11):
        for y in ('♣', '♥', '♦', '♠'):
          deck.add(PokerCard(str(x), y))
      for z in ('J', 'Q', 'K', 'A'):
        for y in ('♣', '♥', '♦', '♠'):
          deck.add(PokerCard(z, y))
      deck.shuffle()
      hand = PokerHand()
      pcreds2 = player1.getMoney()
      player1 = PokerPlayer(pname, int(pcreds2), hand)
      playRound(player1, deck)
      playAgain = input('Would you like to play again? (y/n) ')
      print('')
      if playAgain == 'n':
        print("Thanks for playing!")
        return('')
  else:
    print("Thanks for playing!")
    return('')
  

def playRound(p, d):

  '''
  playRound is the bulk of the poker game and is what is called to actually play the game. When this function is called, the player bets an amount of money based on their own input. Their earnings are proportional to their bet, meaning the amount they win is multiplied by the amount they bet. The player is then dealt 5 cards and is asked to hold the cards they wish to hold. There is also a guide to tell you if you have been dealt a hand. For example, if the hand you are dealt has two Js, the guide will print out 'Pair (Jacks or Better)'. After the player holds their desired cards, they then receive their new hand and win their earnings
  '''

  print("You have " + str(p.getMoney()) + " credits")
  betstr = input('How many credits would you like to bet? ')
  while int(betstr) > p.getMoney():
    print('You do not have enough credits to bet this much, please bet responsibly')
    betstr = input('How many credits would you like to bet? ')
  p.addMoney(-int(betstr))
  print("You have " + str(p.getMoney()) + " credits left")

  for n in range(5):
      p.addCard(d.deal())
  p.hand.sort()
  print(str(p.getName()) + "'s hand:", end = '')
  print(p.hand)
  for whand in WINNING_HANDS:
      if whand == p.hand.handType():
          print(whand)
      else:
          print(end = '')

  holdlst = p.askHoldChoice()
  holdstr = ''
  for x in holdlst:
    if len(holdlst) == 0:
      holdstr = ''
    if x not in '12345':
      holdstr += ''
    else:
      holdstr += x
    
  holdlst2 = []
  newHand = PokerHand()
  if holdstr == '':
    for x in range(4):
      p.removeCard(0)
  for y in holdstr:
    holdlst2.append(int(y))
  for z in holdlst2:
    idx = 0
    for x in range(5):
      if (z-1) == idx:
        newHand.add(p.removeCard(z - 1))
        p.hand.insert(z - 1, PokerCard('Placeholder', 'placeholder'))
        idx += 1
      else:
        idx += 1
  p.hand = newHand
  print('You held:' + str(newHand))

  while p.hand.length() < 5:
    p.addCard(d.deal())
  p.hand.sort()

  print(str(p.getName()) + "'s hand:", end = '')
  print(p.hand)

  pointsWon = 0
  handtype = p.hand.handType()
  pcreds = p.getMoney()
  if handtype == 'None':
    print('Nothing, you lost')
    print('You have ' + str(pcreds) + ' credits')
  for whand in WINNING_HANDS:
    if whand == handtype:
      pointsWon = pointValue(p.hand) * int(betstr)
      if whand == p.hand.handType():
          pointsWon = pointValue(p.hand) * int(betstr)
          print(whand + '! Congratulations, you won ' + str(pointsWon) + ' credits!')
          p.addMoney(pointsWon)
          pcreds = p.getMoney()
          print('You have ' + str(pcreds) + ' credits')
      elif whand != p.hand.handType():
          print(end = '')
      elif p.hand.handType() == 'Royal Flush':
          print(end = '')
      elif whand == 'None':
          print('Nothing, you lost')
          print('You have ' + str(pcreds) + ' credits')


def pointValue(hand):
  
  '''
  pointValue is an extra fnc added to make it easier to retreive the point amounts for each hand
  '''

  if hand.handType() == 'Royal Flush':
    return 250
  elif hand.handType() == 'Straight Flush':
    return 50
  elif hand.handType() == 'Four of a Kind':
    return 25
  elif hand.handType() == 'Full House':
    return 9
  elif hand.handType() == "Flush":
    return 6
  elif hand.handType() == 'Straight':
    return 4
  elif hand.handType() == "3 of a Kind":
    return 3
  elif hand.handType() == 'Two Pairs':
    return 2
  elif hand.handType() == "Pair (Jacks or better)":
    return 1
  else:
    return 0


def main():
    PokerGame()
    
if __name__ == "__main__":
    main()

        

