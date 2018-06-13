import sys
import json
reload(sys)
sys.setdefaultencoding('utf8')
ma_truong = "360"
fo = open('list_'+ma_truong+'.txt', 'r')
g = fo.read()
fo.close()
fw = open('done_'+ma_truong+'.csv', 'a')
fw.write("SBD,NAME,DOB,UT,KK,VAN,ANH,TOAN\n")
fw.close()
for i in g.split("\n"):
	if i!="":
		j = json.loads(i)
		cr = j['rs'][0]['r']
		fw = open('done_'+ma_truong+'.csv', 'a')
		fw.write(cr[0]+',"'+cr[1]+'","'+cr[2]+'","'+cr[3]+'","'+cr[4]+'","'+cr[5]+'","'+cr[6]+'","'+cr[7]+'"\n')
		fw.close()

