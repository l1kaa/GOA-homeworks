# 1. შექმენი ფუნცია, სადაც არგუმენტად გადასცემ ორ რიცხვს, შემდეგ დაპრინტე ამ ორი რიიცხვის განაყოფი.
def division(num1,num2):
    return num1 / num2

# 2. შექმენი ფუნქცია, სადაც არგუმენტად გადასცემ სახელს, შემდეგ დაპრინტე მისალმების მესიჯი, სადაც ამ სახელს გამოიყენებ.
def greet(name):
    print("hello", name)
greet("lika")

# 3. შექმენი ფუნქცია, სადაც არგუმენტად გადასცემ დაბადების თარიღს, შემდეგ დაპრინტე თუ რამდენი წლისაა მომხმარებელი.
def age(date):
    date = int(input("enter your birth year"))
    print(2024 - date)

# 4. შექმენი ფუნქცია, სადაც არგუმენტად გადასცემ რიცხვ, შემდეგ დაპრინტე ეს რიცხვი გამრავლებული 5-ზე.
def num(number):
    print(num * 5)

# 5. შექმენი ფუნქცია, სადაც პირველ არგუმენტად input()-ის გამოყენებით გადასცემ ასაკს, მეორე არგუმენტად კი input()-ის გამოყენებით გადასცემ სახელს, შემდეგ დაპრინტე, თუ რა ქვია მომხმარებელს და რამდენი წლის არის ის
def user(username,user_age):
    username = input("what's your name?: ")
    user_age = int(input("what's your age?: "))
    print("user's name is ", username, "and user's age is ", user_age)


# bonus exercises:
# 6. შექმენი ფუნქცია, რომელსაც არგუმენტად გადასცემ რიცხვს (სტრინგად), შემდეგ ფუნქციაში გადაქციე ეს სტრინგი ინტეჯერად, და დაპრინტე მასზე 5-ჯერ მეტი რიცხვი.
def numm(number):
    number = int(number)
    return number * 5
print(numm)


# 7. შექმენი ფუნქცია, რომელსაც არგუმენტად გადასცემ სამ რიცხვს, შემდეგ დაპრინტე ამ სამი რიცხვის ნამრავლი, განაყოფი, სხვაობა, ჯამი.
def nums(num1, num2, num3):
    print(num1 * num2 * num3)
    print(num1 / num2 / num3)
    print(num1 - num2 - num3)
    print(num1 + num2 + num3)
nums(100, 200, 300)


# 8. შექმენი ფუნქცია, რომელსაც არგუმენტად გადასცემ 5 ელემენტიან სიას, შემდეგ დაპრინტე ამ სიის მე-3 ინდექსზე მყოფი ელემენტი.
def list (list = [1,2,3,4,5]):
    print(list[3])
print(list)


# 9. შექმენი ფუნცია, რომელსაც პირველ არგუმენტად გადასცემ 5 ელემენტიან სიას, ხოლო მეორე არგუმენტად გადასცემ რაიმე რიცხვს, შემდეგ დაპრინტე ამ სიიდან ის ინდექსი, რომელი რიცხვიც მეორე არგუმენტად გადაეცი.
def find_index(list,index):
    if index in list:
        print(list[index])
    else:
        print("the index is not in the list")


# 10. შექმენი ფუნქცია, რომელსაც არგუმენტად გადასცემ რიცხვს, შემდეგ დაპრინტე 0-იდან ამ რიცხვამდე ყველა რიცხვი, გამოიყენე for loop().
def loop(number):
    for i in range(0,number):
        print(i)
    