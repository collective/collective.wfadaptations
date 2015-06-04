# -*- coding: utf-8 -*-
"""API for workflow adaptations."""
from plone import api


RECORD_NAME = 'collective.wfadaptations.applied_adaptations'


class AdaptationAlreadyAppliedException(Exception):
    pass


def get_applied_adaptations():
    """Get applied adaptations for all workflows.

    :returns: The list of applied adaptations
    :rtype: list
    """
    return api.portal.get_registry_record(RECORD_NAME)


def add_applied_adaptation(adaptation_name, workflow_name):
    """Add an applied adaptation to registry record.

    :param adaptation_name: [required] name of the applied adaptation
    :type adaptation_name: Unicode object

    :param workflow_name: [required] name of the workflow on which the
    adaptation is applied
    :type workflow_name: Unicode object
    """
    applied_adaptations = api.portal.get_registry_record(RECORD_NAME)
    value = {
        u'workflow': unicode(workflow_name),
        u'adaptation': unicode(adaptation_name),
        }
    if value in applied_adaptations:
        raise AdaptationAlreadyAppliedException

    applied_adaptations.append(value)
    api.portal.set_registry_record(RECORD_NAME, applied_adaptations)
