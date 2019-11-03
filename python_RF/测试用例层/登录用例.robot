*** Settings ***
Resource    ../页面对象层/登录页面关键字.robot
Variables    ../测试数据层/登录数据.py
Variables    ../测试数据层/公共数据.py
Library    myExcelLibrary.py    

Test Setup    Open Browser    ${web_login_url}    gc
Test Teardown    Close Browser

Force Tags    login    demo    

*** Test Cases ***
正常用例-登录成功
    [Tags]    smoke
    登录页面关键字.登录操作    ${success_data.user}    ${success_data.passwd}
    
异常用例-用户名为空
    登录页面关键字.登录操作    ${phone_data[2]["user"]}    ${phone_data[2]["check"]}
    ${msg}=    登录页面关键字.获取错误信息提示-来自登录区域
    Should Be Equal    ${phone_data[0]["check"]}    ${msg}

用例3-读取-v参数传进来的全局变量
    [Tags]    vv
    Log    ${web_url}   
    
用例4-使用自定义库的关键字
    [Tags]    my
    ${sum}=    Add TwoNum    12    14 