from enum import Enum, auto
from random import randint


class Options(Enum):
    ROCK = auto()
    PAPER = auto()
    SCISSORS = auto()
    LIZARD = auto()
    SPOCK = auto()
    SPIDERMAN = auto()
    BATMAN = auto()
    WIZARD = auto()
    GLOCK = auto()


class Game:
    NEW_LINE = "\n"
    HINT = f"Choose one: {NEW_LINE}{NEW_LINE.join([f'{option.name} - {index + 1}' for index, option in enumerate(Options)])}\n\nPress 'Q' and 'Enter' to quite a game.\n"
    RULES = {
        Options.ROCK: [Options.LIZARD, Options.WIZARD, Options.SCISSORS, Options.SPIDERMAN],
        Options.SCISSORS: [Options.PAPER, Options.WIZARD, Options.LIZARD, Options.SPIDERMAN],
        Options.PAPER: [Options.ROCK, Options.SPOCK, Options.GLOCK, Options.BATMAN],
        Options.LIZARD: [Options.SPOCK, Options.BATMAN, Options.PAPER, Options.GLOCK],
        Options.SPOCK: [Options.WIZARD, Options.SPIDERMAN, Options.ROCK, Options.SCISSORS],
        Options.BATMAN: [Options.SPIDERMAN, Options.SCISSORS, Options.ROCK, Options.SPOCK],
        Options.SPIDERMAN: [Options.GLOCK, Options.LIZARD, Options.PAPER, Options.WIZARD],
        Options.GLOCK: [Options.ROCK, Options.BATMAN, Options.SPOCK, Options.SCISSORS],
        Options.WIZARD: [Options.BATMAN, Options.PAPER, Options.LIZARD, Options.GLOCK],
    }

    def __init__(self) -> None:
        self.first_round = True
        self.human = 0
        self.pc = 0
        self.ties = 0

    def evaluate(self, human: Options, pc: Options) -> None:
        if human == pc:
            self.ties += 1
            return

        if pc in Game.RULES[human]:
            self.human += 1
            return

        self.pc += 1
    def play(self) -> None:
        CHOICES = [option.name for option in Options]
        def is_input_invalid(user_input: str) -> bool:
            return (
                not user_input.isdigit() 
                and not user_input.lower() in["q","rules","r"]
            )

        while True:
            user_input = input(Game.HINT) if self.first_round else input("Your choice:\n")
            self.first_round = False
            if is_input_invalid(user_input):
                print(Game.HINT)
                continue

            if user_input.lower() == "q":
                print(
                    f"Thanks for playing.\nFinal score:\n\nYou: {self.human}\nComuter: {self.pc}\nTies: {self.ties}"
                )
                return
            
            if user_input.lower() in ["rules", "r"]:
                print(
                    self.__get_rules()
                )
                continue

            user_input = int(user_input)
            if user_input < 1 or user_input > 9:
                print(Game.HINT)
                continue

            choice = Options[CHOICES[user_input - 1]]
            computers_choice = Options[CHOICES[randint(0, 4)]]

            print(
                f"\nYour choice: {choice.name}\nComputer's choice: {computers_choice.name}\n"
            )

            self.evaluate(choice, computers_choice)

    def __get_rules(self) -> str:
        return f"""
    Pick a number between 1-9 corresponding to appropriate Option.
    Options: 
    
    {Game.HINT}
    
    From 9 options you have, each option can win against 4 other options, lose against other 4 and tie with itself.
    
    List of who can win against whom can be seen below:
    
    {Game.NEW_LINE.join([f'{key.name}: {[option.name for option in value]}{Game.NEW_LINE}' for key, value in Game.RULES.items()])}

    To Quit the game press 'Q' and 'ENTER'.
    """

if __name__ == "__main__":
    game = Game()
    game.play()
