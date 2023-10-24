from FastSurfer.wrapper.fast_surfer_parser import (
    Configurations,
    parse_fast_surfer_arguments,
)
from FastSurfer.wrapper.fast_surfer_runner import FastSurferRunner


def main():
    arguments = parse_fast_surfer_arguments(config=Configurations())
    runner = FastSurferRunner(arguments)
    runner.run()


if __name__ == "__main__":
    main()
