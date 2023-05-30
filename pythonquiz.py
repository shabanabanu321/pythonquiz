print("WELCOME TO PYTHON QUIZ!!!")
playing=input("DO YOU WANT TO PLAY !!")
if playing.lower()!="yes":
    quit()
print("OKAY!!LETS PLAY!!")
score=0
answer=input("who developed python?")
if answer.lower()=="guido van rossum" :
    print("Correct answer!")
    score=score+1
else:
    print("incorrect answer!")
answer=input("what is the correct extension of python file?")
if answer.lower()==".py" :
    print("the second answer is correct")
    score+=1
else:
    print("incorrect answer")
answer=input("what are the subprograms that are used to specific task ?")
if answer.lower()=="functions" :
    print("the third answer is correct")
    score+=1
else:
    print("incorrect answer")
answer=input("Which one is NOT a legal variable name??")
if answer.lower()=="my-var " :
    print("the fourth answer is correct")
    score+=1
else:
    print("incorrect answer")
answer=input("Which method can be used to remove any whitespace from both the beginning and the end of a string?")
if answer.lower()=="strip()" :
    print("the fivth answer is correct")
    score+=1
else:
    print("incorrect answer")
answer=input("Which statement is used to stop a loop?")
if answer.lower()=="(break)" :
    print("the sixth answer is correct")
    score+=1
else:
    print("incorrect answer")
answer=input("What is the correct syntax to output the type of a variable or object in Python?")
if answer.lower()=="print(type(x))" :
    print("the seventh answer is correct")
    score+=1
else:
    print("incorrect answer")
answer=input("What is the correct way to create a function in Python?")
if answer.lower()=="def myFunction()" :
    print("the eigth answer is correct")
    score+=1
else:
    print("incorrect answer")
answer=input("Which collection is ordered, changeable, and allows duplicate members?")
if answer.lower()=="list" :
    print("the ninth answer is correct")
    score+=1
else:
    print("incorrect answer")
answer=input("Which method can be used to return a string in upper case letters?")
if answer.lower()=="upper()" :
    print("the tenth answer is correct")
    score=+1
else:
    print("incorrect answer")
print("you got"+str(score)+" question correct")
print("you have got :"+str((score/10)*100)+"%")
