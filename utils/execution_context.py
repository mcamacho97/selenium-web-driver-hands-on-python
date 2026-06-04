from datetime import datetime
from pathlib import Path


class ExecutionContext:
    def __init__(self) -> None:
        self.timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        self.execution_folder = Path(f"reports/{self.timestamp}")

        self.execution_folder.mkdir(parents=True, exist_ok=True)


# if __name__ == "__main__":
#     context = ExecutionContext()
