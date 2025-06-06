#Create a program capable of displaying questions to the user like KBC. 
# Use List data type to store the questions and their correct answers. 
# Display the final amount the person is taking home after playing the game.

= input("Enter your name for playing KBC: ")
print("Welcome To KBC,", name)
print("Let's Start the Quiz!")
print("Answer carefully. Type A, B, C, or D as your answer.\n")

# Questions, Options, and Answers
Questions = [
    "1. What is the class of Frog?",
    "2. What is the easiest programming language to learn?",
    "3. Who owns Tesla?"
]

Options = [
    ["A. Mammal", "B. Reptile", "C. Bird", "D. Amphibian"],
    ["A. C++", "B. Python", "C. Java", "D. Javascript"],
    ["A. Narendra Modi", "B. Bill Gates", "C. Tim Cook", "D. Elon Musk"]
]

# Correct Answers corresponding to the options
Answers = ["D", "B", "D"]
Prize_Money = [5000, 10000, 50000]

total = 0
for i in range(len(Questions)):
    print("\n" + Questions[i])
    for option in Options[i]:
        print(option)
    answer = input("Your answer (A/B/C/D): ").strip().upper()
    
    if answer == Answers[i]:
        print("✅ Correct! You've won ₹", Prize_Money[i])
        total = Prize_Money[i]
    else:
        if i == 0:
            print("❌ Wrong answer! You're taking home ₹0")
        else:
            print("❌ Wrong answer! You're taking home ₹", Prize_Money[i-1])
        break
else:
    print("\n🎉 Woohoo", name + "!", "You completed the game and won ₹", total)

print("\nThank you for playing KBC, " + name + "!")

