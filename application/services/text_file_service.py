from infrastructure.repository.line_repository import LineRepository
import os


class TextFileService:
    def __init__(self):
        file_name = os.getenv("TEXT_FILE_NAME")
        self.line_repository = LineRepository(file_name)

    def get_line(self, index: int) -> str:
        """
        Get the text of the requested line.

        Args:
            index (int): The index of the line to retrieve.

        Returns:
            str: The text of the requested line, or None if the line is beyond the end of the file.
        """
        return self.line_repository.get_line(index)
