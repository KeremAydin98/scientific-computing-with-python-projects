def arithmetic_arranger(problems, condition=False):
    arranged_problems = []

    if len(problems) > 5:

        print("Error: Too many problems.")
        quit()

    for problem in problems:

        objects = problem.split()

        try:
            first_number = int(objects[0])

            second_number = int(objects[2])

        except:

            print("Error: Numbers must only contain digits.")
            quit()

        operation = str(objects[1])

        if operation == "+":

            result = first_number + second_number

        elif operation == "-":

            result = first_number - second_number

        else:

            print("Operation must be either + or -")
            quit()

        numbers = [first_number, second_number, result]
        counts = []

        for number in numbers:

            count = 0

            while number >= 1:
                number /= 10
                count += 1

            if count <= 4:
                counts.append(count)
            else:
                print("Error: Numbers cannot be more than four digits.")
                quit()

            max_len = max(counts)

        space = " "
        line = "-"

        n_spaces = [abs(max_len - counts[0]) + 1, abs(max_len - counts[1]) + 1]

        if condition:

            arranged_problem = space * (n_spaces[0] + 1) + str(first_number) + "\n" \
                               + operation + space * n_spaces[1] + str(second_number) + "\n" \
                               + line * (max_len + 2) + "\n" + space * abs(max_len - counts[2] + 2) + str(result)

            arranged_problems.append(arranged_problem)

        else:

            arranged_problem = space * (n_spaces + 1) + str(first_number) + "\n" \
                               + operation + space * (n_spaces - 1) + str(second_number) + "\n" \
                               + line * (n_spaces + max_len + 1)

            arranged_problems.append(arranged_problem)

    return arranged_problems


arranged_problems = arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], condition=True)

length = len(arranged_problems)

for i in range(length):

    print(arranged_problems[i])
    print("\n")





