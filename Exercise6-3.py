'''
Encapsulate this code in a function named count, and generalize it
so that it accepts the string and the letter as arguments.

word = 'banana'
count = 0
    for letter in word:
        if letter == 'a':
        count = count + 1
print(count)

'''
def lettercount(word,letra):
    count = 0
    for l in word:
        if l == letra:
            count = count + 1
    print(count)
