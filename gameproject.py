from operator import lt


def give_options(x,y,z):
    print("a):", x)
    print("b):", y)
    print("c):", z)
    
print("Hello! Welcome to my Quiz" "\n" "All Questions carries 10 marks each")
ans = input("Are you ready to play (yes/no): ")
a ="Note: wrtie answers! do not write option."
score = 8
total_questions = 8

correct_ans =["python", "audi", "yuri gagarin", "naim süleymanoğlu", "brazil", "oxford univercity", "elon musk", "sir ısaac newto"]
if ans.lower() == "yes":
    print(a)
    print("Question- What is the best Programming Language? ")
    give_options("Python", "C", "Java" )
    ans=input("&gt;&gt;&gt;")
    if ans.lower() == correct_ans[0]:
        score=score+1
        print("Correct")
    else:
        print("Incorrect")
        print(a)



    print("Question- which is the german car ? ")
    give_options("Audi", "Ferrari", "Renault" )
    ans=input("&gt;&gt;&gt;")
    if ans.lower() == correct_ans[1]:
        score=score+1
        print("Correct")
else:
    print("Incorrect")
    print(a)


print("Question- first astronaut in space? ")
give_options("yuri gagarin", "alper gezeravcı", "neil armstrong" )
ans=input("&gt;&gt;&gt;")
if ans.lower() == correct_ans[2]:
        score=score+1
        print("Correct")
else:
     print("Incorrect")
     print(a)


print("Question- Who is the world weightlifting champion? ")
give_options("naim süleymanoğlu", "nurcan taylan", "long qingquan" )
ans=input("&gt;&gt;&gt;")
if ans.lower() == correct_ans[3]:
        score=score+1
        print("Correct")
else:
     print("Incorrect")
     print(a)


     print("Question- Which country has won the world cup the most? ")
give_options("brazil", "spain", "germany" )
ans=input("&gt;&gt;&gt;")
if ans.lower() == correct_ans[4]:
        score=score+1
        print("Correct")
else:
     print("Incorrect")
     print(a)


     print("Question- most successful school in the world? ")
give_options("oxford univercity", "harvard univercity", "odtü univercity" )
ans=input("&gt;&gt;&gt;")
if ans.lower() == correct_ans[5]:
        score=score+1
        print("Correct")
else:
     print("Incorrect")
     print(a)


     print("Question- who is the richest person in the world? ")
give_options("elon musk", "jeff bezos", "bernard arnault" )
ans=input("&gt;&gt;&gt;")
if ans.lower() == correct_ans[6]:
        score=score+1
        print("Correct")
else:
      print("Incorrect")
      print(a)


print("Question- Who is the first scientist to discover gravity? ")
give_options("sir ısaac newto", "alessandro Giuseppe antonio anastasio volta", "donald trump" )
ans=input("&gt;&gt;&gt;")
if ans.lower() == correct_ans[7]:
        score=score+1
        print("Correct")
else:
      print("Incorrect")
      print(a)

i = score*10

if i &lt: 30
print("ouch, your score is",i,"/ 40 better")
print("congratulations")
