from openai import OpenAI
import requests
client = OpenAI(
  api_key="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"
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
