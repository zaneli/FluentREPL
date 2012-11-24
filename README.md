#FluentREPL
SublimeREPL を少し使いやすくするための[Sublime Text 2](http://www.sublimetext.com/2 "Sublime Text 2") 用パッケージです。  
(FluentREPL は SublimeREPL のインストールを前提としています。)  
現時点では Haskell ソースコード用の機能のみ提供しています。  

#インストール方法
Sublime Text 2 のパッケージディレクトリ内に FluentREPL ディレクトリを配置してください。  

#使用方法
現時点での機能は以下の 2 つです。  
いずれも Haskell 用 SublimeREPL を起動している場合のみ動作します。  

##型情報の表示
Haskell ソースコード上の関数にカーソルが当たった状態で Ctrl + Shift + Alt + 「T」を押下することで、  
SublimeREPL で開いた GHCi に該当関数の :t(:type) コマンドを実行し、型情報を表示します。  
(ショートカットキーは Default (<OS名>).sublime-keymap ファイルを編集することで変更可能です。)  

##ソースコード編集後の自動ロード
Haskell ソースコードを編集後、保存時に SublimeREPL で開いた GHCi に :l(:load) コマンドを実行し、  
自動的に編集後のソースコードを GHCi に反映させます。