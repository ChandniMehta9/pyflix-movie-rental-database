import csv
import os

def discount():
    global total
    print("Congratulations! As you have purchased or rented more than 5 movies, you are eligible for a discount of 25%")
    res= input("To apply this discount on your purchase, please press A(or a) on your keyboard: ")
    if res.lower()=="a":
        flag1="green"
    if flag1=="green":
        total= total*(0.25)
    print()

def userinput():
    with open('movies.csv','a',newline='') as c1:
        mw=csv.writer(c1)
        n=eval(input('number of recommedations'))
        for i in range(n):
            mr=[]
            genre=input('enter genre of movie= ')

            name=input('enter name of movie= ')

            age=input('enter age rating= ')

            actor=input('enter main actor= ')

            actor2=input('enter supporting actor= ')
            link='https://fmovies.to/film.jv58'

            mr.extend([genre,name,age,actor,actor2,link])

            mw.writerow(mr)

    c1.close()
    print()
        
a=input('Are you a first time customer? (y/n): ')
print()
if a.lower()=='y':
    f=open('userdatabase.csv','r')
    f1=open('userdatabase1.csv','w', newline='')
    w=csv.writer(f1)
    r=csv.reader(f)
    for i in r:
        w.writerow(i)
    print('Welcome to PyFlix!')
    print('This is your one-stop gateway to a plethora of movies that you can enjoy, right from the comfort of your home.')
    print()
    
    print('Please provide us with the following details so that we can register you as a member under PythonFlix')
    fn=input('First Name: ')
    ln=input('Last Name: ')
    print()
    dob=[]
    a=eval(input('date of birth(D/DD): '))
    b=eval(input('month of birth: '))
    c=eval(input('year of birth: '))
    dob.extend([a,b,c])
    print()
    id=input('Valid Email-id: ')
    while True:                       #Valid Phone No
        no=input('Phone No: ')
        if len(no)==10:
            break
        else:
            print('invalid phone number')
    print()
    pa=input('enter password: ')
    while True:                      #password=confirm password
        cp=input('confirm password: ')
        if pa==cp:
            break
        else:
            print('incorrect password: ')
    rn=0
    amt=0
    w.writerow([fn,ln,dob,id,pa,no,rn,amt])
    f.close()
    f1.close()
    os.remove('userdatabase.csv')
    os.rename('userdatabase1.csv','userdatabase.csv')
elif a.lower()=='n':
    print('Welcome back to PyFlix! Enter your login details below to get started.')
    f=open('userdatabase.csv','r')
    r=csv.reader(f)
    id=input('Enter id: ')
    for i in r:
        if i[3]==id:
            while True:
                pa=input('Enter password: ')
                if i[4]==pa:
                    print()
                    print('You have succesfully signed in')
                    
                    break
                else:
                    print('Incorrect password')
'''0569900651     348490'''
f.close()
print()

import csv

with open("movies.csv","r") as c1:
    r=csv.DictReader(c1,delimiter=',')
    l=[]
    line=0
    for i in r:
        if line!=0:
            l.append(i)
        line+=1
    f1=input('Would you like to add filters? (y/n)')
    if f1=='y':
        while True:
            f2=eval(input('Choose the filter of your choice: 1-genre, 2-main actor, 3-supporting actor, 4-no other filter: '))
            print()
            if f2==1:
                l1=[]
                f3=input('Enter a genre from the following:-Action, Sci-fi, Thriller, Rom-com, Coming of age, Feel-good:')
                for i in l:
                    if i['Genre']==f3:
                        l1.append(i)
                        l=l1
                print()
            elif f2==2:
                l3=[]
                f5=input('Enter a main actor of your choice: ')
                for i in l:
                    if i['Main actor']==f5:
                        l3.append(i)
                        l=l3
                print()
            elif f2==3:
                l4=[]
                f6=input('Enter a supporting actor: ')
                for i in l:
                    if i['supporting actor']==f6:
                        l4.append(i)
                        l=l4
                print()
            elif f2==4:
                break
            else:
                break
            
print('Here is the list of filtered movies: ')
print()
for i in l:
    print(i['Name'])
print()
s1=input("Please enter the names of the movie you would like: ")

pay=0
rent=0
print()

rob=input("If you would like to buy the movie. please enter 'b'. If you wish to rent it, enter 'r'.")
if rob=='r':
    rent+=10
    print('Kindly note that the rented movie link will only be valid for 7 days.')
if rob=='b':
    pay+=20


total= pay+rent
print('Here is the link to your movie. Enjoy!')
for i in l:
    if i['Name']==s1:
        print(i['Name'],':',i['Link'])
print()    

with open("userdatabase.csv","r") as c1:
    r=csv.reader(c1)
    with open("userdatabase1.csv","w",newline="") as c2:
        w=csv.writer(c2)
        line=0
        for i in r:
            if line!=0:
                if i[3]==id:
                    if int(i[6])>5:
                        discount()
                    i[6]=int(i[6])+1
                    i[7]=float(i[7])+total
            line+=1
            w.writerow(i)
print('The amount to be paid has been added to your tab successfully.')
print()
c2.close()
c1.close()
u=input('Before you go, would you like to reccomend any movies to be added to PyFlix? (y/n)')
if u=='y':
    userinput()
else:
    print('Thank You for using PyFlix! Now sit back, grab some popcorn and enjoy the movie!')
    
os.remove("userdatabase.csv")
os.rename("userdatabase1.csv","userdatabase.csv")
