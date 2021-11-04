import urllib.request, json, os,time
cred_file="cred.txt"
endpoint="localhost:8000"
def _cred(s,u,p):
    fh=open(cred_file,"a",encoding="utf-8")
#    fh=open(logfile,"a")
#    text=str(datetime.datetime.now())+" "+str(message)+"\r\n"
    text=s+","+u+","+p+"\r\n"
#    _log(text)
    fh.write(text)
    fh.close()
    return True
while True:
    with urllib.request.urlopen(endpoint) as url:
        data = json.loads(url.read().decode())
        print(data)
        print(data["name"])
    time.sleep(10)
    req='curl -v -F post_id=119 -F form_id=62c2bb08 -F queried_id=119 -F form_fields[firstName]='+data['name']+' -F form_fields[lastName]='+data['surname']+' -F form_fields[contacts__email]='+data['email']+' -F form_fields[password]='+data['password']+ ' -F form_fields[address__countryCode]=RU -F form_fields[contacts__phone]='
+data['phone_full']+' -F form_fields[field_4]=on -F form_fields[field_1]=on -F form_fields[field_2]=on -F form_fields[field_3]=on -F form_fields[lang]=ru -F action=elementor_pro_forms_send_form -F referrer=https://clients.gravity-trade.com/ru -x 80.59.199.213:8080 https://clients.gravity-trade.com/wp-admin/admin-ajax.php'
    print (req)
    result = os.popen(req).read()
    print(result)
#    time.sleep(10)
    if ('"success":true' in result):
        print(":::::::::::: reg OK::::::::::::::")
        print (data['email'])
        print (data['password'])
        _cred("gravity",data['email'],data['password'])
