import pandas as pd

#Calculation for Estimated Remaining Characters after guessing
def estRemain(yesatt, totalcount, noatt):
    calc = ((yesatt * (yesatt/totalcount)) + (noatt * (noatt/totalcount)))
    return calc

#Initial Display of Attributes
def display():
    dispdict = {}
    for column in df:
        try:
            dispdict.update({column: str(round(estRemain(
            float(df[column].value_counts()['Yes']),
            float(df[column].value_counts().sum()),
            float(df[column].value_counts()['No'])), 3))})
        except KeyError:
            dispdict.update({column: ': Disregard (All True or All False)'})

    sortdict = sorted( ((v,k) for k,v in dispdict.items()), reverse=True)

    for x,y in sortdict:
        if y == 'Name':
            continue
        else:
            print(str(y) + ': ' + str(x))

#Get Input for Attribute to guess and Yes/No answer
def guessChoice():
    attribute = None
    yesNo = None

    while attribute not in df:
        attribute = input("Choose your Attribute: ")
    while yesNo not in ['Yes', 'No']:
        yesNo = input("Yes or No for that Attribute? ")
    return attribute, yesNo

#Reuse of Display with increased filtering
def stageOneFunc(attribute, choice):
    global guessing
    updatedDict = {}
    list = df[df[attribute] == choice]
    if len(list['Name']) == 1:
        print('The correct answer is: ' + list['Name'])
        guessing = 0
    else:
        for column in list:
            try:
                updatedDict.update({column: str(round(estRemain(
                float(list[column].value_counts()['Yes']),
                float(list[column].value_counts().sum()),
                float(list[column].value_counts()['No'])), 3))})
            except KeyError:
                updatedDict.update({column: ': Disregard (All True or All False)'})
            except IndexError:
                pass

        sortUpdatedDict = sorted(((v,k) for k,v in updatedDict.items()), reverse=True)

        for x,y in sortUpdatedDict:
            if y == 'Name':
                continue
            else:
                print(str(y) + ': ' + str(x))

#Reuse of Stage 1 with Increased filtering
def stageTwoFunc(att1, choice1, att2, choice2):
    global guessing
    updatedDict = {}
    list = df[(df[att1] == choice1) & (df[att2] == choice2)]
    if len(list['Name']) == 1:
        print('The correct answer is: ' + list['Name'])
        guessing = 0
    else:
        for column in list:
            try:
                updatedDict.update({column: str(round(estRemain(
                float(list[column].value_counts()['Yes']),
                float(list[column].value_counts().sum()),
                float(list[column].value_counts()['No'])), 3))})
            except KeyError:
                updatedDict.update({column: ': Disregard (All True or All False)'})
            except IndexError:
                pass

        sortUpdatedDict = sorted(((v,k) for k,v in updatedDict.items()), reverse=True)

        for x,y in sortUpdatedDict:
            if y == 'Name':
                continue
            else:
                print(str(y) + ': ' + str(x))

#Increased Filtering again...
def stageThreeFunc(att1, choice1, att2, choice2, att3, choice3):
    global guessing
    updatedDict = {}
    list = df[(df[att1] == choice1) & (df[att2] == choice2) & (df[att3] == choice3)]
    if len(list['Name']) == 1:
        print('The correct answer is: ' + list['Name'])
        guessing = 0
    else:
        for column in list:
            try:
                updatedDict.update({column: str(round(estRemain(
                float(list[column].value_counts()['Yes']),
                float(list[column].value_counts().sum()),
                float(list[column].value_counts()['No'])), 3))})
            except KeyError:
                updatedDict.update({column: ': Disregard (All True or All False)'})
            except IndexError:
                pass

        sortUpdatedDict = sorted(((v,k) for k,v in updatedDict.items()), reverse=True)

        for x,y in sortUpdatedDict:
            if y == 'Name':
                continue
            else:
                print(str(y) + ': ' + str(x))

#Oh for pete sake... How do I automate this increased filtering
def stageFourFunc(att1, choice1, att2, choice2, att3, choice3, att4, choice4):
    global guessing
    updatedDict = {}
    list = df[(df[att1] == choice1) & (df[att2] == choice2) & (df[att3] == choice3) & (df[att4] == choice4)]
    if len(list['Name']) == 1:
        print('The correct answer is: ' + list['Name'])
        guessing = 0
    else:
        for column in list:
            try:
                updatedDict.update({column: str(round(estRemain(
                float(list[column].value_counts()['Yes']),
                float(list[column].value_counts().sum()),
                float(list[column].value_counts()['No'])), 3))})
            except KeyError:
                updatedDict.update({column: ': Disregard (All True or All False)'})
            except IndexError:
                pass

        sortUpdatedDict = sorted(((v,k) for k,v in updatedDict.items()), reverse=True)

        for x,y in sortUpdatedDict:
            if y == 'Name':
                continue
            else:
                print(str(y) + ': ' + str(x))

