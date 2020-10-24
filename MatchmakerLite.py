 # Justin Freiberg 
 # Matchmaker Lite

INTRODUCTION = '''
******************************************************
                    Matchmaker 2.0
            Helping you find <3 since 2020
                    Cupidsoft, Inc.
******************************************************

This Program figures out if you and I are a match 
made in heaven. You will be given 5 questions to 
answer. For each question, answer 5 if you strongly
agree, 4 if you agree, 3 if you are neutral, 2 if 
you disagree, and 1 if you strongly disagree.

Will we find find happiness together? 
'''

QUESTION = [
    'The Chicago White Sox are the superior Chicago baseball team.',
    'Golf is one of the more difficult sports to learn and improve at.',
    'Pinepple belongs on pizza.',
    'Subway is better than any other sub shop.',
    'We are not the only living life form in the universe.'
]

DESIRED_RESPONSE = [
    5, 
    4, 
    3, 
    1,
    5, 
]

MAX_SCORE = 5 * len(QUESTION)

print(INTRODUCTION)

response = []
compatibility = []

for i in range(len(QUESTION)):
    userResponse = int(input(QUESTION[i]))
    while userResponse > 5 or userResponse < 1: 
        print("Error! Now I know you might want to emphasis your thoughts on certain topics, let's keep the responses between 1 and 5 for my own sanity. Let's go ahead and try that one again!")
        print("")
        userResponse = int(input(QUESTION[i]))    
    response.append(userResponse)

    questionCompatibility = 5 - abs(userResponse - DESIRED_RESPONSE[i])
    compatibility.append(questionCompatibility)

    
    print('Question %d compatibility: %d\n' % (i+1, questionCompatibility))

totalCompatibility = 0
for c in compatibility:
    totalCompatibility += c

totalCompatibility *= 100 / MAX_SCORE
print("Your score was %d\n\n" % (totalCompatibility))
if totalCompatibility <= 70: 
    print("Yeah, so uhh, I don't quite think this is going to work out.")
elif totalCompatibility >= 71 and totalCompatibility <= 90: 
    print("Unfortunately, I think we would just be better off as friends.")
else:
    print("So ... when's the wedding?")




