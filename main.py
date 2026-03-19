from generate_questions import questions    # Imports questions from separate module

# Main program
# Loops questions until an incorrect answer
print("Welcome to the Quiz 🧠")
print("Answer as many questions as you can! 🙋‍♂️")

score = 0 

while True:
    num_1, num_2, operator, result = questions()
    message = f"What is {num_1} {operator} {num_2}?" 
    print(message)
    user_answer = int(input("Your answer: "))

    if user_answer == result:
            print("✅ Well Done! That is Correct")
            score += 1
    else:
         print(f"❌ Bad Luck, that's incorrect, the correct answer was {result}")
         break

print(f"    🏁 GAME OVER 🏁")
print(f"You achieved a score of {score}")