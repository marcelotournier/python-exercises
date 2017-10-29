import os
os.chdir('C:/Users/macjr/Desktop/')
fname = input('Enter the file name: ')
fhand = open(fname)
count = 0
for line in fhand:
    if line.startswith('From:'):
        count = count + 1
print('There were', count, 'From lines in', fname)
