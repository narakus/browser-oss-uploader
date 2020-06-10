# brower-oss-uploader
这是通过浏览器直接上传阿里云oss的工具，需要配置下bucket相应权限，已经对应role角色以及sts



### 如何配置：

1. 创建一个阿里云ram角色，并赋予相应oss权限，可以参考如下策略，获取RoleArn

   ```json
   {
       "Version": "1",
       "Statement": [
           {
               "Sid": "允许获取myphotos中的信息, 访问源必须在允许的IP段中",
               "Effect": "Allow",
               "Action": [
                   "oss:ListObjects",
                   "oss:GetObject",
                   "oss:DeleteObject",
                   "oss:ListParts",
                   "oss:AbortMultipartUpload",
                   "oss:PutObject"
               ],
               "Resource": [
                   "acs:oss:*:*:example-bucket",
               ]
           }
       ]
   }
   ```

2. 创建阿里云子账号，用于调用sts服务，并赋予AliyunSTSAssumeRoleAccess权限，生成该账号的ak，sk

3. 修改config.py ，将RoleArn、Role、ak、sk、StsOssEndPoint、OssEndPoint对应信息修改，role是阿里云ram角色名称，StsEndPoint、OssEndPoint 可以在阿里云官方查到，例如北京地区的StsEndPoint为：sts.cn-beijing.aliyuncs.com

4. 配置bucket cors ，请参考：https://help.aliyun.com/document_detail/31925.html?spm=a2c4g.11186623.6.634.lNfXyE

5. 添加多地区bucket需要修改templates/index.html文件下35行以及111行记录  



### 如何使用：



![img](https://github.com/narakus/brower-oss-uploader/blob/master/example.gif)



- 参考：https://help.aliyun.com/document_detail/31925.html?spm=a2c4g.11186623.6.634.lNfXyE
