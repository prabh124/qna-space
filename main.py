from questions import Questions

if __name__ == '__main__':
    
    q = Questions()
    df = q.initDataframe()
    
    q.askQuestion(df, 'How does the len() function work?', q.getStudentNum(), 24)
    q.askQuestion(df, 'How do I add a list to a dataframe?', q.getStudentNum())
    
    q.askQuestion(df, 'How can I find the sum of a list?', q.getStudentNum(), 4)
    q.askQuestion(df, 'What is abstraction?', q.getStudentNum(), 2)
    
    
    q.askQuestion(df, 'What are the 4 pillars of Object Oriented Programming?', q.getStudentNum(), 4)
    q.askQuestion(df, 'How do you compare a list of characters?', q.getStudentNum(), 2)
    
    studentNums = df['studentNum'].tolist()
    
    q.upvoteQuestion(df, studentNums[0])
    q.upvoteQuestion(df, studentNums[0])
    q.upvoteQuestion(df, studentNums[0])
    q.upvoteQuestion(df, studentNums[1])
    
    print(df)