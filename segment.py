
#https://wiki.appnexus.com/display/api/Segment+Service

import subprocess, json

f1=open('segment','r')
f2=open('segment_outp','w')

for line in f1:
    seg=line.strip()
    a=subprocess.check_output("curl -b cookies -c cookies 'http://api.appnexus.com/segment?id='"+seg,shell=True)
    b=json.loads(a)
    print b
    name=b['response']['segment']['short_name']
    f2.write(seg+'\t'+name+'\n')

f1.close()
f2.close()
