# List Functions:

# 1. შექმენით სია, 5 რიცხვით, შემდეგ დაპრინტეთ ამ სიაში შემავალი რიცხვების ჯამი.
numbers = [100, 560, 98440, 7884, 89]
print(sum(numbers))

# 2. შექმენით სია, 5 რიცხვით, შემდეგ დაპრინტეთ ამ სიაში შემავალი რიცხვებიდან უდიდესი.
numbers = [100, 560, 98440, 7884, 89]
print(max(numbers))

# 3. შექმენით სია, 5 რიცხვით, შემდეგ დაპრინტეთ ამ სიაში შემავალი რიცხვებიდან უმცირესი.
numbers = [100, 560, 98440, 7884, 89]
print(min(numbers))

# 4. შექმენით სია, 5 რიცხვით, შემდეგ დაპრინტეთ ამ სიის სიგრძე.
numbers = [100, 560, 98440, 7884, 89]
print(len(numbers))

# 5. შექმენით სია, 5 სტრინგით, შემდეგ .append()-ის მეშვეობით სიის ბოლოში დაამატეთ სასურველი სიტყვა.
items = ["headphones", "microphone", "mousepad", "PC", "disk"]
items.append("headset")

# 6. შექმენით სია, 5 სტრინგით, შემდეგ .insert()-ის მეშვეობით სიაში სასურველ ინდექსზე დაამატეთ სასურველი სიტყვა.
subjects = ["math", "english", "science", "biology", "IT"]
subjects.insert(3, "history")

# 7. შექმენით სია, 5 სტრინგით, შემდეგ .pop()-ის მეშვეობით სიიან ამოაგდეთ ინდექსის მეშვეობით რომელიმე სიტყვა.
lessons = ["lesson 0", "lesson 1 ", "lesson 2", "lesson 3", "lesson 4"]
lessons.pop(4)