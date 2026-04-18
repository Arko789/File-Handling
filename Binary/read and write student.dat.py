#func to get student id,name,age and class in a list and write details of 
#n students in a binary file student.dat
import pickle
def get_details():
        fileobj=open('student.dat','wb')
        n=int(input('Enter no. of students: '))
        st_list=[]
        for i in range(n):
            stid=int(input(f'Enter st{i+1} id: '))
            name=str(input(f'Enter st{i+1} name: '))
            age=int(input(f'Enter st{i+1} age: '))
            stclass=input(f'Enter st{i+1} class: ')
            l=[stid,name,age,stclass]
        return l
            #st_list.append(l)
        pickle.dump(l,fileobj)
        '''for i in fileobj:
                pickle.load(i)'''
        filobj.close()
get_details()
    

'''def write_details(st_list):
    with open('student.dat','wb') as f:
        pickle.dump(st_list,file)

        
import pickle

def get_student_details(n):
    student_list = []
    for i in range(n):
        student_id = input(f"Enter student {i+1} ID: ")
        name = input(f"Enter student {i+1} name: ")
        age = int(input(f"Enter student {i+1} age: "))
        class_ = input(f"Enter student {i+1} class: ")
        student = [student_id, name, age, class_]
        student_list.append(student)
    return student_list

def write_to_binary_file(student_list):
    with open('student.dat', 'wb') as file:
        pickle.dump(student_list, file)

n = int(input("Enter the number of students: "))
student_list = get_student_details(n)
write_to_binary_file(student_list)
'''
