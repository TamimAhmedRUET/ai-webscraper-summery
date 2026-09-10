import os
from dotenv import load_dotenv
from openai import OpenAI
from new_scraper import scrape_website

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

system_prompt = "You are a helpful assistant that summarizes the content of a website."
user_prompt = "Please Summarize the content of the following website:"
scraped_content = scrape_website("blakemonakino.framer.website")

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"{user_prompt}\n\n{scraped_content}"},
    ],
)

print(response.choices[0].message.content)
