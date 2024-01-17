'''
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Lukáš Smejkal
email: smejklukas@gmail.com
discord: Razee #6106
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]



line = "-" * 79
double_line = "=" * 79


login = {
    "bob" : "123",
    "ann" : "pass123",
    "mike" : "password123",
    "liz" : "pass123"
}

#greetings

print(double_line)
print()
print("Hello, thank you for using text anylizator 1")
print()
print(line)
print("For access to program, please login")

# login and password

user = input("user:")
password = input("password:")

print(double_line)

#user and password check

if user in login and password == login [user]: 
    print("Welcome", user)
else:
    print("unregistered user, terminating the program..")
    quit()


number_text = len(TEXTS)

#choosing text and statistics
while True:
    try:
        text_number =int(input(f"Enter a number btw. 1 and {number_text} to select:"))
        print(double_line)
        if text_number <= number_text and text_number >= 1:
            break
        print(double_line)
        print("wrong number, please try again")
        print(double_line)
    except:
        print(double_line)
        print("wrong number, please try again")
        print(double_line)
        continue
text = TEXTS[text_number - 1].replace("\n", " ")
text = text.strip()
words = text.split(" ")
count_words = len(words)
print(f"There are {count_words} words in the selected text.")
numeric_string = 0
numeric_counter = 0
lower_word = 0
upper_word = 0
upper_count = 0
for word in words:
    if word.isnumeric():
        numeric_string = numeric_string + 1
        word_num = int(word)
        numeric_counter += word_num
    if word[0].isnumeric():
        continue
    if word [0] == word [0].upper():
        upper_count = upper_count + 1
    if word == word.upper():
        upper_word = upper_word + 1
    if word == word.lower():
        lower_word = lower_word + 1
    

print(f"There are {upper_count} titlecase words.")
print(f"There are {upper_word} uppercase words.")    
print(f"There are {lower_word} lowercase words.")
print(f"There are {numeric_string} numeric strings.")
print("The sum of all the numbers", numeric_counter)
print(double_line)

delka_slov = {}
max_delka = 0

for word in words:
    delka = len(word)
    if delka in delka_slov:
        delka_slov[delka] += 1
    else:
        delka_slov[delka] = 1
    if max_delka < delka:
        max_delka = delka
for i in range (1,max_delka + 1):
    if i in delka_slov:
        hvezdicky = "*" * delka_slov[i]
        print (f"{i}|{hvezdicky}")

print(double_line)
print("Thank you for using text anylizator 1 ")
print("Have a nice day")
print(double_line)