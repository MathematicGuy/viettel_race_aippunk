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