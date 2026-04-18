#WAF CreateFile() to input data for a record and add to Book.dat
# [BookNo,Book_Name, Author,Price]
import pickle
def CreateFile():
    try:
        f=open('Book.dat','wb')
        while True:
            BookNo=int(input('Enter book no.: '))
            Book_Name=input('Enter book name: ')
            Author=str(input('Enter author name: '))
            Price=int(input('Enter price: '))
            l=[BookNo,Book_Name, Author,Price]
            pickle.dump(l,f)
            ch=input('Enter Y to continue and N to stop ')
            if ch=='N':
                break
        f.close()
    except:
        print('Some Error')
CreateFile()
