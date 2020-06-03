#coding=utf-8

import oss2
from config import *
from aliyunsdkcore import client
from flask import Flask,render_template,request
from aliyunsdkcore.profile import region_provider
from aliyunsdksts.request.v20150401 import AssumeRoleRequest

# 配置要访问的STS Endpoint
region_provider.add_endpoint('Sts', RegionId, StsOssEndPoint)
# 初始化Client
clt = client.AcsClient(AccessKeyId,AccessKeySevcret, RegionId)

app = Flask(__name__)

@app.route('/',methods=['GET'])
def show_page():
    return render_template('index.html')

@app.route('/sts',methods=['GET'])
def get_token():

    # 构造"AssumeRole"请求
    ali_request = AssumeRoleRequest.AssumeRoleRequest()
    # 指定角色
    ali_request.set_RoleArn(RoleArn)
    # 设置会话名称，审计服务使用此名称区分调用者
    ali_request.set_RoleSessionName(Role)
    # 发起请求，并得到response
    ali_response = clt.do_action_with_exception(ali_request)
    return ali_response


#这里加参数获取endopoint,bucket
@app.route('/sign',methods=['GET'])
def sign_url():
    file_name = request.args.get('name')
    bucket_name = request.args.get('bucket')
    endpoint = request.args.get('endpoint')
    auth = oss2.Auth(AccessKeyId, AccessKeySevcret)
    bucket = oss2.Bucket(auth, endpoint, bucket_name)
    return bucket.sign_url('GET',file_name,TimeOut)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5002)
