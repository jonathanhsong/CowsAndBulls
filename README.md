# CowsAndBulls
COMS1002 Assignment


Write an application in Python that allows a user to play the game Bulls and Cows against a computer. The game works as follows: The computer chooses a 4-digit number in secret. The digits must all be different.  The user then guesses the number and the computer provides the number of matching digits. If the matching digit is in the right position it is a "bull", if it is on a different position it is a "cow". For example:

 

Computer chooses: 3691

User guesses:1649

Computer answers:1 bull and 2 cows

 

If the user guesses a number with repeat digits that is partially correct the rule is that a correct digit can only count once and bulls count before cows. So for example

 

Computer chooses: 3691

User guesses: 4211

Computer answers:1 bull and 0 cows


READ ME FIRST!
------------------------------------------------------------------------------
How to play the game:
Run the file called game.py

Make sure both the bulls_and_cows.py and game.py files are in the same 
directory

The game will generate an answer of 4 unique digits. It will prompt the user
for a guess. After inputing the guess the game will return the number of Bulls
and Cows in your guess. 

What is a Bull?
A Bull is a digit in the user's guess that matches the value and 
position of the answer.

What is a Cow?
A Cow is a a digit in the user's guess that matches a digit in the answer
but not the position.

NOTE: A digit cannot be both a Bull and a Cow. 
------------------------------------------------------------------------------

Design

I wrote this code to be as efficient as possible with respect to checking the
conditions of whether or not a user's input would constitute a Bull, Cow, or
neither.
 
I was tempted to call the Bulls function within Cows seeing as part of being
a Cow is NOT being a Bull, but I found it faster to simple create a new
if statement using the arugments established by the for loop above 
(See lines 38 and 42)

Additionally I felt that "for" loops would be best here as opposed to "while"
due to the fact that I am iterating over string slices instead of looping 
while some condition is or is not met. 

The only "while" loop I implemented was for the secret generator because as 
long as the unique digit condition was not met.

------------------------------------------------------------------------------

Improvements

-I would like to make the interaction between the game and user more natural 
-Asking a user for input regarding difficulty settings and adjust the length
of the answer 
-Improve the efficiency of generating the answer
