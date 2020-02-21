#! python2

# randomQuizGenerator.py - Creates quizzes with questions and answers in
# random order, along with the answer key

import random, os, sys

# The quiz data. Keys are states and values are their capitals

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
            'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado':
            'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida':
            'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho':
            'Boise', 'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa':
            'Des Moines', 'Kansas':'Topeka', 'Kentucky': 'Frankfort', 'Louisiana':
            'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis',
            'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota':
            'Saint Paul', 'Mississippi': 'Jackson', 'Missouri': 'Jefferson City',
            'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City',
            'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico':
            'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
            'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma':
            'Oklahoma City', 'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg',
            'Rhode Island': 'Providence', 'South Carolina': 'Columbia',
            'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin',
            'Utah': 'Salt Lake City', 'Vermont': 'Montpelier', 'Virginia':
            'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston',
            'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# Generate 35 quiz files

if not os.path.isdir(os.path.join(os.getcwd(), 'statesCapitalsQuiz')):
    os.mkdir(os.path.join( os.getcwd(), 'statesCapitalsQuiz'))
    
os.chdir(os.path.join( os.getcwd(), 'statesCapitalsQuiz'))
cwd = os.getcwd()

for quizNum in range(35):
    quizFile=open(str(quizNum)+'quiz.txt','w')
    ansFile=open(str(quizNum)+'ans.txt','w')
    quizFile.write('Welcome to guiz'+str(quizNum))
    
    states = capitals.keys()
    random.shuffle(states)

    quizFile.close()
    ansFile.close()

    #quizFile = open(str(quizNum)+'quiz.txt','a')
    #ansFile = open(str(quizNum)+'ans.txt','a')
    
    for questNum in range(50):
        correctAnswer = capitals[states[questNum]]
        wrongAnswers = list(capitals.values())
        wrongAnswers.remove(correctAnswer)
        #del wrongAnswers[wrongAnswers.index(correctAnswer)]
        answerOptions = random.sample( random.sample(wrongAnswers,3) + [correctAnswer],4)
        #print [states[questNum]] + answerOptions

        with open(str(quizNum)+'quiz.txt','a') as quizFile:
            quizFile.write('\n\n' + str(questNum+1) + '. What is the capital of ' + states[questNum] + '?')
            for i in range(4):
                quizFile.write('\n   ' + 'ABCD'[i] + ' ' + answerOptions[i])

        with open(str(quizNum)+'ans.txt','a') as ansFile:
            ansFile.write('\n\n' + str(questNum+1) + '. The capital of ' + states[questNum] + ' is :')
            for i in range(4):
                if answerOptions[i] == correctAnswer:
                    ans = answerOptions[i]
                else:
                    ans = ''
                ansFile.write('\n   ' + 'ABCD'[i] + ' ' + ans)
            
    quizFile.close()
    ansFile.close()
