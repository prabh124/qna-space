#import pyodbc
#import sqlalchemy
#from sqlalchemy import create_engine
'''
USERNAME = 'sqlserver'
PASSWORD = 'sfhacks2021'
SERVER = 'localhost'
DATABASE = 'master'
DRIVER = 'SQL Server Native Client 11.0'
'''


import pandas as pd
from random import randint

def initDataframe():
    df = pd.DataFrame(columns=['question', 'studentNum', 'popularity'])
    return df

def getStudentNum():
    studentNum = randint(200000000, 299999999)
    
    return studentNum

def askQuestion(df, question, studentNum, popularity = 1):
    lis = [question, studentNum, 1]
    
    df_length = len(df)
    df.loc[df_length] = lis
    
    return None

df = initDataframe()

askQuestion(df, 'How can I take the derivative of x?', getStudentNum())

askQuestion(df, 'How can I take the derivative of y?', getStudentNum())

askQuestion(df, 'How can I take the integral of y?', getStudentNum())

print(df)

#lis = df['Question'].tolist()
#print(lis)