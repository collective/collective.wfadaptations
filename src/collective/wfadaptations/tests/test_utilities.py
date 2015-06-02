# -*- coding: utf-8 -*-
"""Test utility."""
import unittest2 as unittest

from zope.component import getGlobalSiteManager, getUtility
from zope.interface import implements

from collective.wfadaptations.interfaces import IWorkflowAdaptation


class DummyWorkflowAdaptation(object):

    implements(IWorkflowAdaptation)

    schemas = []

    def patch_workflow(self):
        return


class TestUtility(unittest.TestCase):

    """Test workflow adaptation utility."""

    def test_register_utility(self):
        gsm = getGlobalSiteManager()
        my_wf_adaptation = DummyWorkflowAdaptation()
        gsm.registerUtility(
            my_wf_adaptation,
            IWorkflowAdaptation,
            'my_wf_adaptation')
        self.assertEqual(
            my_wf_adaptation,
            getUtility(IWorkflowAdaptation, 'my_wf_adaptation'))