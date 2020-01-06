## 定期的にツイッターからツイートを読み込みtxtファイルに書き込みを行っている
## 作成されるファイル名
from requests_oauthlib import OAuth1Session,OAuth1
import json
import requests
import urllib
import MeCab
import sys
import time
import pandas
import numpy as np
import re



# キーワード必要が必ず必要
# 検索ワードを引数として関連するツイートを表示する関数
def twitter_search_write(word):
    # APIキーの設定
    CK="uevzqM4e45MnY28kQabaZtYLS"   # consumer_kek
    CKS="3wLtgdVy9YIinxRMlixkAgW7ccqnIqLHJrCyQdvgzdK0wlPDC6" # consumer_key_secret
    AT="1197830297489793025-LQqsFzfr9ovYoazielLfOgl5nX4zpI"  # access_token
    ATC="f3txNcNdH0Ulw7S8zqclFdJsgXDiAnYdvVgp2sPmLP0Tf" # access_token_secret

    # URLの指定　自分の情報、キーワードを投げる→twittetに送る情報
    url="https://api.twitter.com/1.1/search/tweets.json?count=100&q=" + word    #countは返す個数、keywordはキーワード
    auth= OAuth1(CK,CKS,AT,ATC)
    response=requests.get(url, auth = auth)
    change_char =dict.fromkeys(range(0x10000,sys.maxunicode + 1),0xfffd)
    
    # responseにtwitterからのデータが送られてくる
    data = response.json()['statuses']
    
    for tweet in data:
    # テキスト部分を表示
        print(tweet["text"])
        
        x=(tweet["text"].translate(change_char))
        
        # #file=open("today.txt","a",encoding='UTF-8') #ファイルを開く、なければ作成、書き込むだけなら"w"追加するなら"a"(append),読み取るなら"r"次に言語指定
        file.write(x)
        #file.close()
    
#図る前の時間を取得
Start_Time=time.time()

#x=input("検索ワードを入力してください")


k=0
x=["に","を","が","な","あ","ま","め","そ","る","た","ば","き","そ","し","な","が","同志社","雨","芸人","ゲーム","トレンド",\
    "歌手","流行","アニメ","テレビ","学校","大学","高校","自分","思春期","が","ぼく","私","俺","ニート","社会","ブラック","会社","バイト","アルバイト","サークル",\
        "ハッシュタグ","日本","アメリカ","世界","医者","社会","同志社","ブラック","社会","人間","ブラック","ＯＮＥ","team","究極","死","渋谷","ちびまるこちゃん",\
            "行列","グルメ","ラーメン","流行","正規","偽","政治家","アベノミクス","アベンジャーズ","アメコミ","実現","を","あ","い","う","え","お","か","き","つ","く","け","こ",\
                "さ","し","す","せ","そ","た","ち","つ","て","と","な","に","ぬ","ね","の","ま","み","む","め","も","や","ゆ","よ","が","ぎ","ん","を","ぐ"]
#ここから繰り返し　本来ならrange(10000~),sleep(900)程度で
#"w"なら毎回ファイルを上書き"a"ならファイルを上書き
file=open("today.txt","a",encoding='UTF-8') #ファイルを開く

for i in range(0,50000):
    
    twitter_search_write(x[k])
    time.sleep(10)
    
    k=k+1
    
    if i%10==0:
        #時間取得
        End_Time=time.time()
        #計算して表示
        a=(End_Time-Start_Time)/60
        print("途中経過　経過時間"+str(a)+"分")
    
    #仮の配列で回している
    if k==100:
        k=0


file.close()
