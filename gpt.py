import openai
import os

# Set up API key (replace "your_api_key" with your actual API key)
openai.api_key = os.environ.get("OPENAI_API_KEY")

def generate_response(prompt):
    # Set up parameters for GPT-3.5 API call
    params = {
        "engine": "text-davinci-003",
        "prompt": prompt,
        "max_tokens": 3000,
        "n": 1,
        "stop": None,
        "temperature": 0.7,
    }

    try:
        # Make API call and parse the response
        response = openai.Completion.create(**params)
        message = response.choices[0].text.strip()
        return {"success": True, "message": message}
    except Exception as e:
        # Handle exceptions and return an error message
        return {"success": False, "message": str(e)}
