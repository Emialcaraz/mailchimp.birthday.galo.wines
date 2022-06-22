from mailchimp_birthday.logger import get_logger
from mailchimp_birthday.settings import ServiceSettings
import datetime
from mailchimp_birthday.utils.utils import get_data_for_campaign_birthday, create_segment
import uuid


class BirthdayMail:
    """Class Responsible for sending the "Birthday email" """

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

    def replicate_campaign(self, segment_id, month, day, name):
        """
        This method will take in the following parameters:

        - segment_id: The id of the segment that you want to target with the campaign.
        - month: The month that the campaign should be sent out.
        - day: The day of the month that the campaign should be sent out.
        - name: The name of the user that the campaign should be sent to.

        This method will return the campaign that was created.
        """
        self._logger.info("Replicating campaign")
        replicate_campaign = self.client.campaigns.actions.replicate(campaign_id=self.settings.CAMPAIGN_ID_BIRTHDAY)
        data = get_data_for_campaign_birthday(segment_id, month, day, name)
        update = self.client.campaigns.update(campaign_id=replicate_campaign["id"], data=data)

        self._logger.info(f"Sending campaigns to user {name} ")
        self.client.campaigns.actions.send(campaign_id=update["id"])

        return update

    def start_process(self):
        """
        This function starts the process, it will create a new segment for the given day and all the subscribers of that
        list. For each subscriber it will create a new segment and will send a new campaign to it, the campaign will have
        the same result if the same email was sent to all the subscribers, but the content will be different.

        The first time that the function is called it will create a new campaign that will be used from now on, then it will
        just replicate that campaign to the new segments created.
        """
        list_id = self.get_audience_id()
        d = datetime.datetime.now()
        month = d.strftime("%m")
        day = f'{d.day:02d}'

        segment_id = create_segment(self.client, list_id, month, day)

        members = self.client.lists.segments.members.all(list_id=list_id, segment_id=segment_id, get_all=False)

        for member in members["members"]:
            segment = self.client.lists.segments.create(
                list_id=list_id,
                data=
                {
                    "name": f"segmento usuario ({member['email_address']}) - {uuid.uuid4().hex.upper()[0:6]} ",
                    "options": {
                        "match": "all",
                        "conditions": [
                            {
                                "field": "merge0",
                                "op": "is",
                                "value": f"{member['email_address']}"
                            },
                        ]}
                })

            segment_id = segment["id"]
            name = member["merge_fields"]["FNAME"]
            self.replicate_campaign(segment_id, month, day, name)




