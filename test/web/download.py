
import requests
import os, shutil
# 监测url

#多行政区划 ca登陆页面
Dxzxh_url = 'http://bs.hebds.gov.cn/loginLtCert.action'

#ca 控件
cab_url = 'http://bs.hebds.gov.cn/login/CheckUKeyCtrl.CAB'

#hby ca
hby_ca = 'http://bsfw.hebds.gov.cn/wbcms/tmpRes/login/loginltcert.jsp'

#登陆页面
login= 'http://bsfw.hebds.gov.cn/wbcms'

urls = [Dxzxh_url, cab_url, hby_ca, login]
def saveFile(url, dir=r'd:'):
    response = requests.get(url)
    filename = os.path.join(dir, url.split('/')[-1])
    print(filename)
    with open(filename, 'wb') as f:
        f.write(response.content)

save_dir = r"d:\hbds"
if os.path.exists(save_dir):
    shutil.rmtree(save_dir)
os.mkdir(save_dir)


for url in urls:
    saveFile(url, save_dir)

# filename = r'D:\1.html'
# with open(filename, 'wb') as f:
#     f.write(response.content)


# def readCookietxt(file_path):
#     f = open(file_path, 'r')
#     cookies = {}
#     for line in f.read().split(';'):
#         name, value = line.strip().split('=',1)
#         cookies[name] = value
#     return cookies

# cookies = readCookietxt(r'D:\python\test\web\cookie.txt')
# print(cookies)

# response = requests.get(form_page, cookies=cookies)

# filename = r'D:\1.html'
# with open(filename, 'wb') as f:
#     f.write(response.content)

#00版本