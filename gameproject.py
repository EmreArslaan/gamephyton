def give_options(x,y,z):
    print("a):", x)
    print("b):", y)
    print("c):", z)
    
print("Hello! Welcome to my Quiz" "\n" "All Questions carries 10 marks each")
ans = input("Are you ready to play (yes/no): ")
a ="Note: wrtie answers! do not write option."
score = 0
total_questions = 4

correct_ans =["python", "audi", "youtube", "albert einstein "]

if ans.lower() == "yes":
    print(a)
    print("Question- What is the best Programming Language? ")
    give_options("Python", "C", "Java" )
    ans=input("&gt;&gt;&gt;")
    if ans.lower() == correct_ans[0]:
        score=score+1
        print("Correct")
