# -*- coding: utf-8 -*-
from zope.interface import implements

from collective.wfadaptations.interfaces import IWorkflowAdaptation


class DummyWorkflowAdaptation(object):

    implements(IWorkflowAdaptation)

    schema = None

    def patch_workflow(self):
        return


class AnotherWorkflowAdaptation(object):

    implements(IWorkflowAdaptation)

    schema = None

    def patch_workflow(self):
        return
