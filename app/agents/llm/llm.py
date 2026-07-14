from openai import OpenAI

class CustomLLM:
    def __init__(self):
        self.client = OpenAI(
            base_url="http://35.253.171.20:8080/v1",
            api_key="hucdsbcdbchbdbkdfdb2",
            timeout=30.0,
        )

    def invoke(self, prompt):
        print("STEP 1: invoke entered")

        response = self.client.chat.completions.create(
            model="Qwen/Qwen2.5-7B-Instruct",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=512,
            temperature=0.3,
        )

        print("STEP 2: response received")

        class Response:
            def __init__(self, content):
                self.content = content

        return Response(response.choices[0].message.content)

llm = CustomLLM()