#Etc.. Filtering
def stageFiveFunc(att1, choice1, att2, choice2, att3, choice3, att4, choice4, att5, choice5):
    global guessing
    updatedDict = {}
    list = df[(df[att1] == choice1) & (df[att2] == choice2) & (df[att3] == choice3) & (df[att4] == choice4) & (df[att5] == choice5)]
    if len(list['Name']) == 1:
        print('The correct answer is: ' + list['Name'])
        guessing = 0
    else:
        for column in list:
            try:
                updatedDict.update({column: str(round(estRemain(
                float(list[column].value_counts()['Yes']),
                float(list[column].value_counts().sum()),
                float(list[column].value_counts()['No'])), 3))})
            except KeyError:
                updatedDict.update({column: ': Disregard (All True or All False)'})
            except IndexError:
                pass

        sortUpdatedDict = sorted(((v,k) for k,v in updatedDict.items()), reverse=True)

        for x,y in sortUpdatedDict:
            if y == 'Name':
                continue
            else:
                print(str(y) + ': ' + str(x))

#Etc Filtering...
def stageSixFunc(att1, choice1, att2, choice2, att3, choice3, att4, choice4, att5, choice5, att6, choice6):
    global guessing
    updatedDict = {}
    list = df[(df[att1] == choice1) & (df[att2] == choice2) & (df[att3] == choice3) & (df[att4] == choice4) & (df[att5] == choice5) & (df[att6] == choice6)]
    if len(list['Name']) == 1:
        print('The correct answer is: ' + list['Name'])
        guessing = 0
    else:
        for column in list:
            try:
                updatedDict.update({column: str(round(estRemain(
                float(list[column].value_counts()['Yes']),
                float(list[column].value_counts().sum()),
                float(list[column].value_counts()['No'])), 3))})
            except KeyError:
                updatedDict.update({column: ': Disregard (All True or All False)'})
            except IndexError:
                pass

        sortUpdatedDict = sorted(((v,k) for k,v in updatedDict.items()), reverse=True)

        for x,y in sortUpdatedDict:
            if y == 'Name':
                continue
            else:
                print(str(y) + ': ' + str(x))

#Seven filters should be enough...
def stageSevenFunc(att1, choice1, att2, choice2, att3, choice3, att4, choice4, att5, choice5, att6, choice6, att7, choice7):
    global guessing
    updatedDict = {}
    list = df[(df[att1] == choice1) & (df[att2] == choice2) & (df[att3] == choice3) & (df[att4] == choice4) & (df[att5] == choice5) & (df[att6] == choice6) & (df[att7] == choice7)]
    if len(list['Name']) == 1:
        print('The correct answer is: ' + list['Name'])
        guessing = 0
    else:
        for column in list:
            try:
                updatedDict.update({column: str(round(estRemain(
                float(list[column].value_counts()['Yes']),
                float(list[column].value_counts().sum()),
                float(list[column].value_counts()['No'])), 3))})
            except KeyError:
                updatedDict.update({column: ': Disregard (All True or All False)'})
            except IndexError:
                pass

        sortUpdatedDict = sorted(((v,k) for k,v in updatedDict.items()), reverse=True)

        for x,y in sortUpdatedDict:
            if y == 'Name':
                continue
            else:
                print(str(y) + ': ' + str(x))
#Main Program Begins
df = pd.read_csv('Complete Profile.csv')
guessing = 1
display()

#This loops failed on it's own to break when there was a correct guess
#Just realized this while look accomplishes nothing, but the spaghetti code works
while guessing != 0:
    #This IF statement correctly broke if the guess was correct
    if guessing != 0:
        stageOne = guessChoice()
        stageOneFunc(stageOne[0], stageOne[1])
    else:
        break
        #Second Guess with correct Break
    if guessing != 0:
        stageTwo = guessChoice()
        stageTwoFunc(stageOne[0], stageOne[1], stageTwo[0], stageTwo[1])
    else:
        break
        #Third Guess...
    if guessing != 0:
        stageThree = guessChoice()
        stageThreeFunc(stageOne[0], stageOne[1], stageTwo[0], stageTwo[1], stageThree[0], stageThree[1])
    else:
        break
        #Fourth Guess
    if guessing != 0:
        stageFour = guessChoice()
        stageFourFunc(stageOne[0], stageOne[1], stageTwo[0], stageTwo[1], stageThree[0], stageThree[1], stageFour[0], stageFour[1])
    else:
        break
        #Fifth Guess
    if guessing != 0:
        stageFive = guessChoice()
        stageFiveFunc(stageOne[0], stageOne[1], stageTwo[0], stageTwo[1], stageThree[0], stageThree[1], stageFour[0], stageFour[1], stageFive[0], stageFive[1])
    else:
        break
        #Sixth Guess
    if guessing != 0:
        stageSix = guessChoice()
        stageSixFunc(stageOne[0], stageOne[1], stageTwo[0], stageTwo[1], stageThree[0], stageThree[1], stageFour[0], stageFour[1], stageFive[0], stageFive[1], stageSix[0], stageSix[1])
    else:
        break
        #Final Guess
    if guessing != 0:
        stageSeven = guessChoice()
        stageSevenFunc(stageOne[0], stageOne[1], stageTwo[0], stageTwo[1], stageThree[0], stageThree[1], stageFour[0], stageFour[1], stageFive[0], stageFive[1], stageSix[0], stageSix[1], stageSeven[0], stageSeven[1])
    else:
        break
    print('You have had 7 stages. If you can not win by now, you do not deserve to...')
    break
