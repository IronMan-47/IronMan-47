import os
from datetime import datetime

def create_new_post(title, content):
    date = datetime.now().strftime('%Y-%m-%d')
    filename = f"_posts/{date}-{title.replace(' ', '-').lower()}.md"
    
    if not os.path.exists('_posts'):
        os.makedirs('_posts')
    
    with open(filename, 'w') as file:
        file.write(f"---\n")
        file.write(f"title: \"{title}\"\n")
        file.write(f"date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        file.write(f"categories: blog\n")
        file.write(f"---\n\n")
        file.write(content)
    
    print(f"New post created: {filename}")

def commit_and_push():
    os.system("git add .")
    os.system(f'git commit -m "New blog post created automatically"')
    os.system("git push origin main")

# Example usage
title = "My Automated Blog Post"
content = """
This is a blog post generated automatically using a Python script!

## How It Works

The script creates a Markdown file with the current date and title, writes the content, and saves it to the _posts directory.
"""

create_new_post(title, content)
commit_and_push()
