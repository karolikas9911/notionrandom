import os
import random
import requests

NOTION_API_TOKEN = os.environ["NOTION_API_TOKEN"]
DATABASE_ID = os.environ["DATABASE_ID"]

def get_random_page():
    headers = {
        "Authorization": f"Bearer {NOTION_API_TOKEN}",
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28"
    }
    url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"
    response = requests.post(url, headers=headers)

    if response.status_code != 200:
        return f"Error: {response.json().get('message', 'Unknown error')}"

    pages = response.json().get("results", [])
    if not pages:
        return "No pages found in the database!"

    # Pick a random page
    random_page = random.choice(pages)
    return random_page["url"]

if __name__ == "__main__":
    random_page_url = get_random_page()
    print(random_page_url)  # Output the random page URL
