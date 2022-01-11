
### 検索ツールサンプル
### これをベースに課題の内容を追記してください

# 検索ソース
source=["ねずこ","たんじろう","きょうじゅろう","ぎゆう","げんや","かなお","ぜんいつ"]

### 検索ツール
def search():
    word =input("たんじろう")   
    ### ここに検索ロジックを書く
    if word in source:
        print("{}が見つかりました".format(word))
    else:
        print("{}が見つかりません".format(word))

    
   



if __name__ == "__main__":
    search()