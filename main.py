from art import logo , vs
from game_data import data



import random as rn


def checkWhoHasMore(compare , against):
    if compare > against:
        return 'a'
    else:
        return 'b'    


score = 0
against = rn.choice(data)
gameContinue = True

print(logo)


while gameContinue:
    compare = against
    against = rn.choice(data)

    if compare == against:
        against = rn.choice(data)
    
    print(f"Compare A: {compare['name']} , a {compare['description']} from {compare['country']} .")
    print(vs)
    print(f"Against B: {against['name']} , a {against['description']} from {against['country']} .")

    choice = input('Who has more followers? \'A\' or \'B\' : ').lower()

    whoHasMore = checkWhoHasMore(compare['follower_count'] , against['follower_count'])


    if choice == whoHasMore:
        score = score + 1
        print(f"You are right! current score: {score}")
    else:
        gameContinue = False
        print(f"You are wrong! final score: {score}")    







