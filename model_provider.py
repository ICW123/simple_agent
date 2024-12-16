import dashscope
import os
from dashscope.api_entities.dashscope_response import Message
from pycparser.ply.ctokens import t_PERIOD

from prompt import user_prompt
import random
from http import HTTPStatus
from dotenv import load_dotenv
import json

load_dotenv()

class ModelProvider(object):
    def __init__(self):
        self.api_key = os.environ.get("API_KEY")
        self.model_name = os.environ.get("MODEL_NAME")
        self._client = dashscope.Generation()
        print(self.model_name)
        self.max_retry_time = 3


    def chat(self, prompt, chat_history):
        cur_retry_time = 0
        while cur_retry_time < self.max_retry_time:
            cur_retry_time += 1
            try:
                messages = [Message(role='system', content = prompt)]
                for his in chat_history:
                    messages.append(Message(role='user', content = his[0]))
                    messages.append(Message(role='assistant', content = his[1]))
                messages.append(Message(role='user', content = user_prompt))
                response = self._client.call(
                    model = self.model_name,
                    messages = messages,
                    api_key = self.api_key,
                )
                """
                {
                    "status_code": 200, 
                    "request_id": "8fbc8c5c-f667-9c81-ba10-d48fe24dbea4", 
                    "code": "", 
                    "message": "", 
                    "output": {
                        "text": null, 
                        "finish_reason": null, 
                        "choices": [{
                            "finish_reason": "stop", 
                            "message": {
                                "role": "assistant", 
                                "content": "我是通义千问，由阿里云研发。"
                                    }
                                }]
                            }, 
                "usage": {
                    "input_tokens": 12, 
                    "output_tokens": 11, 
                    "total_tokens": 23
                    }
                }
                """
                out = response['output']['text']
                json.dumps(out)
                content = json.loads(response['output']['text'])
                return content
            except Exception as err:
                print("调用大模型出错: {}".format(err))
            return {}

