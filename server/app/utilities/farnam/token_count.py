import os
import tiktoken

def count_tokens(file_path):
    with open(file_path, 'r') as f:
        text = f.read()
    encoding = tiktoken.get_encoding("cl100k_base")
    num_tokens = len(encoding.encode(text))
    return num_tokens

def count_tokens_for_all_files(directory):
    total_tokens = 0
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.txt'):
                file_path = os.path.join(root, file)
                file_tokens = count_tokens(file_path)
                total_tokens += file_tokens

    return total_tokens

directory = "parsed"
total_tokens = count_tokens_for_all_files(directory)
print(f"Total tokens in the '{directory}' directory: {total_tokens}")