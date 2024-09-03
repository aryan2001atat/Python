password = input("Enter your password")
score = 0
has_upper = 0
has_lower = 0
has_digit = 0
has_special = 0
specialCharacter = ['!', '@', "#", "$"]
if len(password) >= 8:
    score += 1


for i in password:
    if i.isdigit():
        has_digit = 1
    if i in specialCharacter:
        has_special = 1
    if i.isupper():
        has_upper = 1
    if i.islower():
        has_lower = 1

if has_upper and has_lower:
    score += 1
if has_digit:
    score += 1
if has_special:
    score += 1

if score == 4:
    print("Strong password")
elif score == 2 or score == 3:
    print("Moderate password")
elif score == 0 or score == 1:
    print("Weak password")

