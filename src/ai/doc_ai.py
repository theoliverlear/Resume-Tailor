import json
import os
import tkinter as tk

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
open_ai_key = os.getenv('OPEN_AI_KEY')

def get_text_input():
    def get_and_close():
        nonlocal user_text
        user_text = text_area.get("1.0", tk.END).strip()
        root.destroy()

    user_text = ""
    root = tk.Tk()
    root.title("Text Input")

    text_area = tk.Text(root, wrap=tk.WORD, height=15, width=60)
    text_area.pack(pady=10, padx=10)

    submit_button = tk.Button(root, text="Submit", command=get_and_close)
    submit_button.pack(pady=5)

    root.mainloop()
    return user_text


def call_open_ai():
    text = get_text_input()
    prompt = f"""
    Extract relevant content into two categories: hard skills (ex. Java, React, Databases) and soft skills (ex. Critical Thinking, Time Management) from the following job application text and return it as a JSON response.
    Hard skills should look like Python, Django, Unit Testing, and System Architecture, not Problem Solving, Programming Languages, and Teamwork.

    The values should be returned in Title Case.
    Hard skills limit = 9, soft skills limit  = 4.
    Ensure that the returned skills are the most relevant and hirable according to the job application. Return each section in a hierarchical order as to the most relevant on top and the lesser relevant on bottom.
    Limit individual skill's text to 20 characters.
    Do not put your response in a formatted block. Instead just provide the JSON directly.
    Make sure to include all braces needed.
    Text:
    {text}
    """
    open_ai_messenger = OpenAI(api_key=open_ai_key)
    response = open_ai_messenger.chat.completions.create(
        model="gpt-4o-mini",
        max_tokens=150,
        temperature=0.5,
        messages=[{"role": "system",
                   "content": "You are an AI that extracts key insights from job applications."},
                  {"role": "user", "content": prompt}],
    )
    response_content = response.choices[0].message.content
    print(response_content)
    json_response = json.loads(response_content)
    print(json_response)
    skill_list = list(json_response["hardSkills"] + json_response["softSkills"])
    print(skill_list)
    return skill_list