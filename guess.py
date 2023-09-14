import random as rd

random_num = rd.randint(0, 10)
attempts = 0 
score = 20

while True:
    print("Enter Number = ")
    input_a = int(input())
    attempts += 1  

    if input_a == random_num:
        score = score+5;
        print('Correct Number')
        print(f'Number of attempts: {attempts}')
        print("score = ")
        print(score)
        
        break
    elif input_a > random_num:
        score = score-5
        print("Go lower")
    elif input_a < random_num:
        score = score-5
        print('Go Higher')