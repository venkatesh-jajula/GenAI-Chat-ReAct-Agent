import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
print(api_key)

if not api_key:
    raise ValueError("❌ OPENAI_API_KEY not found in .env file")

# Initialize OpenAI client
client = OpenAI(api_key=api_key)

# Send a simple test prompt
try:
    print("🔍 Testing API connection...")
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Say 'Hello, BMW! This is a test response.'"}
        ],
        max_tokens=50
    )
    print("✅ API working successfully!\n")
    print("Model reply:", response.choices[0].message.content)

except Exception as e:
    print("❌ API test failed!")
    print(e)
