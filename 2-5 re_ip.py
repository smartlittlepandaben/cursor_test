import re
str1 = 'port-channel1.189      192.168.189.254 YES CONFIG up'
pattern = r'^(\S+)\s+(\d{1,3}(?:\.\d{1,3}){3}).*(up|down)$'

match = re.search (pattern,str1)

if match:
    interface = match.group(1)
    ip_add = match.group(2)
    status = match.group(3)

    print(f"接口：{interface}")
    print(f"IP地址: {ip_add}")
    print(f"状态:{status}")
    