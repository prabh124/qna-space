# qna-space

This is our team's submission to SF Hacks 2021!
https://devpost.com/software/qna-space

## Inspiration

Students sometimes have moments where they want to ask a question, but are too shy to do so. What if there was a forum where students can ask their profs questions anonymously, with analytics provided to the prof to better their understanding of the classes knowledge on the lecture?

## What it does

QNA Space provides a platform where professors can generate a forum for their lecture and share the link to their class. The link is unique for that session, allowing for easy access and usage. Students can ask questions which are then categorized using NLP. Students can upvote questions that are similar to what they wanted to ask. Analytics for the session are provided to the professor, who is able to look at statistics such as engagement, most upvoted questions, and number of questions in each category.

## How we built it

To have a proof of concept of the front end we used Figma to design what the student's session and the professors dashboards. The bulk of the backend was related to training the model. The model was trained on a dataset full of questions, answers, and tags on stackoverflow. After preprocessing the data we ended up with a csv file with 2 columns (Questions, tags) and 75,000 rows. Using single-label classification on Google Cloud AutoML supervised learning platform, we were able to train a ML model on the dataset which resulted in 688 filter labels. These filter labels can be applied to predictions. The model is able to take new Python questions and categorize them by their general topic (filter label). These topics include algorithm design, AWS, qa-automation, visualizations, and many many more.

## Challenges we ran into

Training the model was the biggest challenge we had. This included cleaning the data, finding dataset a reliable dataset and preprocessing the data for the model to be trained effectively.

## Accomplishments that we're proud of

Some accomplishments we're proud of include learning to use Google cloud and using their natural language processing API. Pre-processing was a big challenge for us, preparing the data for it to be trained by the model was a big learning curve.

## What we learned

We learned many things throughout our journey, some things included was using google cloud natural language processing for the first time, designing the concept on Figma, and training a model using a large 75,000 row dataset with questions and tags on Kaggle.

## What's next for QnA Space

Use Python library BeautifulSoup to scrape various web sources with student and course-specific questions to enhance model tagging and functionality. Some possible websites are: Chegg.com Stackoverflow.com Mathoverflow.net writingforums.com

We also want to expand the analytics the professors see such as having course analysis rather than just sessions. A professor will be able to see the engagement over the span of a semester.
