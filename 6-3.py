def contaletra(word,letra):
    count = 0
    for letter in word:
        if letter == letra:
            count = count + 1
    print(count)
