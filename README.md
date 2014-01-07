#FluentREPL
SublimeREPL を少し使いやすくするための[Sublime Text 2](http://www.sublimetext.com/2 "Sublime Text 2") 用パッケージです。  
(FluentREPL は SublimeREPL のインストールを前提としています。)  
現時点では Haskell / F# ソースコード用の機能のみ提供しています。  

##インストール方法
Package Control がインストールされていることを前提としています。  

1. Command Pallete から Package Control: Add Repository を選択  
![Package Control: Add Repository を選択](http://www.zaneli.com/img/FluentREPL/installation_instruction1.png "Package Control: Add Repository を選択")

2. URL欄に FluentREPL リポジトリのURLを入力  
![FluentREPL リポジトリのURLを入力](http://www.zaneli.com/img/FluentREPL/installation_instruction2.png "FluentREPL リポジトリのURLを入力")

3. Command Pallete から Package Control: Install Package を選択  
![Package Control: Install Package を選択](http://www.zaneli.com/img/FluentREPL/installation_instruction3.png "Package Control: Install Package を選択")

4. FluentREPL を選択  
![FluentREPL を選択](http://www.zaneli.com/img/FluentREPL/installation_instruction4.png "FluentREPL を選択")

##使用方法
現時点での機能は以下の 2 つです。  
いずれも Haskell / F#  用 SublimeREPL を起動している場合のみ動作します。  

###型情報の表示(Haskell のみ)
Haskell ソースコード上の関数にカーソルが当たった状態で Ctrl + Shift + Alt + 「T」を押下することで、  
SublimeREPL で開いた GHCi に該当関数の :t(:type) コマンドを実行し、型情報を表示します。  
(ショートカットキーは Default (<OS名>).sublime-keymap ファイルを編集することで変更可能です。)  

###ソースコード編集後の自動ロード
ソースコードを編集後、保存時に自動的に編集後のソースコードを SublimeREPL に反映させます。
+ Haskell  
SublimeREPL で開いた GHCi に :l(:load) コマンドを実行します。
+ F#  
SublimeREPL で開いた F# Interactive に #load コマンドを実行します。
