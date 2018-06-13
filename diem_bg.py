import requests
import base64
ma_truong = "360"

for i in range(589):
	rr = requests.get('http://bacgiang.edu.vn/ssearch.ashx?iid=486&q='+ma_truong+('%03d'%(i+1))+'&pl=10').content
	fo = open('list_'+ma_truong+".txt", "a")
	fo.write(rr+"\n")
	fo.close()
	print rr