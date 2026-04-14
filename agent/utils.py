import platform, subprocess, ctypes


def MsgBox(msg):
    if platform.system() == "Darwin":
        subprocess.run(["osascript", "-e", f'display alert "{msg}"'])
    else:
        ctypes.WinDLL("user32").MessageBoxW(None, msg, "Title", 0x1000)
