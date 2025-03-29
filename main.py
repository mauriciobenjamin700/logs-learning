from src.logging import LogManager


LogManager.create_info_log(
    action="test_action",
    local="test_local",
    agente="test_agente",
    agente_role="test_role",
    request_time=0.123456
)

LogManager.create_error_log(
    action="test_action",
    local="test_local",
    agente="test_agente",
    agente_role="test_role",
    status=404,
    detail="Not Found"
)