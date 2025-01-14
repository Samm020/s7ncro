thank you [sam](https://github.com/Samm020/) for creating the automation for obby <3

---
### rules when using
1. keep roblox window focused as if you were actively playing
2. do not move camera angle, this usually ruins everything
3. roblox must be in windowed mode, (macro will resize it automatically at the beginning)
4. roblox must be running at minimum 20fps

### other info
- you will NOT be reconnected after a disconnect or the save error
- you can move the window anywhere even after starting the macro (just make sure window is fully visible)
- not timer based, will wait forever until it loads into a lobby
- does not use any other method besides scanning ui elements so you can scroll zoom in and out i guess.. just dont go into first person mode

# manual install
> [!note]
> please use any python version between 3.8 and 3.12 as DearPyGui 1.10.1 is not compatible with 3.13 and onwards
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
