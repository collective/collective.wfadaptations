# -*- coding: utf-8 -*-
"""Test api."""
import unittest2 as unittest

from plone import api

from collective.wfadaptations.api import get_applied_adaptations
from collective.wfadaptations.api import add_applied_adaptation
from collective.wfadaptations.api import AdaptationAlreadyAppliedException
from collective.wfadaptations.testing import COLLECTIVE_WFADAPTATIONS_INTEGRATION_TESTING  # noqa


RECORD_NAME = 'collective.wfadaptations.applied_adaptations'


class TestAPI(unittest.TestCase):

    """Test API."""

    layer = COLLECTIVE_WFADAPTATIONS_INTEGRATION_TESTING

    def setUp(self):
        applied_adaptations = [
            {u'workflow': u'workflow1', u'adaptation': u'adaptation1'},
            {u'workflow': u'workflow1', u'adaptation': u'adaptation2'},
            {u'workflow': u'workflow2', u'adaptation': u'adaptation2'},
        ]
        api.portal.set_registry_record(
            RECORD_NAME, applied_adaptations)

    def test_get_applied_adaptations(self):
        applied_adaptations = get_applied_adaptations()
        self.assertIn(
            {u'workflow': u'workflow1', u'adaptation': u'adaptation1'},
            applied_adaptations,
            )

        self.assertIn(
            {u'workflow': u'workflow1', u'adaptation': u'adaptation2'},
            applied_adaptations,
            )

        self.assertIn(
            {u'workflow': u'workflow2', u'adaptation': u'adaptation2'},
            applied_adaptations,
            )

    def test_add_applied_adaptation(self):
        add_applied_adaptation(u'adaptation1', u'workflow2')
        self.assertIn(
            {u'workflow': u'workflow2', u'adaptation': u'adaptation1'},
            api.portal.get_registry_record(RECORD_NAME),
            )
        with self.assertRaises(AdaptationAlreadyAppliedException):
            add_applied_adaptation(u'adaptation1', u'workflow1')
