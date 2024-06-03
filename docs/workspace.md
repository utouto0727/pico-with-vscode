# プロジェクトフォルダ・ファイルの設定

## プロジェクトフォルダを作成する。

Ubunttuで任意の場所にプロジェクトフォルダを作成してください。

``` bash
mkdir <pjfolder>
```

## プロジェクトをVSCodeで開く

作成したプロジェクトフォルダに移動します。

``` bash
cd <pjfolder>
```

フォルダをプロジェクトとして開きます。

```
code .
```

VSCodeが起動したらOKです。

## micropicoファイルの作成

プロジェクトフォルダ直下に以下のファイルを作成する。

- [.micropico](../.micropico): 拡張機能がプロジェクトフォルダを認識するために利用します。

## srcフォルダの作成

プロジェクトフォルダ直下に以下のフォルダを作成する

- src: ソースコードを格納するフォルダ。このプロジェクトでは、フォルダの中をPicoにアップロードするように`devcontainer.json`で設定します。


## 開発コンテナ起動に必要なフォルダ・ファイルを作成

### devcontainerフォルダ・ファイルの作成

- プロジェクトフォルダ直下に`.devcontainer`フォルダを作成する。

### devcontainerで利用するファイルの作成


`.devcontainer`フォルダ内に以下の2ファイルを作成します。記載内容はリンク先のファイルを参考に、適宜書き換えてください。

- [devcontainer.json](../.devcontainer/devcontainer.json): VSCodeの設定をjsonファイルの内容で自動で設定するために利用します。
- [Dockerfile](../.devcontainer/Dockerfile): 開発環境のコンテナファイルです。


ここまでで、以下のようなファイル構成になっていればOKです。
```
pjfolder
  ├ src
  ├ .micropico
  └ .devcontainer
    ├ devcontainer.json
    └ Dockerfile
```

## 開発コンテナを起動する

1. VSCode左下の`><`を押下する。
2. `コンテナーで再度開く`を選択する。


