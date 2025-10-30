from openai import OpenAI
import requests
client = OpenAI(
  api_key=""
)


# //_git/
r = requests.get('https://dev.azure.com/PeoplesHR/HRM/_apis/git/repositories/HRM-DB/pullrequests?api-version=7.1')

# print(r)

response = client.responses.create(
  model="gpt-5-nano",
  reasoning={"effort": "low"},
  input="are you aware of good dotnet coding practices",
  store=True,
)

print(response.output_text);
