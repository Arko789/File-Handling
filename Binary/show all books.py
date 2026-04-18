import pickle
def show_all_books():
    try:
        f=open(r"C:\Users\user\Documents\File Handling\Binary\Book.dat",'rb')
        while True:
            x=pickle.load(f)
            print('Book No: ',x[0])
            print('Booko Name: ',x[1])
            print('Book Author: ',x[2])
            print('Book Price: ',x[3])
        f.close()
    except:
        print('input output error')
show_all_books()
