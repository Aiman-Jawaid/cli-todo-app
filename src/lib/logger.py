"""
Simple logging module for the todo application.
"""
import datetime
from typing import Optional


class TodoLogger:
    """
    Simple logger for the todo application.
    """

    def __init__(self, log_file: Optional[str] = None):
        """
        Initialize the logger.

        Args:
            log_file: Optional file to write logs to
        """
        self.log_file = log_file

    def log(self, level: str, message: str):
        """
        Log a message with the specified level.

        Args:
            level: Log level (INFO, ERROR, WARNING, etc.)
            message: Message to log
        """
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"[{timestamp}] {level}: {message}"

        # Print to console
        print(log_message)

        # Optionally write to file
        if self.log_file:
            try:
                with open(self.log_file, 'a', encoding='utf-8') as f:
                    f.write(log_message + '\n')
            except Exception:
                # If file logging fails, just print to console
                pass

    def info(self, message: str):
        """Log an info message."""
        self.log("INFO", message)

    def error(self, message: str):
        """Log an error message."""
        self.log("ERROR", message)

    def warning(self, message: str):
        """Log a warning message."""
        self.log("WARNING", message)

    def debug(self, message: str):
        """Log a debug message."""
        self.log("DEBUG", message)


# Global logger instance
logger = TodoLogger()