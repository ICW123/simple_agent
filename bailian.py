import random
from http import HTTPStatus
from dashscope import Generation, api_key  # 建议dashscope SDK 的版本 >= 1.14.0
import os
from dotenv import load_dotenv
import dashscope

load_dotenv()

api_key = os.environ.get("DASHSCOPE_API_KEY")

def call_stream_with_messages():
    messages = [
        {'role': 'user', 'content': '你叫什么名字'}]
    responses = Generation.call(
        model = 'qwen1.5-7b-chat',
        messages=messages,
        seed=random.randint(1, 10000),  # set the random seed, optional, default to 1234 if not set
        result_format='message',  # set the result to be "message"  format.
        stream=True,
        output_in_full=True,  # get streaming output incrementally.\
        api_key=api_key
    )
    full_content = ''
    for response in responses:
        if response.status_code == HTTPStatus.OK:
            full_content += response.output.choices[0]['message']['content']
            print(response)
        else:
            print('Request id: %s, Status code: %s, error code: %s, error message: %s' % (
                response.request_id, response.status_code,
                response.code, response.message
            ))
    print('Full content: \n' + full_content)


if __name__ == '__main__':
    call_stream_with_messages()

# messages = [
#     {'role': 'system', 'content': 'You are a helpful assistant.'},
#     {'role': 'user', 'content': '你是谁？'}
#     ]
# response = dashscope.Generation.call(
#     # 若没有配置环境变量，请用百炼API Key将下行替换为：api_key="sk-xxx",
#     api_key=os.getenv('DASHSCOPE_API_KEY'),
#     model="qwen-plus", # 模型列表：https://help.aliyun.com/zh/model-studio/getting-started/models
#     messages=messages,
#     result_format='message'
#     )
# print(response)




