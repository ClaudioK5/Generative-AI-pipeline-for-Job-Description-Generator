from AI_description_generator import AI_description_generator
from prompt import create_prompt
import requests

url = "http://127.0.0.1:8000/job_descriptions/"

job_title = input("enter the job title")

user_input = input("Enter your job requirements")

prompt = create_prompt(user_input)

print(prompt)

ai_output = AI_description_generator(prompt)

data = {'job_name': job_title, 'job_description': ai_output}

response = requests.post(url, json=data)

if response.status_code == 200 or response.status_code == 201:

    print("job description successfully saved on postgresql!")
    print(response.json())

else:

    print('failed!')
    print(response.status_code, response.text)



