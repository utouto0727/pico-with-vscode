# usbipd-win

## usbipd-winのインストール

``` PowerShell
winget install --interactive --exact dorssel.usbipd-win
```

## Picoを接続

BOOTSELボタンは押さなくてOKです。

## BUSIDの確認

以下のコマンドでBUSIDを確認する。

``` PowerShell
usbipd list
```

どのデバイスかわからない場合は、デバイス抜き差しして前後に`usbipd list`をして増えてるものがどれかを確認してください。

## デバイスをバインドする

**管理者権限**のコマンドプロンプトから実行してください。

```
usbipd bind --busid <BUSID>
```

## デバイスをアタッチする

```
usbipd attach --wsl --busid <BUSID>
```

これでUbuntu側からもUSBデバイスが認識できるようになります。

## 参考
* [USB デバイスを接続する](https://learn.microsoft.com/ja-jp/windows/wsl/connect-usb)