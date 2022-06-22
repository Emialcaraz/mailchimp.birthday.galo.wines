from mailchimp_birthday.logger import configure_logger, get_logger
from mailchimp_birthday.settings import ServiceSettings
from mailchimp_birthday.mailchimp.client import MailchimpClient
from mailchimp_birthday.mailchimp.celebrate_birthday import CelebrateBirthday
from mailchimp_birthday.mailchimp.day_birthday import BirthdayMail
import schedule
import time


class Orchestrator:
    """
    The class that coordinates the entire execution of the service
    """

    def __init__(self):
        """
        Class Constructor
        """
        self._settings = ServiceSettings()
        configure_logger(self._settings)
        self._logger = get_logger(self.__class__.__name__)
        self._client = MailchimpClient().start_client()
        self._celebrate_client = CelebrateBirthday(self._client)
        self._birthday_client = BirthdayMail(self._client)

    def start(self):
        """
        Start orchestrator and submodules
        """
        self._logger.info("Starting orchestrator...")

        schedule.every().day.at("19:00").do(self._celebrate_client.start_process())
        schedule.every().day.at("00:00").do(self._birthday_client.start_process())

        while True:
            schedule.run_pending()
            time.sleep(10)

    def stop(self):
        """Stop orchestrator and submodules"""
        self._logger.info("Stopping orchestrator...")

