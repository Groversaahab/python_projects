import random

def quizer(question, answer, score):
    print(question)
    user_answer = input()
    if user_answer in answer:
        print("Correct Answer!!")
        print("Score + 1")
        score += 1
    else:
        print("Wrong Answer :(")

def question_chooser(user_num, question_num):
    rand_nums = []
    for i in range(user_num):
        rand_num = random.randint(0, question_num-1)
        while rand_num in rand_nums:
            rand_num = random.randint(0, question_num-1)
        rand_nums.append(rand_num)
    return rand_nums

def user_num_check(user_num):
    if user_num == 0:
        print("A smart one aren't you, anyway thanks for your time")
    elif user_num not in range(1, 10):
        print("Score = -1, a dumb one aren't you choose between 1, 2, 3, 4, 5, 6, 7, 8, 9, 10")
        user_num = input()
        user_num_check(user_num)
    try:
        user_num = int(user_num)
    except:
        print("Write a number between 1 and 10 including 1 and 10")


print("Welcome to my quiz!!!")
print("Type name to start")
name = input()
print(f"Hi {name}!!")
print("Please read these rules:(press enter after reading the rule)")
print("1. For each correct answer you get +1 point.", end="")
input()
print("2. For each wrong answer you get +0 point", end="")
input()
print("3. After answering any question you may raise a query by using the following codes:")
print("'score' for your current score")
print("'protest' if you think your answer is correct")
print("'answer' for answer list")
print("'repeat' if you want to try again the same question")
print("No other code is supported, submiting any other text will automatically load the next question", end="")
input()
print("4. A repeated question gets half the points")
input()
print("Thats all for the rules, please choose the number of question between 1 and 10")
user_num = input()
user_num_check(user_num)
print("Let the Games Beginn!!!")
question_numbers = question_chooser(user_num, 10)
