import os

'''
定数は大文字で定義する
定数は
'''
# csv_path
SOURCE_CSV_PATH = "source.csv"
# csvが存在しない場合の初期データ
DEFAULT_CARACTORS = ["ぜんいつ","たんじろう","ねずこ","いのすけ","かがや","ぎゆう"]

'''
処理は細かく関数化する
関数化のポイント、関数内には具体的な内容は記述せずに引数に持たせる
この処理でしか使えなくなってしまうような記述は極力避けて
別のプロジェクトに使い回す前提で記述する
'''
def read_source(csv_path:str):
    '''
    sourceをCSVから読み込む
    関数の基本は、引数(今回はcsv_path) → 処理(関数の中身) → 戻り値(return)
    '''
    # ファイルが存在しない場合は、初期値で新規作成
    if not os.path.exists(csv_path):
        print(f"csv_path:{csv_path} が存在しません。新規作成します。")
        write_source(csv_path, DEFAULT_CARACTORS)
    # ファイルを読み込み
    with open(csv_path, 'r', encoding="utf-8_sig") as f:
        return f.read().splitlines() # readでファイル読み込み、splitlinesで１行づつに分解してlistとして返す

def write_source(csv_path:str, source:list):
    '''
    sourceをcsvに書き込む
    "utf-8_sig"がないと文字化けする可能性がある
    modeのwはwriteの略
    '''
    with open(csv_path, mode='w', encoding="utf-8_sig") as f:
        f.write("\n".join(source)) # listを改行(\n)で連結してファイルに書き込む

    # 特に戻り値が必要ない場合はreturnは省略できる、その場合はNoneが返る


### 検索ツールサンプル
### これをベースに課題の内容を追記してください

# 検索ソース
source=["ねずこ","たんじろう","きょうじゅろう","ぎゆう","げんや","かなお","ぜんいつ"]

### 検索ツール
def search():
    
      # sourceをcsvから読み込む
    source = read_source(SOURCE_CSV_PATH)
    
    while True:
        
        word = input("鬼滅の登場人物の名前を入力してください >>> ")
    ### ここに検索ロジックを書く
    
        if word in source:
            print("{}が見つかりました".format(word))
        
        else:
            print("{}が見つかりません".format(word))
    
        choice = input("新しいキャラクターをリストに追加しますか？ 'yes' or 'no' [y/N]: ").lower()
        if choice in ["y", "ye", "yes"]:
            source.append(word)
            print(f"新しいキャラクター{word}を追加しました")
            
        elif choice in ['n', 'no']:
            return
        
        
        # sourceをcsvに書き込む
        write_source(SOURCE_CSV_PATH, source=source)
        
                

if __name__ == "__main__":
    search()
