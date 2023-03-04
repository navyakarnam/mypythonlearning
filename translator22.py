def translate(phrase):#translate is a fn we created and phrase is a parameter
    translation=""
    #variable is created to store and display the final result

    for letter in phrase:
        if letter.lower() in "aeiou":  #if letter in "AEIOUaeiou":
            #lower() helps it to keep aeiou only
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation=translation+letter
    return translation

print(translate(input("enter a phrase: ")))
