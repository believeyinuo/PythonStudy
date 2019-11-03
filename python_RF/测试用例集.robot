*** Settings ***
Library    RequestsLibrary

*** Test Cases ***
用例1-get请求
    Create Session    qcd    http://120.79.176.157:8080
    ${req_data}=    Create Dictionary    mobilephone=13700010000    pwd=123456789
    ${res}=    Get Request    qcd    futureloan/mvc/api/member/register    params=${req_data}
    Log    ${res}
    Log    ${res.text}
    Log    ${res.status_code}
    Log    ${res.json()}
    
用例2-post请求
    Create Session    qcd    http://120.79.176.157:8080
    ${req_data}=    Create Dictionary    mobilephone=13700010000    pwd=123456789
    ${res}=    Post Request    qcd    futureloan/mvc/api/member/register    data=${req_data}
    Log    ${res}
    Log    ${res.text}
    Log    ${res.status_code}
    Log    ${res.json()}
    