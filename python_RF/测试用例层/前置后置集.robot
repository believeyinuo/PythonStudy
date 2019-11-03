*** Settings ***
Library    SeleniumLibrary
Resource    ../页面对象层/登录页面关键字.robot

*** Keywords ***
打开浏览器并方位前程贷系统
    Open Browser
    登录页面关键字.登录操作    用户名    密码