from datetime import datetime

class LogManager:
    """
    A class to manage logging in the application.
    
    This class provides methods to log messages at different levels
    
    (INFO, ERROR, WARNING, DEBUG, CRITICAL, TRACE) to separate log files.
    
    Each log message includes a timestamp, the user actor, the action, the target and the message
    
    """
    __info_logs_path = "src/logs/info.log"
    __error_logs_path = "src/logs/error.log"
    
    @classmethod
    def create_info_log(
        cls,
        action: str,
        local: str,
        agente: str,
        agente_role: str,
        request_time: float
    ):
        """
        A method to log information messages.
        
        - Args:
            - agente: str: The user actor who performed the action
            - action: str: The action performed by the user actor
            - local: str: The local context of the action
            - agente_role: str: The role of the user actor
            - request_time: float: The time taken to process the request
        - Returns:
            - None
        """
        log_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"LOG_INFO---{action}---{local}---{agente}---{agente_role}---{request_time}---{log_time}\n"
        
        file = cls.__info_logs_path
            
        with open(file, "a") as f:
            f.write(log_message)

    @classmethod
    def create_error_log(
        cls,
        action: str,
        local: str,
        agente: str,
        agente_role: str,
        status: int,
        detail: str,
    ):
        """
        A method to log error messages.
        
        - Args:
            - action: str: The action performed by the user actor
            - local: str: The local context of the action
            - agente: str: The user actor who performed the action
            - agente_role: str: The role of the user actor
            - status: int: The HTTP status code of the error
            - detail: str: The detailed error message
        - Returns:
            - None
        """

        log_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"LOG_ERROR---{action}---{local}---{agente}---{agente_role}---{status}---{detail}---{log_time}\n"
        
        file = cls.__error_logs_path
            
        with open(file, "a") as f:
            f.write(log_message)