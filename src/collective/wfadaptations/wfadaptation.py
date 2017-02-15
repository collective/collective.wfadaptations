# -*- coding: utf-8 -*-

from zope.interface import implements
from collective.wfadaptations.interfaces import IWorkflowAdaptation

from . import _


class WorkflowAdaptationBase(object):

    implements(IWorkflowAdaptation)

    schema = None  # must be replaced with empty Schema

    def check_state_in_workflow(self, workflow, state_name):
        """ Check if state_name is a workflow state"""
        if state_name not in workflow.states:
            message = _("The workflow id '${id}' (${title}) doesn't contain the state '${state}'.",
                        mapping={'id': workflow.id, 'title': workflow.title, 'state': state_name})
            return message
        else:
            return ''

    def check_transition_in_workflow(self, workflow, transition_name):
        """ Check if transition_name is a workflow transition """
        if transition_name not in workflow.transitions:
            message = _("The workflow id '${id}' (${title}) doesn't contain the transition '${transition}'.",
                        mapping={'id': workflow.id, 'title': workflow.title, 'transition': transition_name})
            return message
        else:
            return ''
