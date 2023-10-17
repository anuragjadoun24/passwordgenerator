#DESIGN A PASSWORD GENERATOR IN PYTHON [TASK 3]
import random
letters=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","!","@","#","$","%","^","&","*","(",")","+","-"]
print("WELCOME TO THE PASSWORD GENERATOR")
n_length=int(input("WHAT LENGTH DO YOU WANT IN YOUR PASSWORD??"))
password=""
for i in range(1,n_length+1):
    char=random.choice(letters)
    password=password+char
print(password)    