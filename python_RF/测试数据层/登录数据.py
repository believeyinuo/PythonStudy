# 正常场景 - 测试数据
DICT__success_data = {"user":"18684720553", "password":"python"}

# 异常用例-手机号码格式不正确(大于11位、小于11位、为空、不在号码段)
LIST__phone_data = [{"user":"186847205533", "password":"python", "check":"请输入正确的手机号"},
              {"user":"186847205", "password":"python", "check":"请输入正确的手机号"},
              {"user":"", "password":"python", "check":"请输入手机号"},
              {"user":"11684720553", "password":"python", "check":"请输入正确的手机号"},
              {"user":"18684720553", "password":"", "check":"请输入密码"}]

# 异常用例 - 错误的密码、账号未注册没有授权
LIST__wrong_data = [
    {"user":"18684720553", "passwd":"python111", "check":"账号或密码错误！"}, 
    {"user":"18600001100", "passwd":"python", "check":"此账号没有经过授权，请联系管理员！"}