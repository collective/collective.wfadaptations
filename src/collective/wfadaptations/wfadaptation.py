# -*- coding: utf-8 -*-

from zope.interface import implements
from collective.wfadaptations.interfaces import IWorkflowAdaptation

from . import _


class WorkflowAdaptationBase(object):

    implements(IWorkflowAdaptation)

    schema = None  # must be replaced with empty Schema

    def check_state_in_workflow(self, workflow, state_name):
        """ Check if state_name is a state of workflow """
        if state_name not in workflow.states:
            message = _("The workflow id '${id}' (${title}) doesn't contain the state '${state}'.",
                        mapping={'id': workflow.id, 'title': workflow.title, 'state': state_name})
            return message
        else:
            return ''
