'''
Exercise 1: Write a while loop that starts at the last character
in the string and works its way backwards to the ﬁrst character
in the string, printing each letter on a separate line, except backwards.
'''
def contareverso(palavra):
    i=-1
    while i >= -len(palavra):
        print(palavra[i])
        i=i-1
