# -*- coding: utf-8 -*-
"""Base module for unittesting."""

from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2
from zope.configuration import xmlconfig

import collective.wfadaptations


class CollectiveWfadaptationsLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        xmlconfig.file(
            'configure.zcml',
            collective.wfadaptations,
            context=configurationContext
        )

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.wfadaptations:default')


COLLECTIVE_WFADAPTATIONS_FIXTURE = CollectiveWfadaptationsLayer()


COLLECTIVE_WFADAPTATIONS_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_WFADAPTATIONS_FIXTURE,),
    name='CollectiveWfadaptationsLayer:IntegrationTesting'
)


COLLECTIVE_WFADAPTATIONS_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_WFADAPTATIONS_FIXTURE,),
    name='CollectiveWfadaptationsLayer:FunctionalTesting'
)


COLLECTIVE_WFADAPTATIONS_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        COLLECTIVE_WFADAPTATIONS_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='CollectiveWfadaptationsLayer:AcceptanceTesting'
)
