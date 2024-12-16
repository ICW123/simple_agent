from tools import tools_map

response = {'action': {'name': 'write_to_file', 'args': {'filename': '理财计划.txt', 'content': '1. 评估财务状况\n2. 设定理财目标\n3. 制定投资策略\n4. 执行计划\n5. 定期审查和调整'}}, 'thoughts': {'plan': '首先制定一个基本的理财计划框架，然后根据用户的具体情况逐步完善。', 'criticism': '需要确保每个步骤都是实际可行的，并且能够根据用户的反馈进行调整。', 'speak': '我将为您制定一个基本的理财计划框架，接下来您可以根据自己的具体情况进行调整。', 'reasoning': '通过制定一个清晰的理财计划框架，可以帮助用户更好地理解和执行理财计划。'}, 'observation': '', 'answer': ''}

action_info = response.get('action')
action_name = action_info.get('name')
action_args = action_info.get('args')

func = tools_map.get(action_info.get('name'))

print(action_name)
func(**action_args)

