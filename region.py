


import subprocess, json

f2=open('region_outp','w')

for s in range(0,201,100):
    a=subprocess.check_output("curl -b cookies -c cookies 'http://api.appnexus.com/region?country_code=GB&start_element="+str(s)+"'",shell=True)
    b=json.loads(a)
    for r in b['response']['regions']:
        name=r['name']
        code=r['code']
        f2.write(code+'\t'+name+'\n')

f2.close()
