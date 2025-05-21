from maa.agent.agent_server import AgentServer
from maa.custom_action import CustomAction
from maa.context import Context
import json, time


@AgentServer.custom_action("task")
class MyCustomAction(CustomAction):
    def run(
        self,
        context: Context,
        argv: CustomAction.RunArg,
    ) -> bool:
        argv: dict = json.loads(argv.custom_action_param)
        tasks = argv["tasks"]
        if not isinstance(tasks, list):
            tasks = [tasks]
        for task in tasks:
            if context.run_task(task, argv.get("pipeline_override", {})).status.failed:
                return False
            time.sleep(1)
        return True
