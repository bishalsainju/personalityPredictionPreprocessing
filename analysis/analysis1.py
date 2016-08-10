import csv

inpStatus = csv.reader(open('mypersonality_final.csv','r'), delimiter = ',', quotechar='"')
opStatus = csv.writer(open('analysis1.csv', 'w'), delimiter = ',', quotechar = '"')

usermap = {}

for row in inpStatus:
    break

opStatus.writerow(["UserID", "opn" , "copn", "con", "ccon", "ext", "cext", "agr", "cagr", "neu", "cneu"])
for row in inpStatus:
    userid = row[0]
    # status = row[1]
    ext = row[2]
    neu = row[3]
    agr = row[4]
    con = row[5]
    opn = row[6]
    e = row[7]
    n = row[8]
    a = row[9]
    c = row[10]
    o = row[11]

    if userid not in usermap:
        usermap[userid] = {}
        opStatus.writerow([userid, opn, o, con, c, ext, e, agr, a, neu, n])
