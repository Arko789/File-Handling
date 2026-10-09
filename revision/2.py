"waf to get n lines from user and write these lines in a text file new.txt"

def write_lines():
    n=int(input("Enter number of lines:"))
    with open ("new.txt",'w') as f:
        for i in range(n):
            st=input("Enter lines: ")
            f.write(st+"\n")

write_lines()
