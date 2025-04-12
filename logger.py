import logging
import os
from datetime import datetime


# Configure the root logger
def setup_logger(log_level=logging.INFO):
    # Create logs directory if it doesn't exist
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)

    # Create a formatted timestamp for the log filename
    timestamp = datetime.now().strftime("%Y-%m-%d")
    log_file = os.path.join(log_dir, f"app_{timestamp}.log")

    # Configure the logger
    logging.basicConfig(
        level=log_level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()  # Also output to console
        ]
    )

    return logging.getLogger()


# Create and configure our application logger
logger = setup_logger()