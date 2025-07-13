import openpyxl
import openpyxl.workbook
import os

class question:
    def __init__(self, ques: str, ans:list, genre: str, difficulty: str, neg_mark: bool):
        self.question = ques
        self.answer = ans
        self.genre = genre
        self.difficulty = difficulty
        self.neg_mark = neg_mark

    def points(dif:str):
        if dif == "hard":
            return 3
        elif dif == "medium":
            return 2
        else:
            return 1

def intro() -> list:
    print("Hi, welcome to quiz maker")
    print("Please fill the asked questions appropriately:")
    print("Name:", end=" ")
    user_name = input()
    print("Genre of the quize you wanna make:(mix for multiple genre)", end=" ")
    quiz_genre = input()
    print("What is the title of your quiz?", end=" ")
    quiz_title = input()
    print("Difficulty of your quiz:(mix for multiple difficulty questions)", end=" ")
    quiz_difficulty = input()
    print("Do you want to specify difficulty rating of each question?(y/n)", end=" ")
    quiz_question_difficulty = input()
    return [user_name, quiz_genre, quiz_title, quiz_difficulty, quiz_question_difficulty]

def excel_file_initialising(user_name: str):
    xlfile = openpyxl.workbook()
    xlfile.save(f"./quiz_data/{user_name}.xlsx")

def excel_file_format(xlsheet, custom_dif, quiz_genre, quiz_difficulty):
    h1 = ["Quiz Genre", "Quiz difficulty", "Custom question difficulty"]
    if custom_dif:
        h2 = ["Question", "Question difficulty", "Points", "Genre", "Negative marking", "Answer"]
        p1 = [quiz_genre, quiz_difficulty, "Yes"]
    else:
        h2 = ["Question", "Points", "Genre", "Negative marking", "Answer"]
        p1 = [quiz_genre, quiz_difficulty, "No"]
    
    for i in range(len(h1)):
        xlsheet.cell(row=1, column=(i+1)).value = h1[i]
        xlsheet.cell(row=2, column=(i+1)).value = p1[i]
    for i in range(len(h2)):
        xlsheet.cell(row=4, column=(i+1)).value = h2[i]

def quistion_maker(custom_dif: bool, quiz_difficulty: str, quiz_genre: str) -> question:
    pass

def main():
    [user_name, quiz_genre, quiz_title, quiz_difficulty, custom_question_difficulty] = intro()
    if custom_question_difficulty == "y":
        custom_question_difficulty = True
    else:
        custom_question_difficulty = False

    if os.path.exists(f"./quiz_data/{user_name}.xlsx"):
        xlfile = openpyxl.load_workbook(f"./quiz_data/{user_name}.xlsx")
        sheet = xlfile.create_sheet(title=quiz_title)
    else:
        excel_file_initialising(user_name)
        xlfile = openpyxl.load_workbook(f"./quiz_data/{user_name}.xlsx")
        sheet = xlfile.active
        sheet.title = quiz_title
    
    excel_file_format(sheet, custom_question_difficulty, quiz_genre, quiz_difficulty)


if __name__ == "__main__":
    main()