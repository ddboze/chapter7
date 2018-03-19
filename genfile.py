#!/usr/local/bin/python3
# coding: UTF-8

import sys # モジュール属性 argv を取得するため

argvs = sys.argv  # コマンドライン引数を格納したリストの取得
argc = len(argvs) # 引数の個数
# デバッグプリント

print ("argc : " , str(argc))

if (argc != 2):   # 引数が足りない場合は、その旨を表示
    print ('Usage: # python 5000')
    quit()

if not isinstance(int(argvs[1]), int):
    print ('Usage: # python integer')
    print(isinstance(argvs[1], int))
    quit()

#print ('Hello, Python')
#import syslog

#syslog.openlog(1,'test')

str1 = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA SEQNO="
str2 = " ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ"

maxlen = 100000000
# 最大桁を得る
max_len = len(str(maxlen))
i = 0
seq = 0
seqNo = str(seq).zfill(max_len)
print ("seqNo : " , seqNo)

f = open('./text.txt', 'w') # 書き込みモードで開く

for i in range(int(argvs[1])):
    #seqNo = str(seq).zfill(max_len)
    seqNo = str(seq).zfill(max_len)
    strline = str1 + seqNo + str2 + '\n'
    f.writelines(strline) # 引数の文字列をファイルに書き込む
    seq+=1

f.close() # ファイルを閉じる
