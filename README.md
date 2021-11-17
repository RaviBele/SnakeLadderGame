# SnakeLadderGame
Snake and Ladder Design

Problem statement:
**Developing a Game of
Snakes and Ladders**

1. Make the game run for 10 turns
2. Design it for a single player
3. Push the code to github and share the github repo.
4. The problem can be solved in any language.


**Story #1: Basic Board**
On a board (Of size 100), for a dice throw a player should
move from initial position by the number on dice throw

**Story #2: Add a snake on the board**
A snake moves a player from its start position to end position
where start position > end position

Test data: Add a snake at position 14 moving the player
to position 7.

**Story #3: Make A Crooked Dice**

A dice that only throws Even numbers.
The can game can be started with normal dice or crooked
dice.

Design:
![SnakeLadder](https://user-images.githubusercontent.com/24969715/142224616-51f470d4-faeb-4c56-9f51-214d7b7c917d.png)


Automated test run with single player:

```[xxx@xxxxx game]# python3 snakeLadderGame.py 
Enter number of players: 1
Enter name of player no 1:ravi
Player: ravi moving from 0 to 5 with dice value: 5
Player: ravi moving from 5 to 10 with dice value: 5
Player: ravi moving from 10 to 15 with dice value: 5
Player: ravi moving from 15 to 18 with dice value: 3
Player: ravi moving from 18 to 23 with dice value: 5
Player: ravi moving from 23 to 28 with dice value: 5
Player: ravi moving from 28 to 31 with dice value: 3
Player: ravi moving from 31 to 37 with dice value: 6
Player: ravi moving from 37 to 41 with dice value: 4
Player: ravi moving from 41 to 45 with dice value: 4
snake head 47 snake tail 17
Snake bites me. Going down.
Player: ravi moving from 45 to 17 with dice value: 2
Player: ravi moving from 17 to 21 with dice value: 4
Player: ravi moving from 21 to 27 with dice value: 6
Player: ravi moving from 27 to 28 with dice value: 1
Player: ravi moving from 28 to 29 with dice value: 1
Player: ravi moving from 29 to 34 with dice value: 5
Player: ravi moving from 34 to 38 with dice value: 4
Player: ravi moving from 38 to 40 with dice value: 2
Player: ravi moving from 40 to 46 with dice value: 6
snake head 47 snake tail 17
Snake bites me. Going down.
Player: ravi moving from 46 to 17 with dice value: 1
Player: ravi moving from 17 to 22 with dice value: 5
Player: ravi moving from 22 to 25 with dice value: 3
Player: ravi moving from 25 to 27 with dice value: 2
Player: ravi moving from 27 to 31 with dice value: 4
Player: ravi moving from 31 to 33 with dice value: 2
Player: ravi moving from 33 to 37 with dice value: 4
Player: ravi moving from 37 to 42 with dice value: 5
Player: ravi moving from 42 to 43 with dice value: 1
Player: ravi moving from 43 to 45 with dice value: 2
Player: ravi moving from 45 to 51 with dice value: 6
Player: ravi moving from 51 to 56 with dice value: 5
Player: ravi moving from 56 to 60 with dice value: 4
Player: ravi moving from 60 to 64 with dice value: 4
Player: ravi moving from 64 to 67 with dice value: 3
Player: ravi moving from 67 to 72 with dice value: 5
Player: ravi moving from 72 to 74 with dice value: 2
Player: ravi moving from 74 to 79 with dice value: 5
Player: ravi moving from 79 to 82 with dice value: 3
Player: ravi moving from 82 to 85 with dice value: 3
Player: ravi moving from 85 to 86 with dice value: 1
Player: ravi moving from 86 to 88 with dice value: 2
Player: ravi moving from 88 to 93 with dice value: 5
Player: ravi moving from 93 to 96 with dice value: 3
Player: ravi moving from 96 to 99 with dice value: 3
Player: ravi moving from 99 to 99 with dice value: 5
Player: ravi moving from 99 to 99 with dice value: 6
Player: ravi moving from 99 to 99 with dice value: 3
Player: ravi moving from 99 to 99 with dice value: 2
Player: ravi moving from 99 to 99 with dice value: 5
Player: ravi moving from 99 to 99 with dice value: 5
Player: ravi moving from 99 to 99 with dice value: 6
Player: ravi moving from 99 to 99 with dice value: 6
Player: ravi moving from 99 to 99 with dice value: 6
Player: ravi moving from 99 to 99 with dice value: 5
Player: ravi moving from 99 to 99 with dice value: 2
Player: ravi moving from 99 to 99 with dice value: 4
Player: ravi moving from 99 to 99 with dice value: 3
Player: ravi moving from 99 to 100 with dice value: 1
Player: ravi won with rank: 1
Game over```

