students= [{'names': 'Paul', 'ages': 20, 'genders':'Males', 'G1': 15, 'G2': 14, 'G3':16},
           {'names': 'Mary', 'ages': 27, 'genders': 'Females', 'G1':12, 'G2': 13, 'G3':14},
           {'names': 'John', 'ages': 23, 'genders': 'Males', 'G1': 10, 'G2': 11, 'G3': 12},
           {'names': 'Grace', 'ages': 25, 'genders': 'Males', 'G1': 13, 'G2': 16, 'G3': 18},
           {'names': 'David', 'ages': 26, 'genders':'Males','G1': 14, 'G2':10, 'G3': 12 },
           {'names': 'Esther', 'ages': 21, 'genders': 'Females', 'G1': 15, 'G2': 16, 'G3':15},
           {'names': 'Mike', 'ages': 19, 'genders': 'Males', 'G1': 13, 'G2': 18, 'G3': 11},
           {'names': 'Sarah', 'ages': 29, 'genders': 'Females', 'G1': 11, 'G2': 17, 'G3':12},
           {'names': 'Bright', 'ages': 24, 'genders': 'Females', 'G1':12, 'G2': 13, 'G3': 12}]
print(students)

# this is the database for now showcasw the lists containing differents dictionaries of students records with repective keys and values

# creates an add_ student  functin
def add_students():
    name= input('enter name :')
    age= int(input('enter age :'))
    gender= input('enter gender:')
    G1= int(input('enter G1 :'))
    G2= int(input('enter G2:'))
    G3= int(input('enter G3:'))

    student= {'names': name,
              'ages': age,
              'genders': gender,
              'G1': G1,
              'G2': G2,
              'G3': G3}
    students.append(student)
    print('students added successfully!')

davis= add_students()
print(davis)

# to create a view students function

def view_student():
    for student in students:
        print('\n----------')
        print(f"Name: {student['names']}")
        print(f"Age: {student['ages']}")
        print(f"Gender:{student['genders']}")
        print(f"G1:{student['G1']}, G2: {student['G2']}, G3: {student['G3']}")

chidi= view_student()
print(chidi)

# search function
def search_student():
    name= input('Enter name to search: ')

    for student in students:
        if student['names'].lower()== name.lower():
            print(student)
            return
        print('student not found')

chika= search_student()
print(chika)


# update information

def update_student():
    name= input('Enter name to update:')
    
    for student in students:
        if student['names']. lower()== name.lower():
            student['ages']= int(input('new age:'))
            student['G3']= int(input('new G3:'))
            print('students record updated successfully')
            return
        print('student not found')
    
new_records= update_student()
print(new_records)


# create a menu list

def menu():
    while True:
        print("\n ==== student recording system ====")
        print("1. Add students")
        print("2. view students")
        print("3. search student")
        print("4. update student")
        print("5. Exit")

        choice= input("Enter your choice")

        if choice == "1":
            add_students()
           
        elif choice == "2":
            view_student()
           
        elif choice == "3":
            search_student()
           
        elif choice== "4":
            update_student()
           
        elif choice== "5":
            print("Good bye !")
            break
        else:
            print("invalid choice")

conclude= menu()
print(conclude)
            



  