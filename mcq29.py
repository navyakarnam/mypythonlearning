from question import question_class

question_prompts=[
    "what color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "what color are bananas?\n(a) Teal/\n(b) Magenta\n(c) Yellow\n\n",
    "what color are berries?\n(a) yellow/\n(b) red\n(c) blue\n\n"

]

questions=[
    question_class(question_prompts[0], "a"),
    question_class(question_prompts[1], "c"),
    question_class(question_prompts[2], "b")
]

def run_test(questions):
    score=0
    for question_class in questions:
        answer= input(question_class.prompt)

        if answer==question_class.answer:
            score+=1
    print("you got " + str(score) + "/" + str(len(questions)) + " correct")

run_test(questions)
