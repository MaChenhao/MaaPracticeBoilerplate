import platform, subprocess


def MsgBox(msg):
    if platform.system() == "Darwin":
        subprocess.run(["osascript", "-e", f'display dialog "{msg}"'])
    else:
        subprocess.run(
            [
                "powershell.exe",
                "-Command",
                f'(New-Object -ComObject WScript.Shell).Popup("{msg}", 0, "Action", 0)',
            ]
        )
