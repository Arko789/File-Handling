#WAF to read a text file happy.txt & copy all the words starting with 's' to
#another file sad.txt

r'''def copy():
    f=open(r"C:\Users\user\Documents\File Handling\Text\newstuff.txt",'r')
    s=f.read()
    l=s.split()
    s=''
    for i in l:
        if i[0]=='s':
            s=s+' '+i
    f.close()
    f=open('sad.txt','w')
    f.write(s)
    f.close()
copy()'''

def read_copy():
    obj1=open(r"C:\Users\user\Documents\File Handling\Text\newstuff.txt",'r')
    obj2=open('capital.txt','w')
    #s=obj1.readlines()
    for i in obj1:
        if i[0].isupper():
            obj2.write(i)
    obj1.close()
    obj2.close()
            
read_copy()
