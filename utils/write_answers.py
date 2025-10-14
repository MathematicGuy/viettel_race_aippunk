import os

def write_answers_to_file(answers):
    with open('data/answer.md', 'w') as f:
        f.write("### TASK QA\n")
        f.write("num_correct,answers\n")
        for answer in answers:
            # Split by comma and strip spaces to count options
            options = [opt.strip() for opt in answer.split(',')]
            num_correct = len(options)
            # Format as required, quote if multiple
            if num_correct == 1:
                f.write(f"{num_correct},{answer}\n")
            else:
                f.write(f"{num_correct},\"{answer}\"\n")


def write_extract_to_file(extracted_folder):
    file_names = [d for d in os.listdir(extracted_folder) if os.path.isdir(os.path.join(extracted_folder, d))]
    print(file_names)
    with open('temp_answer.md', 'w', encoding='utf-8') as f:
        f.write('### TASK EXTRACT\n')

    for i, file_name in enumerate(file_names):
        MARKDOWN_DIR = os.path.join(extracted_folder, file_name)
        print('MARKDOWN_DIR:', MARKDOWN_DIR)

        with open(f'{MARKDOWN_DIR}/main.md', 'r', encoding='utf-8') as f:
            content = f.read()
        with open('temp_answer.md', 'a', encoding='utf-8') as f:
            f.write(f'\n\n# {file_name[:6]}_{file_name[-3:]}\n{content}')

    # Move content from temp_answer.md to answer.md
    with open('temp_answer.md', 'r', encoding='utf-8') as temp_f:
        temp_content = temp_f.read()
    with open('../answer.md', 'w', encoding='utf-8') as f:
        f.write(temp_content)
    os.remove('temp_answer.md')

if __name__ == '__main__':
    print(os.getcwd())
    PATH = "../private-test-output"
    write_extract_to_file(PATH)