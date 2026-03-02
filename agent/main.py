import sys, subprocess

from maa.agent.agent_server import AgentServer
from maa.toolkit import Toolkit

import my_action
import my_reco


def main():
    try:
        subprocess.run(["adb", "shell", "cmd", "notification", "set_dnd", "alarms"])

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


if __name__ == "__main__":
    main()
