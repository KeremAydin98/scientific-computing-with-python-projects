import random

def Hat(yellow=0, green=0,
        orange=0, black=0, blue=0, pink=0, striped=0, red = 0):


    hat = {"yellow": yellow, "green" : green, "orange": orange, "black": black, "blue" : blue,
           "pink": pink, "striped":striped, "red":red}

    return hat


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

    n_occurred = 0

    for experiment in range(num_experiments):

        copy_hat = hat.copy()

        balls_drawn = dict()

        for drawn in range(num_balls_drawn):

            choice = random.choice(list(copy_hat.keys()))

            while copy_hat[choice] == 0:
                choice = random.choice(list(copy_hat.keys()))

            copy_hat[choice] = copy_hat[choice] - 1

            balls_drawn[choice] = balls_drawn.get(choice, 0) + 1

        occurred = True

        for key in balls_drawn.keys():

            if key not in expected_balls.keys():
                continue

            if balls_drawn[key] != expected_balls[key]:

                occurred = False

        if occurred:
            n_occurred += 1

        print(f"Number {experiment} experiment out of {num_experiments} has been done")

    return n_occurred / num_experiments




