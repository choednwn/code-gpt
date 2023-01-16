import os
import openai

def check_key_file():
    key_path = os.path.join(os.path.dirname(__file__), '../../api.key')
    key_file = open(key_path, "r")
    key = key_file.read()

    try:
        openai.api_key = os.getenv(key)
        openai.Model.retrieve("text-davinci-003")
        response = openai.Completion.create(
            model="text-ada-001",
            prompt="Say this is a test",
            max_tokens=8000,
            echo=True,
            temperature=0
        )
        print(str(response))
        
    except:
        pass