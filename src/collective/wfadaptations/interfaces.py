# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""
from zope.interface import Interface, Attribute
from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class ICollectiveWfadaptationsLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class IWorkflowAdaptation(Interface):

    """Interface for workflow adaptations."""

    schema = Attribute("""Associated schema that provides parameters for the
        workflow adaptation""")

    def patch_workflow(self):
        """Patch the workflow."""
        pass
