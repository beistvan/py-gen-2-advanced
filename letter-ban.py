word = input() + ' ban the letter'

b = list(map(chr, range(ord('a'), ord('z' ) + 1)))

for i in b:
    if i in word:
        word += " " + i
        print(word)
        word = word.replace(i, '').replace('  ', ' ').strip()
        if len(word) < 1:
            break
