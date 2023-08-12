a, b = input(), input()
game = {'rock-rock': 'draw', 'rock-scissors': 'John', 'rock-paper': 'Jack',
        'scissors-scissors': 'draw','scissors-paper': 'John', 'scissors-rock': 'Jack',
        'paper-paper': 'draw','paper-rock': 'John','paper-scissors': 'Jack'}
print(game[a + "-" + b])
