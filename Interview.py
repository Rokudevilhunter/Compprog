name = input("What is your Name?: ")

print(name,'what is your desired program-language?')
type = input('')

print('How long have you been programming in',type)
ex = int(input(''))

while ex < 1:
    print("0 is too low for this job")
    ex = int(input(''))

print("What is you desired salary")
sal = input("") 

print('your name is',name,'you have been programming in',type,'for',ex,'years. you want',sal,'per year')