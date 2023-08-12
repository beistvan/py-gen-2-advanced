a, b = input(), input()
game = {'stone-stone': 'draw', 'stone-scissors': 'John', 'stone-paper': 'Jack',
        'scissors-scissors': 'draw','scissors-paper': 'John', 'scissors-stone': 'Jack',
        'paper-paper': 'draw','paper-stone': 'John','paper-scissors': 'Jack'}
print(game[a + "-" + b])

