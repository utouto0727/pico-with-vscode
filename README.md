WSL+VSCodeを使って速攻Raspberry Pi PicoでLチカしたい人向けのサンプルです。

## usbipd-winのインストール
``` PowerShell
winget install --interactive --exact dorssel.usbipd-win
```

``` PowerShell
usbipd list
```

```
usbipd bind --busid <BUSID>
```

```
usbipd attach --wsl --busid <BUSID>
```

## 参考
* [USB デバイスを接続する](https://learn.microsoft.com/ja-jp/windows/wsl/connect-usb)