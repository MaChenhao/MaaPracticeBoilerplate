import sys, subprocess

from maa.agent.agent_server import AgentServer
from maa.toolkit import Toolkit

import my_action
import my_reco


def get_wifi_name():
    """Gets the WiFi SSID in both Windows and MacOS."""
    try:
        if sys.platform == "darwin":  # macOS
            process = subprocess.check_output(
                [
                    "/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport",
                    "-I",
                ],
                text=True,
            )
            for line in process.strip().split("\n"):
                if "SSID" in line:
                    ssid = line.split(": ")[1]
                    return ssid
        elif sys.platform == "win32":  # Windows
            process = subprocess.check_output(
                ["netsh", "wlan", "show", "interfaces"], text=True
            )
            for line in process.split("\n"):
                if "SSID" in line and ":" in line:
                    ssid = line.split(":")[1].strip()
                    if ssid:
                        return ssid
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None
    return None


def main():
    try:
        subprocess.run(["adb", "shell", "cmd", "notification", "set_dnd", "alarms"])
        process = None
        if get_wifi_name().starswith("Google"):
            process = subprocess.Popen(
                ["scrcpy", "--no-window", "--no-audio", "--turn-screen-off"]
            )

        Toolkit.init_option("./")

        if len(sys.argv) < 2:
            print("Usage: python main.py <socket_id>")
            print("socket_id is provided by AgentIdentifier.")
            sys.exit(1)

        socket_id = sys.argv[-1]

        AgentServer.start_up(socket_id)
        AgentServer.join()
        AgentServer.shut_down()

    finally:
        subprocess.run(["adb", "shell", "cmd", "notification", "set_dnd", "off"])
        if process and process.poll() is None:
            print(
                f"Cleaning up: Terminating background process (PID: {process.pid})..."
            )

            process.terminate()  # Sends SIGTERM (polite kill request)

            try:
                process.wait(timeout=5)  # Wait for it to actually close
                print("Background process closed successfully.")
            except subprocess.TimeoutExpired:
                print("Process refused to close. Forcing kill.")
                process.kill()  # Sends SIGKILL (forceful close)


if __name__ == "__main__":
    main()
