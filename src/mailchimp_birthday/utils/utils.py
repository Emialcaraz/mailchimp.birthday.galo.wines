import uuid


def get_data_for_campaign(segment_id, month):
    """
    This function generates the data payload dict that the MailChimp 3.0 API requires when creating a campaign.

    Parameters
    ----------
    segment_id : int
        The id of the MailChimp segment to which the campaign will be sent.

    month : int
        The numeric month for which the campaign will be sent.

    Returns
    -------
    dict
        The data payload dict that the MailChimp 3.0 API requires when creating a campaign.

    """
    data = {
        'recipients': {
            'segment_opts': {
                'saved_segment_id': segment_id,
                'match': 'all',
                'conditions': [
                    {
                        "field": "merge5",
                        "op": "starts",
                        "value": month
                    },
                ]
            }
        },
        'settings': {
            'subject_line': 'Celebrá tu cumpleaños en Galo',
            'title': f'Celebra tu cumpleaños en Galo (mes {month})',
            'from_name': 'Emiliano',
            'reply_to': 'emilianoalcaraz@hotmail.com',
        }
    }
    return data


def get_data_for_campaign_birthday(segment_id, month, day, name):
    """
    This function will create a dict for mailchimp segment based on the month and day passed as argument

    Parameters
    ----------
    segment_id
        mailchimp segment id
    month : string
        month of the contact birthday
    day : string
        day of the contact birthday
    name : string
        name of the person
    Returns
    -------
    data : dict
        the dict to create the segment
    """
    data = {
        'recipients': {
            'segment_opts': {
                'saved_segment_id': segment_id,
                'match': 'all',
                'conditions': [
                    {
                        "field": "merge5",
                        "op": "is",
                        "value": f"{month}/{day}"
                    },
                ]
            }
        },
        'settings': {
            'subject_line': f'Feliz cumpleaños {name}',
            'title': f'Feliz cumpleaños {name}',
            'from_name': 'Galo Wines',
            'reply_to': 'emilianoalcaraz@hotmail.com',
        }
    }
    return data


def create_segment(client, list_id, month, day):
    """
    This function will create a segments in mailchimp list based on the month and day passed as argument

    Parameters
    ----------
    client : object
        mailchimp client
    list_id : string
        mailchimp list id
    month : string
        month of the contact birthday
    day : string
        day of the contact birthday

    Returns
    -------
    segment_id : string
        segment id of mailchimp segment created
    """
    segment = client.lists.segments.create(
        list_id=list_id,
        data=
        {
            "name": f"segmento ({month}/{day}) - {uuid.uuid4().hex.upper()[0:6]} ",
            "options": {
                "match": "all",
                "conditions": [
                    {
                        "field": "merge5",
                        "op": "is",
                        "value": f"{month}/{day}"
                    },
                ]}
        })

    segment_id = segment["id"]

    return segment_id
