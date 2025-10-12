import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def check_similarity(question_csv_path, validate_csv_path):
	scores = 0
	# Load the CSV files
	question_df = pd.read_csv(question_csv_path)
	print(len(question_df))
	validate_df = pd.read_csv(validate_csv_path)

	# Assume the text to compare is in the first column or specify if needed
	# For simplicity, assume each row has a 'text' column or use the first column
	for index in range(len(question_df)):
		question_texts = question_df.iloc[index]['answer']
		validate_texts = validate_df.iloc[index]['answer']

		if question_texts == validate_texts:
			scores += 1
			print(index, question_texts, ' | ', validate_texts, '✅')
		else:
			print(index, question_texts, ' | ', validate_texts, '❌')
		# 	print(index, 'Prediction', question_texts, 'Grounth True:',validate_texts, '\n')

	# Return the similarity matrix or process as needed
	return scores

print(check_similarity('answer_task_qa.csv', 'validate_task_qa.csv'))