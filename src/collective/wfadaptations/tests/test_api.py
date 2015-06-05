# -*- coding: utf-8 -*-
"""Test api."""
import unittest2 as unittest

from plone import api

from collective.wfadaptations.api import get_applied_adaptations
from collective.wfadaptations.api import add_applied_adaptation
from collective.wfadaptations.api import applied_adaptations_by_workflows
from collective.wfadaptations.api import AdaptationAlreadyAppliedException
from collective.wfadaptations.testing import COLLECTIVE_WFADAPTATIONS_INTEGRATION_TESTING  # noqa


RECORD_NAME = 'collective.wfadaptations.applied_adaptations'


class TestAPI(unittest.TestCase):

    """Test API."""

    layer = COLLECTIVE_WFADAPTATIONS_INTEGRATION_TESTING

    def setUp(self):
        applied_adaptations = [
            {u'workflow': u'workflow1',
             u'adaptation': u'adaptation1',
             u'parameters': u'{}'
            },
            {u'workflow': u'workflow1',
             u'adaptation': u'adaptation2',
             u'parameters': u'{}'
            },
            {u'workflow': u'workflow2',
             u'adaptation': u'adaptation2',
             u'parameters': u'{"param": "foobar"}'
            },
        ]
        api.portal.set_registry_record(
            RECORD_NAME, applied_adaptations)

    def test_get_applied_adaptations(self):
        applied_adaptations = get_applied_adaptations()
        self.assertIn(
            {u'workflow': u'workflow1',
             u'adaptation': u'adaptation1',
             u'parameters': {}
            },
            applied_adaptations,
            )

        self.assertIn(
            {u'workflow': u'workflow1',
             u'adaptation': u'adaptation2',
             u'parameters': {}
            },
            applied_adaptations,
            )

        self.assertIn(
            {u'workflow': u'workflow2',
             u'adaptation': u'adaptation2',
             u'parameters': {u"param": u"foobar"}
            },
            applied_adaptations,
            )

    def test_add_applied_adaptation(self):
        params = {'param1': 'foo', 'param2': 'bar'}
        add_applied_adaptation(u'adaptation1', u'workflow2', **params)
        self.assertIn(
            {u'workflow': u'workflow2',
             u'adaptation': u'adaptation1',
             u'parameters': u'{"param1": "foo", "param2": "bar"}'
            },
            api.portal.get_registry_record(RECORD_NAME),
            )
        with self.assertRaises(AdaptationAlreadyAppliedException):
            add_applied_adaptation(u'adaptation1', u'workflow1', **params)

    def test_applied_adaptations_by_workflow(self):
        expected = {
            u'workflow1': [u'adaptation1', u'adaptation2'],
            u'workflow2': [u'adaptation2']
            }
        self.assertEqual(expected, applied_adaptations_by_workflows())
