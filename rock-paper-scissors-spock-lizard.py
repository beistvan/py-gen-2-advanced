a, b = input(), input()
game = {'rock-rock': 'draw', 'rock-scissors': 'John', 'rock-paper': 'Jack',
        'rock-lizard': 'John', 'rock-Spock': 'Jack', 'scissors-scissors': 'draw',
        'scissors-paper': 'John', 'scissors-rock': 'Jack', 'scissors-lizard': 'John',
        'scissors-Spock': 'Jack', 'paper-paper': 'draw', 'paper-rock': 'John',
        'paper-scissors': 'Jack', 'paper-lizard': 'Jack', 'paper-Spock': 'Jack',
        'lizard-lizard': 'draw', 'lizard-Spock': 'John', 'lizard-scissors': 'Jack',
        'lizard-paper': 'John', 'lizard-rock': 'Jack', 'Spock-Spock': 'draw',
        'Spock-scissors': 'John', 'Spock-paper': 'Jack', 'Spock-rock': 'John',
        'Spock-lizard': 'Jack'}
print(game[a + "-" + b])
