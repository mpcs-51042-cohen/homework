# Card Game: Blackjack

## AI Policy Reminder

You can use the internet, including AI engines, but you must use them similar to if you had a smart friend to work with:

1. You CAN ask high-level questions:
   For example, "Does Python have a built-in ability to read JSON files, or do I need to import something?"

2. You CANNOT ask for the solution code by entering this assignment as a prompt.
   For example, "Generate a Python program to read the given files and generate the following output: .." is NOT PERMITTED

3. You MAY ask for SAMPLE code to demonstrate various examples of Python usage
   For example, "Can you show me a short example of how to read lines from a file on disk?"
   This is acceptable because you're asking for help on a general principle, from which you must
   still apply to the specifics of this assignment.

4. Whenever you learn something new from AI that you then apply to your work, you MUST CITE the exact prompt(s) and LLM engine that you used and what you learned from it that you felt helped you with this assignment.

For convenience, you can update this README.md file with your citations.

### Assignment Objectives

This assignment is written to help you identify your current strengths/weaknesses in the following areas:

- Python control flow
- Boolean logic
- Loops
- Using several kinds of data structures in the same application
- Keyboard and Screen I/O


### Assignment Instructions

Your challenge is to write a console-mode game that lets the user play the card game "Blackjack" against the computer.  If you've never played Blackjack, you can find lots of examples online, but our requirements are simpler than true Vegas-style Blackjack.

I've already given you a starter file, blackjack.py, that imports the `random` and `time` modules.
You may NOT import any other modules.

**Here are the rules of the game:**

1. It starts by dealing two cards to each player in the following way:
  - A deck of cards should be randomly shuffled.
  - First, the computer should be dealt two cards, one face up and one face down.
  - Next, the user should be dealt two cards, both face up.  
  - The user's hand is evaluated. See the section on "Human Hand Evaluation".
  - If the user did not win nor lose after evaluation, the game continues to Step 2.

2. The user gets to take actions.
  - The user is given the choice to "Hit" (take another card) or "Stand".  
  - If they choose "Hit", they are dealt another card face up and the user's hand is evaluated. See the section on "Human Hand Evaluation."
  - If they choose "Stand", go directly to Step 3.
  - Go back to the beginning of Step 2 to give the user a choice to Hit or Stand.

3. The computer gets to take actions.
  - If this is the first time the computer gets to act, "reveal" the computer's original face-down card. (You can do this by just showing two new cards, or you may have a more creative approach, it's up to you.)
  - Next, the computer's hand is evaluated. See "Computer Hand Evaluation."
  - Depending on the evaluation, the computer will either win, take a card, lose, or tie the human player.
  
4. The game should announce the result of the hand.

5. The game should ask the user if they want to play another hand.  If so, the cards should be reshuffled
   and play starts over completely with a "new deck" of cards. 

ALSO: There must be a 1-second delay when dealing any new cards so that the game "feels" like a real game.


**Human Hand Evaluation:**

  1. The cards are added up to calculate a total
    - Cards 2 thru 9 are worth that number of points
    - Cards 10, J, Q, K are each worth 10 points
    - An Ace card is worth 1 point OR 11 points, whichever is more advantageous in the moment
    (OR for simplicity, you can opt to always count an ace as always 1 or 11; 
    but at the cost of one grading point, see the grading rubric below)

  2. If the total equals 21, the user wins instantly!  Go directly to Step 4 above to announce the winner.
  3. If the total is over 21, the user loses instantly! Go directly to Step 4 above to announce the winner.  

**Computer Hand Evaluation:**

  1. The cards are added up to calculate a total
    - Cards 2 thru 9 are worth that number of points
    - Cards 10, J, Q, K are each worth 10 points
    - An Ace card is worth 1 point OR 11 points, whichever is more advantageous in the moment

  2. If the total equals 21, the computer wins instantly!  Go directly to Step 4 above to announce the winner.
  3. If the total is over 21, the computer loses instantly! Go directly to Step 4 above to announce the winner.  
  4. If the total is 16 or less, the computer must choose "Hit". Go to Step 3 in the main instructions again.  
  5. If the total is 17 thru 20, the computer must choose "Stand".
    - If the computer ends up with a score greater than the user, the computer wins. 
    - If the computer ends up with a score less than the user, the user wins.
    - If the computer ends up with the same score as the user, the game is declared a TIE.
    - Go to Step 4.

**Note to Blackjack Experts**

1. Yes, I know we're not letting the computer win with an initial blackjack. Instead
we will always give the human user a chance to win first.
2. There's no option for doubling down or splitting the hand.
3. There are probably lots of other rules that I've omitted for simplicity.

### Grading Rubric

* Up to 4 points for correct user-related logic
* Up to 4 points for correct computer-related logic
* 1 point for proper dynamic 1-or-11 scoring of Ace cards
* 1 point for the one-second delay when dealing cards

