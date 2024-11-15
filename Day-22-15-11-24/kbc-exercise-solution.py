# Object -> Dictionary in python
# Array -> List in python

questions = [["Which language was used to create Swageazy", "Python", "JavaScript", "Php", "None", "Java", 2], ["Which language was used to create Swageazy", "Python", "JavaScript", "Php", "None", "Java", 2], ["Which language was used to create Swageazy", "Python", "JavaScript", "Php", "None", "Java", 2]]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]

for i in range(0, len(questions)):
    question = questions[i]
    print(f"Question for Rs. {levels[i]}")
    