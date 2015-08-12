
#https://wiki.appnexus.com/display/api/Advertiser+Service

import subprocess, json

f1=open('adv','r')
f2=open('advertiser_outp','w')

for line in f1:
	id=line.strip()
	a=subprocess.check_output("curl -b cookies -c cookies 'http://api.appnexus.com/advertiser?id="+id+"'",shell=True)
	b=json.loads(a)
	name=b['response']['advertiser']['name']
	f2.write(id+'\t'+name+'\n')

f1.close()
f2.close()
