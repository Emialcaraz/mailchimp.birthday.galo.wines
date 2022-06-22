from mailchimp_birthday.logger import get_logger
from mailchimp_birthday.settings import ServiceSettings
from datetime import timedelta, date
from mailchimp_birthday.utils.utils import get_data_for_campaign, create_segment


class CelebrateBirthday:
    """Class Responsible for sending the "celebrate campaign" """

    def __init__(self, client) -> None:
        """
        Class Constructor
        """
        self.settings = ServiceSettings()
        self._logger = get_logger(self.__class__.__name__)
        self.client = client

    def get_audience_id(self):
        """
        Get the first ID of the audience list

        -------
        Returns
            list_id: str
        """

        audience_lists = self.client.lists.all(get_all=True, fields="lists.name,lists.id")

        list_id = audience_lists["lists"][0]["id"]

        return list_id

    def replicate_campaign(self, segment_id, month):
        """
        This method will take in the following parameters:

        - segment_id: The id of the segment that you want to target with the campaign.
        - month: The month that the campaign should be sent out.

        This method will return the campaign that was created.
        """

        self._logger.info("Replicating campaigns")

        replicate_campaign = self.client.campaigns.actions.replicate(campaign_id=self.settings.CAMPAIGN_ID)
        data = get_data_for_campaign(segment_id, month)

        update = self.client.campaigns.update(campaign_id=replicate_campaign["id"], data=data)

        return update

    def start_process(self):
        """
        This method is for starting process of sending campaign with the segment created right now.

        The method calls the method get_audience_id to get the audience id,
        the method replicate_campaign to create the campaign,
        and finally the method send to send the campaign to users.
        """

        list_id = self.get_audience_id()

        end_date = date.today() + timedelta(days=10)
        month = end_date.strftime("%m")
        day = f'{end_date.day:02d}'

        segment_id = create_segment(self.client, list_id, month, day)

        members = self.client.lists.segments.members.all(list_id=list_id, segment_id=segment_id, get_all=False)

        if members["total_items"] > 0:
            campaign = self.replicate_campaign(segment_id, month)
            self._logger.info("Sending campaigns to users")
            self.client.campaigns.actions.send(campaign_id=campaign["id"])

