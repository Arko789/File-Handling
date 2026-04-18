def count_chars():
    try:
        with open(r"C:\Users\user\Documents\File Handling\Text\newstuff.txt",'r') as file:
            content = file.read()
            count_s = content.count('s')
            count_i = content.count('i')
            print(f"Number of 's' in newstuff:", count_s)
            print(f"Number of 'i' in newstuff:", count_i)
    except FileNotFoundError:
        print(f"File {filename} not found.")

count_chars()

r'''

def count_char():
    with open(r"C:\Users\user\Documents\File Handling\Text\newstuff.txt",'r') as f:
        x=f.read()
        c=d=0
        for i in x:
            if i=='s':
                c+=1
            if i=='i':
                d+=1
    print(f"Number of 's' in newstuff:", c)
    print(f"Number of 'i' in newstuff:", d)
count_char()
'''
