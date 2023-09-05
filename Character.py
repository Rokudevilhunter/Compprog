user_name = input('Whats your name')
user_age = input('whats your age')
user_sex = input('are you male female or other')
character = {
    "Name": user_name,
    "Age": user_age,
    "isMale": user_sex,
    "Fav_food_list": ['watermelon', 'lettuce', 'sandwich'],
    "isAlive": True,
    }
print('i am a',user_age,'year old', user_sex, 'named', user_name)