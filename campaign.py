
#https://wiki.appnexus.com/display/api/Campaign+Service

import subprocess, json

f1=open('adv','r')
f2=open('campaign','w')

for line in f1:
    id0=line.strip()
    a=subprocess.check_output("curl -b cookies -c cookies 'http://api.appnexus.com/campaign?advertiser_id="+id0+"'",shell=True)
    b=json.loads(a)
    for i in b['response']['campaigns']:
        id=str(i['id'])
        name=i['name']
        f2.write(id0+'\t'+'\t'.join([id,name])+'\n')

f1.close()
f2.close()
