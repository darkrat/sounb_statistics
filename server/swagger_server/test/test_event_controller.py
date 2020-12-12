# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.event import Event  # noqa: E501
from swagger_server.test import BaseTestCase


class TestEventController(BaseTestCase):
    """EventController integration test stubs"""

    def test_add_event(self):
        """Test case for add_event

        Add a new event to the store
        """
        body = Event()
        response = self.client.open(
            '/v1/event',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_event(self):
        """Test case for delete_event

        Deletes a event
        """
        headers = [('api_key', 'api_key_example')]
        response = self.client.open(
            '/v1/event/{eventId}'.format(eventId=789),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_event_by_id(self):
        """Test case for get_event_by_id

        Find event by ID
        """
        response = self.client.open(
            '/v1/event/{eventId}'.format(eventId=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_search_events(self):
        """Test case for search_events

        Finds Events by params
        """
        query_string = [('startDate', 'startDate_example'),
                        ('endDate', 'endDate_example')]
        response = self.client.open(
            '/v1/event/search',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_event(self):
        """Test case for update_event

        Update an existing event
        """
        body = Event()
        response = self.client.open(
            '/v1/event',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_event_with_form(self):
        """Test case for update_event_with_form

        Updates a event in the store with form data
        """
        response = self.client.open(
            '/v1/event/{eventId}'.format(eventId=789),
            method='POST',
            content_type='application/x-www-form-urlencoded')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
