import os, re
import sys
reload(sys)
sys.setdefaultencoding("utf8")

filenames1 = os.listdir("")
filenames2 = os.listdir("")
filenames_list1 = []
filenames_list2 = []

for name1 in filenames1:
    ok1 = re.search(r'\.naf$',name1)
    if ok1:
    	filenames_list1.append(name1[:-4])
for name2 in filenames2:
    ok2 = re.search(r'\.naf$',name2)
    if ok2:
    	filenames_list2.append(name2[:-8])

for i in filenames_list1:
	for j in filename2_list2:
		if i == j:
			os.remove(r'XXXXXX/' + i + '.naf')

print "execute successfully!"


