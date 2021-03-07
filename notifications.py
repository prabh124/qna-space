import questions from Questions
import pandas as pd
import requests

class Notification:

	def notify(): 
		totalUpvotes = df['popularity'].sum()
		df['upVoteRatio'] = df['popularity']/totalUpVotes
		unique_id = 'abc123'
		email = 'prof@university.ca'


		if upVoteRatio.values >= 0.5:
			totalUpvoteRatio = 0.5
			response = requests.post('https://events-api.notivize.com/applications/d3d3ea24-0b18-43b1-9cf8-3c93d22ee759/event_flows/31849fb3-372c-4b63-b1ed-baf5843ed8a3/events', json = {
				email': '<value for email>',
				'totalUpvoteRatio': '<value for totalUpvoteRatio>',
				'unique_id': '<value for unique_id>'
				}

		print(response)