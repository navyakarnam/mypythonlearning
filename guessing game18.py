the_secret_word="wow"
guess=" "
guess_count=0
guess_limit=3
out_of_guesses=False

while guess!=the_secret_word and not(out_of_guesses):
    if guess_count<guess_limit:
        guess=input("enter guess: ")
        guess_count=guess_count+1

    else:
         out_of_guesses=True
        
if out_of_guesses:
    print("you loose")
else:
    print("you win")