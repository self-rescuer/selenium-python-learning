import logging
import os


def get_logger(name="api_framework"):
    logger = logging.getLogger(name)

    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        fmt="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # 日志文件路径：api_framework/logs/api_framework.log
    current_dir = os.path.dirname(os.path.abspath(__file__))
    log_dir = os.path.join(os.path.dirname(current_dir), "logs")
    os.makedirs(log_dir, exist_ok=True)

    file_handler = logging.FileHandler(
        os.path.join(log_dir, "api_framework.log"),
        encoding="utf-8"
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger