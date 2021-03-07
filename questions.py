import pandas as pd
from random import randint

class Questions:
    
    def __init__(self):
        pass
    
    def initDataframe(self):
        df = pd.DataFrame(columns=['question', 'studentNum', 'popularity'])
        return df
    
    def getStudentNum(self):
        studentNum = randint(210000000, 299999999)
        
        return studentNum
    
    def askQuestion(self, df, question, studentNum, popularity = 1):
        lis = [question, studentNum, popularity]
        
        df_length = len(df)
        df.loc[df_length] = lis
        
        return None
    
    def upvoteQuestion(self, df, studentNum):
        df['popularity'][df['studentNum'] == studentNum] += 1
        return None