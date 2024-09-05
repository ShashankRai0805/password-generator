def password_gnerator():
    import requests, random
    nounURL = "https://random-word-form.herokuapp.com/random/noun"
    adjectiveURL = "https://random-word-form.herokuapp.com/random/noun"
    noun = requests.get(nounURL).json()[0]
    adjective = requests.get(adjectiveURL).json()[0]
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)
    num3 = random.randint(0,9)
    symbolList = ["!","@","#","$","%","^","&","*",",",".","/","?",";",":","+","-","~"]
    symbol1 = random.choice(symbolList)
    symbol2 = random.choice(symbolList)
    symbol3 = random.choice(symbolList)
    password = f"{adjective.capitalize()}{noun.capitalize()}{num1}{num2}{num3}{symbol1}{symbol2}{symbol3}"
    return password
print("WELCOME TO PASSWORD GENERATOR!")
print("GENERATING PASSWORD...")
password = password_gnerator()
print(f"GENERATED PASSWORD : {password}")
exitProgram = False
while exitProgram==False:
    choice = input("DO YOU WANT TO GENERATE ANOTHER PASSWORD(Y/N) : ")
    if choice=="N":
        exitProgram = True
        break
    else:
        print("GENERATING PASSWORD...")
        password = password_gnerator()
        print(f"GENERATED PASSWORD : {password}")