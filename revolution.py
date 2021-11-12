#curl -v -F _wpcf7_version=5.4.2 -F _wpcf7_locale=ru_RU -F _wpcf7_unit_tag=wpcf7-f1319-p2584-o1 -F _wpcf7_container_post=2584 -F 'your-name=Валентина Васильева' -F your-email=g56546hgh@yandex.ru -F 'your-message=не получается пройти регистрацию 2'  https://revolutexpert.co/ru/wp-json/contact-form-7/v1/contact-forms/1319/feedback
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
    req='curl -v -F _wpcf7_version=5.4.2 -F _wpcf7_locale=ru_RU -F _wpcf7_unit_tag=wpcf7-f1319-p2584-o1 -F _wpcf7_container_post=2584 -F \'your-name='+data["name"]+" "+data["surname"]+'\' -F your-email='+data["email"]+' -F \'your-message='+data["phrase"]+'\'  https://revolutexpert.co/ru/wp-json/contact-form-7/v1/contact-forms/1319/feedback'
    print (req)
    result = os.popen(req).read()
    print(result)
#    time.sleep(10)
    if ('"success":true' in result):
        print(":::::::::::: reg OK::::::::::::::")
        print (data['email'])
        print (data['password'])
        _cred("gravity",data['email'],data['password'])
