# ROCK-PAPER-SCISSORS AND OTHERS

## What is it?

- It's a spinoff of normal ROCK-PAPER-SCISSORS game with more options

## Rules

Quite simple. You, as a player, have 9 options:

1. Rock
2. Paper
3. Scissors
4. Lizard
5. Spock
6. Batman
7. Spiderman
8. Wizard
9. Glock

You will play against a computer by picking one of the choices. 

List of who can win against whom can be seen below:
    
    ROCK: ['LIZARD', 'WIZARD', 'SCISSORS', 'SPIDERMAN']

    SCISSORS: ['PAPER', 'WIZARD', 'LIZARD', 'SPIDERMAN']

    PAPER: ['ROCK', 'SPOCK', 'GLOCK', 'BATMAN']

    LIZARD: ['SPOCK', 'BATMAN', 'PAPER', 'GLOCK']

    SPOCK: ['WIZARD', 'SPIDERMAN', 'ROCK', 'SCISSORS']

    BATMAN: ['SPIDERMAN', 'SCISSORS', 'ROCK', 'SPOCK']

    SPIDERMAN: ['GLOCK', 'LIZARD', 'PAPER', 'WIZARD']

    GLOCK: ['ROCK', 'BATMAN', 'SPOCK', 'SCISSORS']

    WIZARD: ['BATMAN', 'PAPER', 'LIZARD', 'GLOCK']

## How to run and options:

### Windows
```
> python RPSAO.py
```

### Unix
```
> python3 RPSAO.py
```

### In-game options
```
- "r"|"rules" -> Check the rules and who wins against whom
- "q" -> Quit the game and obtain final results
- <1-9> -> Available options to play
```