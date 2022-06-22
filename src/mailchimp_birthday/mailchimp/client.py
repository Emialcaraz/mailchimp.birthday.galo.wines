from mailchimp_birthday.logger import get_logger
from mailchimp_birthday.settings import ServiceSettings
from mailchimp3 import MailChimp


class MailchimpClient:
    """Superclass Responsible for creating the mailchimp client"""

    def __init__(self) -> None:
        """
        Class Constructor
        """
        self.settings = ServiceSettings()
        self._logger = get_logger(self.__class__.__name__)

    def start_client(self):
        """
        Starts the Mailchimp client

        -------
        Returns
            client: Mailchimp
        """
        client = MailChimp(mc_api=self.settings.API_TOKEN.get_secret_value(), mc_user=self.settings.USERNAME)

        return client

