*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${用户名输入框}    //input[@name="phone"]
${密码输入框}    //input[@name="password"]
${登录按钮}    //button[text()="登录"]
${错误提示-登录表单区域}    //div[@class="form-error-info"]
${页面正中间的提示语}    //div[@class="layui-layer-content"]