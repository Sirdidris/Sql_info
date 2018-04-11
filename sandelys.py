import csv
import re


def getting_amount(file_name, list_name):
    with open ('C:\\Users\\Darijus\\Documents\\'+file_name+'.csv', newline='') as f:
        reader = csv.reader(f, delimiter=';', quotechar='t')
        reg = re.compile(r'[0-9]+\.+')
        i = 0
        list_name = []
        for row in reader:
            if len(row) > 10 and reg.match(row[1]):
                #print(re.sub(r'[0-9]+\.+', '', row[1], count=1)+" - "+row[8])
                list_name.append([re.sub(r'[0-9]+\.+', '', row[1], count=1), row[8]])
    #for k in range(len(list_name)):
    #    print (list_name[k])
    return list_name;

lala3 = getting_amount("DFV_0330", "lala")
lala4 = getting_amount("DCF2_0330", "lala2")

try:
    for k in lala3:
        for z in lala4:
            if z[0] in k:
                print (lala3.index(k))
                k.append(z[1])
                print (k)
            else:
                pass
except ValueError:
    print ("nera")
    pass
