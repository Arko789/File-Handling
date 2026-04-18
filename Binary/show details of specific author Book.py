def CountRec(Author):
    f=open('Book.dat','rb')
    x=pickle.load(f)
    if x[2]=='Author':
        c=c+1
        print('Book No: ',x[0])
        print('Booko Name: ',x[1])
        print('Book Price: ',x[3])
    f.close()

CreateFile()
show_all_books()
a=input('Enter the name of the author: ')
d=CountRec(a)
print('No. of books writeen by',a,'=',d)
