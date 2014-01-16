#FluentREPL
SublimeREPL を少し使いやすくするための[Sublime Text 2](http://www.sublimetext.com/2 "Sublime Text 2"), [Sublime Text 3](http://www.sublimetext.com/3 "Sublime Text 3") 用パッケージです。  
(FluentREPL は SublimeREPL のインストールを前提としています。)  
Erlang, F#, Haskell, Scala ソースコード用の機能を提供しています。  

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
Erlang, F#, Haskell, Scala 用 SublimeREPL を起動している場合のみ動作します。  

###ソースコード編集後の自動ロード
ソースコードを編集後、保存時に自動的に編集後のソースコードを SublimeREPL に反映させます。
+ Erlang  
SublimeREPL で開いた Erlang shell に c(File) コマンドを実行します。
+ F#  
SublimeREPL で開いた F# Interactive に #load コマンドを実行します。
+ Haskell  
SublimeREPL で開いた GHCi に :l(:load) コマンドを実行します。
+ Scala  
SublimeREPL で開いた Scala REPL に :load コマンドを実行します。
