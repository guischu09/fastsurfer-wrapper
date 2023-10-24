import argparse
import logging
import os
import time

logging.basicConfig(level=logging.INFO)


class FastSurferRunner:
    def __init__(self, args: argparse.Namespace):
        self.args = args

    def config_to_args(self):
        arguments = [
            f"--{attr} {getattr(self.args, attr)}"
            for attr in dir(self.args)
            if not callable(getattr(self.args, attr)) and not attr.startswith("__")
        ]
        return " ".join(arguments)

    def args_as_flags(self):
        arguments = []
        for attr in dir(self.args):
            if not callable(getattr(self.args, attr)) and not attr.startswith("__"):
                arguments.append(f"--{attr}")
                arguments.append(str(getattr(self.args, attr)))

        return arguments

    def make_command(self) -> str:
        flags = self.config_to_args()
        return f"bash FastSurfer/run_fastsurfer.sh {flags}"

    def run(self):
        command = self.make_command()
        logging.info(f"!>> Started running FastSurfer wrapper...")
        logging.info(f"!>> Running command: {command}")
        time.sleep(1)
        os.system(command)
