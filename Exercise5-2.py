'''
Exercise 2: Write another program that prompts for a list of numbers as above
and at the end prints out both the maximum and minimum of the numbers instead
of the average.
'''
lista=list()
while True:
    number = input('Enter a number: ')
    try:
        list.append(lista,int(number))
    except:
        if number == 'done':
            break
        else:
            print('Invalid input')
print(sum(lista),len(lista),max(lista),min(lista))
del(lista)
