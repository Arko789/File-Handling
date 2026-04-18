def read_content():
    try:
        obj=open('new.txt','r')
        st=obj.read()
        print(st)
    except FileNotFoundError :
        print('Error')
read_content()
