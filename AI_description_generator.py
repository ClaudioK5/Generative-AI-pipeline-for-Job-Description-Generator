from openai import OpenAI
from email_sender import send_email

client = OpenAI(
    api_key="insert here your apikey",
    base_url="https://api.deepseek.com/v1"
)


def AI_description_generator(prompt):


    try:
        response = client.chat.completions.create(model="deepseek-chat",
                                              messages=[{'role': 'user', 'content': prompt}],
                                              max_tokens=300)

        ai_output = response.choices[0].message.content.strip()

        print(ai_output)

        subject = 'AI description for the job requirements'

        send_email(subject, ai_output)

        return ai_output

    except Exception as e:

        return {"error": str(e)}