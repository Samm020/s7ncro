# manual install
> [!note]
> please use any python3 version below 3.13 as DearPyGui 1.10.1 is not compatible
```bash
git clone https://github.com/phruut/s7ncro
```
```bash
cd s7ncro
```
```Pip Requirements
python -m pip install -r requirements.txt
```
```bash
python main.py
```

## compiled with nuitka
```bash
nuitka --onefile --windows-console-mode=disable --windows-icon-from-ico=res/s7ns.ico main.py
```
