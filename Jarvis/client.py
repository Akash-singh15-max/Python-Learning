from openai import OpenAI

# pip install openai
# defaults to getting the key using os.environ.get("OPENAI_API_KEY")
# if you save the key under a different environment variable name, you
# can do something like
client = OpenAI(
    api_key="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",
)

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud."},
        {
            "role": "user",
            "content": "What is coding"
        }
    ]
)

print(completion.choices[0].message.content)


