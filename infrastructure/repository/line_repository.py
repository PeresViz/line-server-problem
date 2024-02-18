from typing import Optional


class LineRepository:
    def __init__(self, file_name: str):
        self.file_name = file_name

    def get_line(self, index: int) -> Optional[str]:
        """
        Retrieve a line from the text file based on the provided index.

        Args:
            index (int): The index of the line to retrieve.

        Returns:
            str: The text of the requested line, or None if the line is beyond the end of the file.
        """
        try:
            with open(self.file_name, 'r') as file:
                # Iterate over the file until reaching the desired line index
                line_num = 0
                for line in file:
                    if line.strip():  # Skip blank lines
                        if line_num == index:
                            return line.rstrip('\n')  # Remove newline character before returning
                        line_num += 1
                # Return None if the index is beyond the end of the file
                return None
        except FileNotFoundError:
            # Handle file not found error
            raise FileNotFoundError(f"File not found: {self.file_name}")
        except IOError as e:
            # Handle I/O errors
            raise IOError(f"Error reading file: {e}")
        except Exception as e:
            # Handle any other unexpected errors
            raise Exception(f"An unexpected error occurred: {e}")