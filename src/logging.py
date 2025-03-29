import logging
from logging.handlers import RotatingFileHandler

class LogManager:
    """
    A class to manage logging in the application.
    Provides methods to log messages at different levels (INFO, ERROR, etc.)
    to separate log files.
    
    - Attributes:
        - _loggers:: dict: A dictionary to store logger instances.
        
    - Methods:
        - _get_logger(level: str, file_path: str): 
            Returns a logger instance for the specified level and file path.
        - create_info_log(action: str, local: str, agente: str, agente_role: str, request_time: float):
            Logs an INFO message to the info log file.
        - create_error_log(action: str, local: str, agente: str, agente_role: str, status: int, detail: str):
            Logs an ERROR message to the error log file.
    - Example:
        - LogManager.create_info_log("action", "local", "agente", "role", 0.123)
        - LogManager.create_error_log("action", "local", "agente", "role", 404, "Not Found")
    """
    
    _loggers = {}

    @classmethod
    def _get_logger(cls, level: str, file_path: str):
        if level not in cls._loggers:
            logger = logging.getLogger(level)
            logger.setLevel(getattr(logging, level))
            
            # Configuração do handler com rotação de arquivos
            handler = RotatingFileHandler(file_path, maxBytes=5_000_000, backupCount=5)
            formatter = logging.Formatter('%(asctime)s---%(levelname)s---%(message)s')
            handler.setFormatter(formatter)
            
            logger.addHandler(handler)
            cls._loggers[level] = logger
        
        return cls._loggers[level]

    @classmethod
    def create_info_log(cls, action: str, local: str, agente: str, agente_role: str, request_time: float):
        """
        Log an INFO message.
        
        - Args:
            - action:: str: The action being logged.
            - local:: str: The local context of the action.
            - agente:: str: The agent involved in the action.
            - agente_role:: str: The role of the agent.
            - request_time:: float: The time taken for the request.
        - Returns:
            - None
        """
        log_message = f"{action}---{local}---{agente}---{agente_role}---{request_time}"
        logger = cls._get_logger("INFO", "src/logs/info.log")
        logger.info(log_message)

    @classmethod
    def create_error_log(cls, action: str, local: str, agente: str, agente_role: str, status: int, detail: str):
        """
        Log an ERROR message.
        
        - Args:
            - action:: str: The action being logged.
            - local:: str: The local context of the action.
            - agente:: str: The agent involved in the action.
            - agente_role:: str: The role of the agent.
            - status:: int: The HTTP status code.
            - detail:: str: Additional details about the error.
        - Returns:
            - None
        """
        log_message = f"{action}---{local}---{agente}---{agente_role}---{status}---{detail}"
        logger = cls._get_logger("ERROR", "src/logs/error.log")
        logger.error(log_message)