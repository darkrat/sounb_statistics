import connexion
import six

from swagger_server.models.event import Event  # noqa: E501
from swagger_server import util


def add_event(body):  # noqa: E501
    """Add a new event to the store

     # noqa: E501

    :param body: Event object that needs to be added to the store
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Event.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_event(eventId, api_key=None):  # noqa: E501
    """Deletes a event

     # noqa: E501

    :param eventId: Event id to delete
    :type eventId: int
    :param api_key: 
    :type api_key: str

    :rtype: None
    """
    return 'do some magic!'


def get_event_by_id(eventId):  # noqa: E501
    """Find event by ID

    Returns a single event # noqa: E501

    :param eventId: ID of event to return
    :type eventId: int

    :rtype: Event
    """
    return 'do some magic!'


def search_events(startDate=None, endDate=None):  # noqa: E501
    """Finds Events by params

    Multiple status values can be provided with comma separated strings # noqa: E501

    :param startDate: Status values that need to be considered for filter
    :type startDate: str
    :param endDate: Status values that need to be considered for filter
    :type endDate: str

    :rtype: List[Event]
    """
    return 'do some magic!'


def update_event(body):  # noqa: E501
    """Update an existing event

     # noqa: E501

    :param body: Event object that needs to be added to the store
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Event.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_event_with_form(eventId):  # noqa: E501
    """Updates a event in the store with form data

     # noqa: E501

    :param eventId: ID of event that needs to be updated
    :type eventId: int

    :rtype: None
    """
    return 'do some magic!'
