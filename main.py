import art
import data_bank
import random
from os import system, name

print(len(data_bank.data))
print(random.randint(0,len(data_bank.data)))
def clear():
    # for windows the name is 'nt'
    if name == 'nt':
        _ = system('cls')

    # and for mac and linux, the os.name is 'posix'
    else:
        _ = system('clear')
def draw_person():
    person_dict = {}
    person_dict = data_bank.data[random.randint(0,len(data_bank.data))]
    print(person_dict)
    return person_dict
def check_person (dict_person_A, dict_person_B):
    if dict_person_A.get("name") == dict_person_B.get("name"):
        return True
    else:
        return False
def compare (dict_person_A, dict_person_B):
    print(f"Person A {dict_person_A.get('name')} has {dict_person_A.get('follower_count')} followers and "
          f"Person B {dict_person_B.get('name')} has {dict_person_B.get('follower_count')} followers ")
    if dict_person_A.get("follower_count") > dict_person_B.get("follower_count"):
        return dict_person_A
    elif dict_person_A.get("follower_count") < dict_person_B.get("follower_count"):
        return dict_person_B
    else:
        return False

def choice_transform(user_choice, dict_person_A, dict_person_B):
    if user_choice == "A":
        return dict_person_A
    elif user_choice == "B":
        return dict_person_B
    else:
        return False

person_A = draw_person()
person_B = draw_person()
score = 0
user_choice = ''
print(art.logo)
end_game = 0

while not end_game:
    while check_person(person_A, person_B):
        person_B = draw_person()

    print(f"Compare A {person_A.get('name')}, {person_A.get('description')}, from {person_A.get('country')}")
    print(art.vs)
    print(f"Against B {person_B.get('name')}, {person_B.get('description')}, from {person_B.get('country')}")
    user_choice = input("Who has more followers? Type A or B").upper()
    if choice_transform(user_choice, person_A, person_B) == compare(person_A, person_B):
        score += 1
        print(f"You are right! Your current score is {score}")
        person_A = person_B
        person_B = draw_person()
        clear()
    else:
        print("Sorry, you are wrong")
        end_game = 1
        print(f"Your score is {score}")

#TODO 1 set score
#TODO 2 draw first person
#TODO 3 draw second person
#TODO 4 compare
#TODO 4 if ok continue, if nok end game
#TODO 5 second person becomes first person and TODO 3



