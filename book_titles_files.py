file = open("/usercode/files/books.txt", "r")

#your code goes here 
for i in file: 
    if i[-1] == '\n':
        print('{}{}'.format(i[0], len(i)-1))
    else:   
        print('{}{}'.format(i[0], len(i)))

file.close()
