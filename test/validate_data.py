import pandas as pd

def check_similarity(folder_path, question_csv_path, validate_csv_path):
    overall_scores = 0
    multiple_choice_score = 0
    single_choice_score = 0

    # Load the CSV files
    question_df = pd.read_csv(question_csv_path)
    print(len(question_df))
    validate_df = pd.read_csv(validate_csv_path)

    # Assume the text to compare is in the first column or specify if needed
    # For simplicity, assume each row has a 'text' column or use the first column
    with open(f'{folder_path}/validate.md', 'w') as f:
        f.write(f"# Validation Result\n")

    for index in range(len(question_df)):
        question_texts = question_df.iloc[index]['answers']
        validate_texts = validate_df.iloc[index]['answers']

        with open(f'{folder_path}/validate.md', 'a', encoding='utf-8') as f:
            if question_texts == validate_texts:
                overall_scores += 1
                # Check if multiple choice (contains comma)
                if ',' in str(validate_texts):
                    multiple_choice_score += 1
                else:
                    single_choice_score += 1
                f.write(f"{index}. {question_texts} | {validate_texts} ✅\n")
            else:
                f.write(f"{index}. {question_texts} | {validate_texts} ❌\n")


    # Return the similarity matrix or process as needed
    return overall_scores, multiple_choice_score, single_choice_score


folder_path = 'answer2'
print('Total Score:', check_similarity(folder_path, f'{folder_path}\\answer.csv', f'{folder_path}\\answer-validate.csv'))
