import tkinter as tk
import requests

# Replace with your OpenAI API key
OPENAI_API_KEY = "xyz"

def call_openai_api(prompt):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": prompt}]
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Error: {response.status_code}\n{response.text}"

def on_search():
    prompt = entry.get()
    result = call_openai_api(prompt)
    output.delete(1.0, tk.END)
    output.insert(tk.END, result)

root = tk.Tk()
root.title("OpenAI Prompt Search")

tk.Label(root, text="Enter your prompt:").pack()
entry = tk.Entry(root, width=50)
entry.pack()

search_btn = tk.Button(root, text="Search", command=on_search)
search_btn.pack()

output = tk.Text(root, height=15, width=60)
output.pack()

root.mainloop()