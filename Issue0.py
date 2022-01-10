#1変数の使い方

name1 = "ねずこ"
name2 = "ぜんいつ"

print(f"{name1}と{name2}は仲間です")
      
#2if文の使い方

if name2 == "むざん":
    print("仲間ではありません")


#3配列の使い方

name = ["たんじろう","ぎゆう","ねずこ","むざん"]
name.append("ぜんいつ") 

print(name)

#4for分の使い方

for charaname in name:
    print(charaname)
    
#5関数の使い方

def character():
    print("たんじろう")
    
character()

#6引数を使う関数の使い方

def test(hikisuu):
   if hikisuu in name:
        print(f"{hikisuu}は含まれます")

test("ぎゆう")