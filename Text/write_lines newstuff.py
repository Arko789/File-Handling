'''def write_lines():
    n=int(input('Enter the no. of lines:'))
    obj=open('newstuff.txt','w')
    for i in range(n):
        st=input('Enter line:')
        obj.write(st+'\n')
    obj.close()
write_lines()'''

def write_lines2():
    n=int(input('Enter the no. of lines:'))
    obj=open('newstuff.txt','w')
    li=[]
    for i in range(n):
        st=input('Enter line:')
        li.append(st+'\n')
    obj.writelines(li)
write_lines2()
