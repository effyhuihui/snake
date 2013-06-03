__author__ = 'jfhuang'
fin = open('record.txt','r+')

score_dict = {}

for line in fin:
    temp = line.strip().split()
    print(temp)