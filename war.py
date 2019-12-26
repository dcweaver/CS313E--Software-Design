#  File: War.py
#  Description:
#  Student's Name: David Chase Weaver   
#  Student's UT EID: dcw2269
#  Course Name: CS 313E 
#  Unique Number: 
#
#  Date Created: February 20, 2019
#  Date Last Modified:

import random

#define lists for the card suits and numbers
listSuit = ["C", "D", "H", "S"]
listRank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]


#create class for a stack datatype
class Stack:

    def __init__(self):
        self.items = [ ]

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]
    
    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)
    
############################################
    
class Card:

    def __init__(self, Suit, Rank):

        self.Suit = Suit
        self.Rank = Rank

    #Define a method to print out each card
    def __str__(self):
        return str(self.Rank) + str(self.Suit)

#######################################################
    
class Deck:
    #create a deck of 52 cards, each with different suit and rank and put them in order
    def __init__(self):

        self.cardList = [ ]
        for i in listSuit:
            for j in listRank:
                self.cardList.append(Card(i,j))

            #Create deck of card OBJECTS and not a list of strings that represent the cards


    #Define print method for printing out the deck in 4 rows of 13 cards
    def __str__(self):
        
        for i in range(len(self.cardList)):
            #if the card index is not the last one in each row, print normally
            if i not in (12, 25, 38):
                print(format(str(self.cardList[i]),">4s"), end = "")
            #If index is at the end of a row, prints a new line
            else:
                print(format(str(self.cardList[i]),">4s"))
        return ""

    #define method to shuffle the cards in the deck into a random order
    def shuffle(self):
        random.seed(15)
        random.shuffle(self.cardList)

    #method to remove first card from deck list and append that card to player's hand
    def dealOne(self, Player):
        Player.handTotal += 1
        return Player.hand.append(self.cardList.pop(0))

#################################
    
class Player:


    def __init__ (self):
        self.hand = [ ]
        self.handTotal = 0
    def __str__(self):
        
        for i in range(len(self.hand)):
            #if the card index is not the last one in each row, print normally
            if i not in (12,25,38) :
                print(format(str(self.hand[i]),">4s"), end = "")
            #If index is at the end of a row, prints a new line
            else:
                print(format(str(self.hand[i]),">4s"))
        return ""

        
    def takeCards(self,Player,numCards):

        self.numCards = numCards
        
        # Creates a temp list of cards used in round
        self.tempCards = self.hand[0:int(self.numCards+1)]
    
        # Deletes winner's cards used in round from hand
        del self.hand[0:int(self.numCards+1)]

        # Adds loser's cards to winner's hand
        self.hand += Player.hand[0:int(self.numCards+1)]
 
        # Adds winner's card used in round back into hand
        self.hand += self.tempCards     
        
        
    def stillHasCards(self):
        return len(self.handTotal) != 0
        
#Define function to have 2 players play a game of war
def playGame(cardDeck, player1, player2):
    
    #Have dealer deal half of the deck to each player, one at a time
    for i in range(26):             
       cardDeck.dealOne(player1)    
       cardDeck.dealOne(player2)
    
    print("Initial hands: \nPlayer 1:")   #print out the initial hands for each player
    print(player1, "\n")
    print("Player 2:")
    print(player2, "\n\n\n")
    totalRounds = 0
    
    
    
    while player1.stillHasCards and player2.stillHasCards:  
        totalRounds += 1
        print("ROUND " + str(totalRounds))
        print("Player 1 plays: ", str(player1.hand[0]))
        print("Player 2 plays: ", str(player2.hand[0]), "\n")
        
        #if player 1 wins the round
        if listRank.index(str(player1.hand[0])[0]) > listRank.index(str(player2.hand[0])[0]):
            roundWinner = player1
            roundLoser = player2
            winner = "Player 1"
            print(winner +  " wins round " +  str(totalRounds) + ": " + str(player1.hand[0]) + " > " + str(player2.hand[0]))
            del player2.hand[0]
            player1.handTotal += 1
            player2.handTotal -= 1
            roundWinner.takeCards(roundLoser,0)
            
            print("\nPlayer 1 now has,", player1.handTotal, "card(s) in hand:")
            print(player1)
        
            print("Player 2 now has,", player2.handTotal, "card(s) in hand:")
            print(player2, "\n\n")
            
        #if player 2 wins the round        
        elif listRank.index(str(player1.hand[0])[0]) < listRank.index(str(player2.hand[0])[0]):
            roundWinner = player2
            roundLoser = player1
            winner = "Player 2"
            print(winner + "wins round " +  str(totalRounds) + ": " + str(player2.hand[0])[0] + " > " + str(player1.hand[0]))
            del player1.hand[0]
            player2.handTotal += 1
            player1.handTotal -= 1
            roundWinner.takeCards(roundLoser, 0)
            
            if player2.hand[0] == 1:
                player2.hand[0] == 10
            
            
            print("\nPlayer 1 now has,", player1.handTotal, "card(s) in hand:")
            print(player1)
        
            print("Player 2 now has,", player2.handTotal, "card(s) in hand:")
            print(player2, "\n\n")


            #Create if statement for if war happens
        elif str(player1.hand[0])[0] == str(player2.hand[0])[0]:
            print("War starts: ", player1.hand[0], "=", player2.hand[0])
            #Have each player put 3 cards face down
            for i in range(3):
                print("Player 1 puts", format(str(player1.hand[i+1]),">3s"), "face down")
                print("Player 2 puts", format(str(player2.hand[i+1]),">3s"), "face down")

            #Have each player flip the next card in the deck flip up  
            print("Player 1 puts", format(str(player1.hand[4]),">3s"), "face up")
            print("Player 2 puts", format(str(player2.hand[4]),">3s"), "face up \n")


            #if player 1 wins the war 
            if listRank.index(str(player1.hand[4])[0]) > listRank.index(str(player2.hand[4])[0]):
                roundWinner = player1
                roundLoser = player2
                winner = "Player 1"
                print(winner, "wins round " + str(totalRounds) + ": "+ str(player1.hand[4]) + " > " + str(player2.hand[4]))
                del player2.hand[0:5]
                player1.handTotal += 5
                player2.handTotal -= 5
                roundWinner.takeCards(roundLoser, 4)   
                
                #if player 2 wins the war
            elif listRank.index(str(player1.hand[4])[0]) < listRank.index(str(player2.hand[4])[0]):
                roundWinner = player2
                roundLoser = player1
                print("Player 2 wins round 1: " + str(player2.hand[4]) + " > " + str(player1.hand[4]))
                del player1.hand[0:5]
                player2.handTotal += 5
                player1.handTotal -= 5
                roundWinner.takeCards(roundLoser, 4)                                                                          
            
        
            print("\nPlayer 1 now has,", player1.handTotal, "card(s) in hand:")
            print(player1)
        
            print("Player 2 now has,", player2.handTotal, "card(s) in hand:")
            print(player2, "\n\n")

        
        
def main():
    #Create 2 players for the game, player 1 and player 2
    player1 = Player()
    player2 = Player()
    
    #Create Deck of 52 cards
    cardDeck = Deck()

    #print the deck in order before shuffling
    print("Initial deck:")
    print(cardDeck,"\n")                 
    
    random.seed(15)
   #Have dealer shuffle the deck
    cardDeck.shuffle()

    #Print the shuffled deck
    print("Shuffled deck:")
    print(cardDeck)
    print("\n")

    playGame(cardDeck, player1, player2)


    player1.stillHasCards
main()
        
