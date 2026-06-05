import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ["OPENROUTER_API_KEY"]
)


class ChatAgent:
    def __init__(self, system_prompt, max_turns, model_key="google/gemma-4-31b-it:free"):
        self.system_prompt = system_prompt
        self.max_turns = max_turns
        self.model_key = model_key
        self.messages = [{"role":"system", "content": self.system_prompt}]

    def call_model(self):
        print("Chat started. Type 'exit' to quit.\n")
        while True:
            
            user_input = input("[YOU] ")
            if user_input == "exit":
                break
            self.messages.append({"role":"user", "content":user_input})
            response = client.chat.completions.create(
                model = self.model_key,
                messages=self.messages
            )
            model_response = response.choices[0].message.content
            self.messages.append({"role":"assistant", "content": model_response})
            print("[MODEL] " + model_response)
            if len(self.messages)>(2*self.max_turns + 1):
                self.messages.pop(1)
                self.messages.pop(1)

if __name__ == "__main__":
    models = {
        "Google Gemma 4": "google/gemma-4-31b-it:free", 
        "Open AI GPT oss": "openai/gpt-oss-120b:free", 
        "NVIDIA Nemotron 3": "nvidia/nemotron-3-super-120b-a12b:free"
    }
    
    print("Choose your model. Enter the number corresponding to the model you want.")
    for idx, name in enumerate(models.keys(), 1):
        print(f"{idx}. {name}")
        
    choice = int(input("Selection: ")) - 1
    selected_model = list(models.values())[choice]

    agent1 = ChatAgent(system_prompt="You are a helpful AI assistant.", max_turns=5, model_key=selected_model)
    agent1.call_model()

