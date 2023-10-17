import re
"""
1.题目描述：
在开发过程中，经常会出现让用户进行使用邮箱进行用户注册的行为。
邮箱的格式一般为: xxxx@xxx.xx 或 xxxx@xxx.xx.xx的形式
实例代码，用来验证用户输入的邮箱是否正确。
"""
def isCorrect(email: str):
    return True if re.fullmatch('\w+@\w{3}\.\w{2}$|\w+@\w{3}(\.\w{2}){2}$', email) else False