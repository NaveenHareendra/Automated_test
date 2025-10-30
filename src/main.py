from openai import OpenAI
import requests


# print(r)

response = client.responses.create(
  model="gpt-5-nano",
  reasoning={"effort": "low"},
  input="are you aware of good dotnet coding practices",
  store=True,
)

print(response.output_text);
