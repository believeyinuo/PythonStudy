*** Settings ***
Library    SeleniumLibrary    10
Resource    ../元素定位层/标页面_元素定位.robot

*** Keywords ***
获取用户余额
    Wait Until Element Is Visible    ${金额输入框}    20
    ${res}=    Get Element Attribute    ${金额输入框}    data-amount
    [Return]    ${res}

投资操作
    [Arguments]    ${money}
    Wait Until Element Is Visible    ${金额输入框}    20
    Input Text    ${金额输入框}    ${money}
    Click Element    ${投标按钮}
  
投资成功弹出框-点击查看并激活按钮
    Wait Until Element Is Visible    ${投资成功弹出框-查看并激活按钮}    20
    Click Element    ${投资成功弹出框-查看并激活按钮}