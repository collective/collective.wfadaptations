# -*- coding: utf-8 -*-
from collective.wfadaptations.interfaces import IWorkflowAdaptation
from zope import schema
from zope.interface import implements
from zope.interface import Interface


class IDummySchema(Interface):

    param = schema.TextLine(
        title=u"Dummy parameter",
        required=True)


class DummyWorkflowAdaptation(object):

    implements(IWorkflowAdaptation)

    schema = IDummySchema
    multiplicity = False
    reapply = False

    def patch_workflow(self, workflow_name, **parameters):
        self.patched = "{};{};{}".format(workflow_name, parameters['param'], self.reapply)
        return True, ''


class AnotherWorkflowAdaptation(object):

    implements(IWorkflowAdaptation)

    schema = None

    def patch_workflow(self, workflow_name, **parameters):
        return True, ''
