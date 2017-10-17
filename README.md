# SCAU-Auth-App
华农学生身份认证app

## 快速上手:

1. 获取验证码:
GET: 192.168.232.2:8111/auth/get

  response:

        {
          "path": "/auth/image/ljg1esf5c1rasxak2jbkcq45",   //验证码地址
          "session": "ljg1esf5c1rasxak2jbkcq45", 
          "view_state": "dDwtNTE2MjI4MTQ7Oz5gXe9/FvmCp4TSSLd1QQxdVAgCkA=="
        }

2. 验证:
POST: 192.168.232.2:8111/auth/post

param: 
    
    session: 第一步返回的数据
    
    view_state: 同上
    
    code: 验证码
           
    username: 学号
           
    passwd: 正方系统密码
           
           
    response:

        {
           "state": "success",
           "name": "xxx同学"
        }
