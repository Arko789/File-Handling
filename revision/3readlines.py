with open ("E.txt",'r') as obj:
    x=obj.read(2)
    t=obj.readline(1)
    y=obj.readlines()
    print(x,t,y)