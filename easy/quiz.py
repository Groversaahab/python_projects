import random

total_questions = 10
questions = [0]*10
answers = [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0]]
score = 0
protest_answers = []

def quizer(question_num, questions, answer, score, repeat):
    print(questions[question_num])
    user_answer = input()
    if user_answer in answer[question_num]:
        print("Correct Answer!!")
        print("Score + 1")
        if repeat:
            score += 0.5
        else:
            score += 1
        status = 1
    else:
        print("Wrong Answer :(")
        status = 0

def question_chooser(user_num, total_questions):
    rand_nums = []
    for i in range(user_num):
        rand_num = random.randint(0, total_questions-1)
        while rand_num in rand_nums:
            rand_num = random.randint(0, total_questions-1)
        rand_nums.append(rand_num)
    return rand_nums

def user_num_check(user_num):
    if user_num == 0:
        print("A smart one aren't you, anyway thanks for your time")
    elif user_num not in range(1, total_questions):
        print(f"Score = -1, a dumb one aren't you choose between 1 and {total_questions}")
        user_num = input()
        user_num_check(user_num)
    try:
        user_num = int(user_num)
    except:
        print("Write a number between 1 and 10 including 1 and 10")

def user_query(score, question_num, questions, answers, protest_answers, status):
    print("query: ", end="")
    code = input()
    if code == "score":
        print(f"Current score: {score}")
        print("Any other query? write code: ", end="")
        user_query(score, question_num, questions, answers, protest_answers, status)
    elif code == "protest":
        print("Please repeat your answer")
        print(questions[question_num])
        protest_answers.append([questions[question_num], input()])
        print("Your answer has been recorded for review")
        print("Any other query? write code: ", end="")
        user_query(score, question_num, questions, answers, protest_answers, status)
    elif code == "answer":
        print(answers[question_num])
        print("Any other query? write code: ", end="")
        user_query(score, question_num, questions, answers, protest_answers, status)
    elif code == "repeat":
        if status == 0:
            quizer(question_num, questions, answers, score, 1)
        elif status == 1:
            print("Can't repeat a correctly answered question")
        print("Any other query? write code: ", end="")
        user_query(score, question_num, questions, answers, protest_answers, status)

# ----------Intro------------

print("Welcome to my quiz!!!")
print("Type name to start")
name = input()
print(f"Hi {name}!!")

# ----------Rules-------------

print("Please read these rules:(press enter after reading the rule)")
print("1. For each correct answer you get +1 point.", end="")
input()
print("2. For each wrong answer you get +0 point", end="")
input()
print("3. After answering any question you may raise a query by using the following codes:(press enter to skip query)")
print("'score' for your current score")
print("'protest' if you think your answer is correct")
print("'answer' for answer list")
print("'repeat' if you want to try again the same question")
print("No other code is supported, submiting any other text will automatically load the next question", end="")
input()
print("4. A repeated question gets half the points")
input()

# -----------Number of questions------------

print(f"Thats all for the rules, please choose the number of question between 1 and {total_questions}")
user_num = input()
user_num_check(user_num)            # Checks if the number is valid
# -------------Quiz begins-----------------
print("Let the Games Beginn!!!")
question_numbers = question_chooser(user_num, total_questions)       # Chooses random questions
for i in question_numbers:          # Questions
    status = 0          # Status of the current questions (right or wrong)
    quizer(i, questions, answers, score, 0)         # Asks question, checks answer and updates score
    user_query(score, i, questions, answers, protest_answers, status)           # Query for user
# --------------Outro------------------
print("Thanks for playing")
print(f"Your score is: {score}")