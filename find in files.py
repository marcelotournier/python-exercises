# referencia arquivos mbox: https://en.wikipedia.org/wiki/Mbox
fhand = open('C:/Users/macjr/Desktop/mbox-short.txt')
for line in fhand:
    #line = line.rstrip()
    if line.find('@uct.ac.za') == -1:
        continue 
    #if line.startswith('From:'):
    print(line.rstrip())
# Skip 'uninteresting lines'        
    #if not line.startswith('From:'):
        #continue
# Process our 'interesting' line
    #print(line)
