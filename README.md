WSL+VSCodeを使って速攻Raspberry Pi PicoでLチカしたときのメモ。
MicroPythonを使用

## 事前準備

- [Windows](./docs/beforesetting_windows.md)
  - WSL+Ubuntu
  - VSCode
- [Ubuntu](./docs/beforesetting_ubuntu.md)
  - DockerEngine
- [Raspberry Pi Pico](./docs/beforesetting_pico.md)
  - ファームウェアの更新

## デバイス接続～開発コンテナの設定
1. [デバイス接続](./docs/usbipd.md)
2. [ワークスペースのセットアップ](./docs/workspace.md)

## デバイス再接続時

### 同じ差込口に再接続した場合

アタッチからやり直す。

``` PowerShell
usbipd attach --wsl --busid <BUSID>
```

#### 異なる差込口に挿した場合

異なる差込口を使った場合はバインドからやり直す必要がある。

BUSIDを調べる

``` PowerShell
usbipd list
```

バインドする

``` PowerShell
usbipd bind --busid <BUSID>
```

アタッチする

``` PowerShell
usbipd attach --wsl --busid <BUSID>
```

## 参考
* [USB デバイスを接続する](https://learn.microsoft.com/ja-jp/windows/wsl/connect-usb)