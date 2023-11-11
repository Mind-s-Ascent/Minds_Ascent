import openai

openai.api_key = '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'

with open('dialogues.txt', 'r', encoding='utf-8') as file:
    dialogs = file.read()


response = openai.Completion.create(
  engine="text-davinci-002",
  prompt=dialogs,
  max_tokens=100
)

print(response.choices[0].text.strip())
