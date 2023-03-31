from bs4 import BeautifulSoup
import json
import os
import glob


def create_txt(file):
    with open(file, "r", encoding="utf-8") as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, "html.parser")
    script_tag = soup.find("script", {"type": "application/ld+json"})
    json_data = json.loads(script_tag.string)


    for item in json_data["@graph"]:
        if item["@type"] == "Article":
            title = item["headline"]
            break

    # Find the content
    entry_content = soup.find('div', {'class': 'entry-content'})

    # Extract plain text from the <body> tag
    plain_text = entry_content.get_text()

    # Create the content for the text file
    text_data = f"{title}\n{plain_text}"

    # Save the content as a text file with the name "{url}.txt"
    filename = f"parsed/{title}.txt"
    with open(filename, 'w') as outfile:
        outfile.write(text_data)

# Change 'your_directory_path' to the path of the directory you want to process
your_directory_path = '/Users/mac20/Desktop/~/Desktop/Farnam'

# Recursively find all .html files in the directory and its subdirectories
html_files = glob.glob(os.path.join(your_directory_path, '**', '*.html'), recursive=True)

#print(len(html_files))

for file in html_files:
    try:
        create_txt(file)
    except:
        print(f"File {file} couldn't be parsed")
