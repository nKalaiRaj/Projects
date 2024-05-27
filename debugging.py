#Python program -Debugging file
def print_values_of(dictionary, keys):
    for key in keys:
        if key in {"lisa","bart","homer"}: #added if condition to get the value of ("lisa","bart","homer")
            value = dictionary[key] #assigned the values to a variable value
            print(value) #Display the output
#Value of homer (d'oh )added within double quotes and with exclamation mark
simpson_catch_phrases = {"lisa": "BAAAAAART!", "bart": "Eat My Shorts!", "marge": "Mmm~mmmmm", "homer": "d'oh!", "maggie": " (Pacifier Suck)"} 
#changed the value of key from ('lisa', 'bart', 'homer') to simpson_catch_phrases.keys()
print_values_of(simpson_catch_phrases,simpson_catch_phrases.keys())

'''
    Expected console output: 

    BAAAAAART!
    Eat My Shorts!
    d'oh!

'''

