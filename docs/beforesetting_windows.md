# Windows上の設定

## Ubuntuをインストール

``` PowerShell
wsl --install Ubuntu-22.04
```

## デフォルトユーザーをrootに設定

rootでの使用は自己責任でお願いします。

``` PowerShell
ubuntu2204 config --default-user root
```

# VSCode

## インストール

公式サイトからVSCodeをインストールする
[Download Visual Studio Code](https://code.visualstudio.com/download)

## 必要な拡張機能をインストールする

VSCodeを開き、拡張機能のアイコンを押下します。

![拡張機能のアイコン](./img/icon_extension.png)

必要な拡張機能である以下の二つをインストールします。
- devcontainer
- WSL

## 参考

- [Download Visual Studio Code](https://code.visualstudio.com/download)
- [WSLを使用してWindowsにLinuxをインストールする方法](https://learn.microsoft.com/ja-jp/windows/wsl/install)