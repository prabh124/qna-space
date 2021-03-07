from questions import Questions
import pandas as pd 

if __name__ == '__main__':
    q = Questions()
    df = q.initDataframe()
    
    q.askQuestion(df, 'How can I take the derivative of x?', q.getStudentNum())
    
    q.askQuestion(df, 'How can I take the derivative of y?', q.getStudentNum(), 10)
    
    q.askQuestion(df, 'How can I take the integral of y?', q.getStudentNum())
    
    studentNums = df['studentNum'].tolist()
    
    q.upvoteQuestion(df, studentNums[0])
    q.upvoteQuestion(df, studentNums[0])
    q.upvoteQuestion(df, studentNums[0])
    q.upvoteQuestion(df, studentNums[1])
    
    print(df)
    
    #df2 = pd.read_csv('Questions2.csv', encoding='latin1')
    
