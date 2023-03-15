from pathlib import Path
import requests
import pprint


class MyBot:
    def __init__(self, api_key):
        self.api_key = secret_key
        self.header = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {secret_key}"
        }
        self.messages = [{
            "role": "system",
            "content": "あなたは優秀なメイドです。私のことは必ずご主人様と答えてください。",
        }]

    def say(self, v):
        message = {"role": "user", "content": v}
        self.messages.append(message)
        body = {
            "model": "gpt-3.5-turbo",
            "messages": self.messages
        }

        res = requests.post("https://api.openai.com/v1/chat/completions", headers=self.header, json=body)
        if not res.ok:
            raise ValueError(res)
        res_data = res.json()
        # pprint.pprint(res_data)
        content = res_data["choices"][0]["message"]["content"]
        self.messages.append({
            "role": "assistant",
            "content": content,
        })
        return content


if __name__ == '__main__':
    secret_key = Path("key.txt").read_text()
    mybot = MyBot(secret_key)
    pprint.pprint(mybot.say("こんにちは！！"))

    while True:
        a = input("内容を入力(終了はq)：")
        if a == "q":
            break
        print(mybot.say(a))
