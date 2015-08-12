
import subprocess, json, time

#https://wiki.appnexus.com/display/api/Log-Level+Data+Service

#days=['2013_07_22']
days=[time.strftime("%Y_%m_%d",time.localtime(int(time.time()-2*3600*24)))]
feeds=['standard_feed'] #'segment_feed'

#get feed file
b=subprocess.check_output("curl -b cookies -c cookies 'http://api.appnexus.com/siphon'",shell=True)
c=json.loads(b)

todo=[]
#process standard_feed
for i in c['response']['siphons']:
    hour=i['hour']
    ts=i['timestamp']
    name=i['name']
    if name in feeds:
        if hour[0:10] in days:
            for s in i['splits']:
                todo.append([name,hour,ts,s['part']])
        
print len(todo)
print todo

#find feed and download
for t in todo:
    subprocess.call("curl --verbose -b cookies -c cookies -D temp 'http://api.appnexus.com/siphon-download?siphon_name="+t[0]+"&hour="+t[1]+"&timestamp="+t[2]+"&split_part='"+t[3],shell=True)
    f1=open('temp','r')
    for line in f1:
        if 'Location:' in line:
            loc=line[10:]
            fn="feeds/"+t[0]+t[1]+t[3]+".gz"
            print t,loc,fn
            b=subprocess.check_output("curl -b cookies -c cookies "+loc,shell=True)
            f2=open(fn,'w')
            f2.write(b)
            f2.close()
    f1.close()
