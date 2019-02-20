#GPSRのコマンド実行
#生成された文を読む込，それをファイル出力する
#これを10000回す

import sys
import subprocess

def main():
    cmd = "python2.7 GPSRsentence_generator2015jp.py"
    #subprocess.call(cmd,shell=True)
    ret = subprocess.check_output( cmd.split(" ") )
    print(ret)



if __name__ == '__main__':
    main()
