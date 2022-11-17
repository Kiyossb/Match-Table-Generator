# Match-Table-Generator
「Match Table Generator」はChallongeからトーナメントの情報を取得して対戦カードを席番号をテキストで出力するツールです。出力したテキストをDiscordなどで通知することでアナウンスを聞き逃した人も再確認することができます。

ツールのダウンロードは[こちらのこちらのreleasesページ](https://github.com/Kiyossb/Match-Table-Generator/releases)のAssetsからできます。

# 要求環境
- OS：Windows

# 使い方
①

  各項目を入力
  
  - ユーザー名入力
  - 
    Challongeのユーザー名
    
  -APIキー入力
  
    設定→デベロッパーAPIから発行できます
    
    （注：メールアドレスを連携しないと発行できません）
    
   - トーナメントID入力
   - 
     作成したトーナメントのURLの末尾
     
     （例：https://challonge.com/ja/〇〇〇〇〇←この部分）
     
        ↓
        
    「対戦カードを取得」を押す

②
  「+」「-」で対戦台の数を調整
  
  ドロップダウンで対戦カードを選択
  
        ↓
        
  「テキストを出力」を押す

③	

  表示された対戦台・対戦カードをコピーしてDiscordなどにペースト
  
  （補足：「テキストを出力」を押したときにクリップボードにコピーされています）

# Author
- [Twitter](https://twitter.com/kiyo_ssb)

# Licence
Match-Table-Generator is under [MIT license](https://github.com/Kiyossb/Match-Table-Generator/blob/main/LICENSE)
