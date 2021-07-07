import random


compliments = ['Oh no! Remember you are valued!', 'It will get better', 'Sorry to hear! Try doing something that makes you happy, like eating ice-cream or watching netflix!']


Hello = str(input('hello world, say hi back!: '))

How_are_you = str(input('Hello! how are you? (Good or Bad): '))

if How_are_you == "Good":
    print('Good to hear!')
    
if How_are_you == "Bad":
    print(random.choice(compliments))
