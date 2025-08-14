import random
NUM_PROBLEMS = 5
score = 0

print("Welcome to the multiplication quiz!")
print(f"You will be given {NUM_PROBLEMS} problems to solve")

for i in range(NUM_PROBLEMS):
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)

    # keep asking until user gives a valid integer
    while True:
        user_input = input(f"Problem {i+1}: {num1} x {num2} = ")
        if user_input.strip().isdigit():
            user_answer = int(user_input)
            break
        else:
            print("Please enter a valid integer.")

    # check correctness
    if user_answer == num1 * num2:
        print("✅ Correct!\n")
        score += 1
    else:
        print("Incorrect!. The correct answer was {num1 * num2}.\n")

# final score
print(f"Your score is {score} out of {NUM_PROBLEMS}")
print("Thanks for playing!")







