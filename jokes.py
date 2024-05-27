#Python program to generate random jokes using random module
#Import random module
import random
#Create joke in a list and assign it to a variable.
jokes = [   'Why does Python live on land? By the way, I am not good at Zoology',
            'What do dentists call an astronaut\'s cavity?  ..A black hole!',
            'What is constant? We don\'t do that here…',
            'If programming language was gun…',
            'You will miss something if you move to another language…',
            'Why do you cant compare two different types?',
            'When I get stuck at something…my brain thinks… nothing is more important than satisfaction…',
            'Haha…feeling sorry for him…',
            'How do functions breakup? ..They stop calling each other.',
            'Yeah…It\'s easy peasy…',
            'When someone reports to tech support about an error…',
            'What do you get when you cross a snowman with a vampire? ..Frostbite!']
#Use the random choice function to pick random jokes from the list provided above       
jokes = random.choice(jokes)
print(jokes) #Display random jokes
