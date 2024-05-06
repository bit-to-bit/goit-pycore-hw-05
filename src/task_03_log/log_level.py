'''Log levels module'''
import enum

@enum.unique
class LogLevel(enum.Enum):
    '''Log levels'''
    INFO    = "INFO"
    ERROR   = "ERROR"
    DEBUG   = "DEBUG"
    WARNING = "WARNING"
