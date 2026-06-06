from datetime import datetime
from pathlib import Path


class ExecutionContext:
    def __init__(self) -> None:
        self.timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        self.execution_folder = Path(f"reports/{self.timestamp}")
        self.screenshots_folder = self.execution_folder / "screenshots"
        self.videos_folder = self.execution_folder / "videos"
        self.logs_folder = self.execution_folder / "logs"

        self.create_folders()

    def create_folders(self):
        folders = [
            self.execution_folder,
            self.screenshots_folder,
            self.videos_folder,
            self.logs_folder,
        ]

        for folder in folders:
            folder.mkdir(parents=True, exist_ok=True)


# if __name__ == "__main__":
#     context = ExecutionContext()
