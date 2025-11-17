import sys, subprocess

from maa.agent.agent_server import AgentServer
from maa.toolkit import Toolkit

import my_action
import my_reco


def main():
    try:
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
