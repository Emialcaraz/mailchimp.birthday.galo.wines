from enum import Enum

from pydantic import BaseSettings, SecretStr

from mailchimp_birthday import version


class LogLevelEnum(str, Enum):
    critical = "CRITICAL"
    error = "ERROR"
    warning = "WARNING"
    info = "INFO"
    debug = "DEBUG"


class EnvironmentTypeEnum(str, Enum):
    production = "production"
    development = "development"


class ServiceSettings(BaseSettings):
    """
    Settings class for the project.
    """

    VERSION = version.__version__
    ENV_TYPE: EnvironmentTypeEnum = EnvironmentTypeEnum.production

    API_TOKEN: SecretStr = ""

    CAMPAIGN_ID: str = ""
    CAMPAIGN_ID_BIRTHDAY: str = ""
    USERNAME: str = ""

    # Logging
    LOG_FILE: str = "mailchimp_birthday.log"
    LOG_LEVEL: LogLevelEnum = LogLevelEnum.info
    LOGGER_MSG_FORMAT: str = "%(name)s :: %(levelname)s :: %(message)s"

    class Config:
        use_enum_values = True
