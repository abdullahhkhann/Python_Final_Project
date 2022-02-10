# Greet the user!

print("Welcome!!")

# Ask for the user's information

name = input("What is your full name? ")
age = eval(input("What is your age?(18+): "))
email = input("E-mail address: ")
print("Answer the next question with a yes or no")
user_conf = input("Do you want to share your address to recieve gift packages? (Gift packages are sent if you complete a long term goal!): ")

# Check for address condition

if user_conf == "yes":
    address = input("Enter your address: ")
    print("Thank you, let's get started!!")
elif user_conf == "no":
    print("Thank you, let's get started!!")
else:
    print("Invalid response, please answer with a yes or no.")
    
# Understanding the user's body type to give them specific schedules

print("Body types: Ectomorph(lean and long), Endomorph(big and high body fat), Mesomorph(High metabolism and well-built)")
body_type = input("What is your body type? Pick a, b, or c: (a: Ectomorph, b: Endomorph, c: Mesomorph): ")
if body_type == "a":
    print("Keep your workouts 3-4 days per week and limit yourself to 45 minute sessions to see optimal results!")
elif body_type == "b":
    print("Keep your workouts 3-5 days per week, limit yourself to 60 minute sessions, keep active throught the week for optimal results!")
elif body_type == "c":
    print("Keep your workouts 3-5 days per week and limit yourself to 30-45 minute sessions for optimal results!")
else:
    print("Invalid choice, please enter a, b, or c")

# Calorie intake and sleep schedule for the different age ranges

print("Now we move onto specific diet and sleep plans for your specific age range!!")
print("Please pick a, b, or c")
age_range = input("Which range does your age lie in? (a:18-27), (b:28-37), (c:38 and above): ")
if age_range == "a":
    print("If you are moderately active, calorie intake: 2800 cal. and sleep from 7-11 hours!")
    print("If you are active, calorie intake: 3000 cal. and sleep from 7-11 hours!")
elif age_range == "b":
    print("If you are moderately active, calorie intake: 2600 cal. and sleep from 6-10 hours!")
    print("If you are active, calorie intake: 3000 cal. and sleep from 6-10 hours!")
elif age_range == "c":
    print("If you are moderately active, calorie intake: 2000-2500 cal. and sleep from 5-9 hours!")
    print("If you are active, calorie intake: 2400-3000 cal. and sleep from 5-10 hours!")
else:
    print("Invalid response, please pickk a, b, or c.")

# Conclusion

print("Stay motivated and keep record of your progress!!")
print("Each new day is a new opportunity to improve yourself, take it and make the most out of it!!!")
print("Thank you for taking a step to living a healthier life during this pandemic with us!!")