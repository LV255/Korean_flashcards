import random

chosen_to_study = None
english_or_korean = None


def intro():
    global chosen_to_study
    global english_or_korean
    print("Can you understand the word? press any key to see the answer, then press any key to see the next word.")

    # choose the cards you want to study
    print("""Welcome to flashcards.
    What would you like to study?
    (1) Korean numbers
    (2) Korean months and days of the week
    (3) 10 basic Korean phrases""")
    list_choice = input("Please type (1/2/3) and press enter: ").lower().strip()
    if list_choice == "1":
        chosen_to_study = korean_numbers
    elif list_choice == "2":
        chosen_to_study = korean_months_days
    elif list_choice == "3":
        chosen_to_study = korean_words
    else:
        print("Sorry, input not recognised.") 
        intro()

    # decide on English fisrt or Korea first
    print("""To view english first type e.
To view Korean first type k.""")
    e_or_k = input("Please type (e/k) and press enter: ").lower().strip()
    # print("Are you ready to begin? Please any key to continue")
    # input("")
    if e_or_k == "e":
        english_or_korean = "english"
    elif e_or_k == "k":
        english_or_korean = "korean"
    else:
        print("Sorry, input not recognised.")
        intro()

    # start studying
    begin_study()

# lists that you can study in this version
# careful there is not an empty last line!
korean_numbers ="""1, 하나 
2, 둘 
3, 셋 
4, 넷 
5, 다섯 
6, 여섯 
7, 일곱 
8, 여덟 
9, 아홉
10, 열"""

korean_months_days ="""Monday, 월요일 
Tuesday, 화요일 
Wednesday, 수요일 
Thursday, 목요일 
Friday, 금요일 
Saturday, 토요일 
Sunday, 일요일 
January, 일월
February, 이월
March, 삼월
April, 사월
May, 오월
June, 유월
July, 칠월
August, 팔월
September, 구월
October, 시월
November, 십일월
December, 십이월"""

korean_words ="""Hello, 안녕하세요 
Please, 주세요 
Sorry, 죄송합니다 
Thank you, 고맙습니다 
Yes, 네 
No, 아니요 
Maybe, 아마도 
Have you eaten?, 밥 먹었어요? 
Help, 도와 주세요
I don’t know, 몰라요"""

def begin_study():
    study_object = chosen_to_study.split("\n")

    if english_or_korean == "english":
        # display cards while there are cards stick in the list
        while len(study_object) > 0:
            # choose a random card
            # len decrease as cards are studying and removed
            chooserandomitem = random.randint(0, (len(study_object)-1))

            # display the front of the card
            randomword = study_object[chooserandomitem].split(",")
            print(randomword[0].strip(), end = " ")
            input()

            # display the back of the card
            print(randomword[1].strip())
            # remove the card that has just been studied
            study_object.pop(chooserandomitem)
            input()

        print("completed")
        play_again()

    # as above but with Korea on the front of the card
    elif english_or_korean == "korean":
        while len(study_object) > 0:
            chooserandomitem = random.randint(0, (len(study_object) - 1))

            randomword = study_object[chooserandomitem].split(",")
            print(randomword[1].strip(), end=" ")
            input()
            print(randomword[0].strip())
            study_object.pop(chooserandomitem)
            input()

        print("completed")
        play_again()

# function to play again after all cards are seen
def play_again():
    again = input("Play again? (y/n)").strip().lower()
    if again == "y":
        intro()
    else:
        play_again()

# starting function
intro()