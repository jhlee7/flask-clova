# -*- coding: utf-8 -*-
import unittest
from flask_clova.core import Clova

from datetime import datetime, timedelta
from mock import patch, MagicMock
import json


class FakeRequest(object):
    """ Fake out a Flask request for testing purposes for now """
    def __init__(self, data):
        self.data = json.dumps(data)


class TestCoreRoutines(unittest.TestCase):
    """ Tests for core Flask Clova functionality """


    def setUp(self):
        self.mock_app = MagicMock()
        self.mock_app.debug = True

        # XXX: this mess implies we should think about tidying up Ask._alexa_request
        self.patch_current_app = patch('flask_clova.core.current_app', new=self.mock_app)
        self.patch_current_app.start()


    @patch('flask_clova.core.flask_request',
           new=FakeRequest({'System': {'application': {'applicationId': 1}}}))
    def test_alexa_request_parsing(self):
        clova = Clova()
        clova._cek_request()

    def test_tries_parsing_on_valueerror(self):
        max_timestamp = 253402300800

        # should cause a ValueError normally
        with self.assertRaises(ValueError):
            datetime.utcfromtimestamp(max_timestamp)

        # should safely parse, assuming scale change needed
        # note: this assert looks odd, but Py2 handles the parsing
        #       differently, resulting in a differing timestamp
        #       due to more granularity of microseconds
        result = Ask._parse_timestamp(max_timestamp)
        self.assertEqual(datetime(1978, 1, 11, 21, 31, 40).timetuple()[0:6],
                         result.timetuple()[0:6])

        with self.assertRaises(ValueError):
            # still raise an error if too large
            Ask._parse_timestamp(max_timestamp * 1000)

    def tearDown(self):
        self.patch_current_app.stop()