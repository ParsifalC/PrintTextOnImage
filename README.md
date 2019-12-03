# PrintTextOnImage

## How To Build

```shell
pyinstaller --onefile --add-binary='/System/Library/Frameworks/Tk.framework/Tk':'tk' --add-binary='/System/Library/Frameworks/Tcl.framework/Tcl':'tcl' --add-data='/YourRepoPath/res':'res' PrintTextOnImage.py
```

## How To Use

Copy /dist/PrintTextOnImage to your `/usr/local/bin`
