import string 
import pandas as pd

def remove_punctuation(text):
    exclude = set(string.punctuation)
    return ''.join(ch for ch in text if ch not in exclude)
def add_periods(text):
    text = text + '.'
    return text
#Questions csv, drop columns
questions = pd.read_csv('Questions.csv', encoding='latin1')
questions = questions.drop(['OwnerUserId', 'CreationDate', 'Score', 'Body'], axis = 1)

questions['Questions'] = [remove_punctuation(question) for question in questions['Title']]
questions['Questions'] = [add_periods(question) for question in questions['Questions']]
questions = questions.drop(['Title'], axis = 1)
                            
#Tags csv
tags = pd.read_csv('Tags.csv', encoding='latin1')

#Merge the dataframes and drop ID 
df = pd.merge(questions, tags, on='Id')
df = df.drop(['Id'], axis=1)


df.to_csv('questions_tagged.csv', index=False)