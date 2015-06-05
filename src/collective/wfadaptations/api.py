# -*- coding: utf-8 -*-
"""API for workflow adaptations."""
import json

from plone import api


RECORD_NAME = 'collective.wfadaptations.applied_adaptations'


class AdaptationAlreadyAppliedException(Exception):
    pass


def get_applied_adaptations():
    """Get applied adaptations for all workflows.

    :returns: The list of applied adaptations
    :rtype: list
    """
    record = api.portal.get_registry_record(RECORD_NAME)
    if record is None:
        return []

    # deserialize parameters
    return [{'workflow': info['workflow'],
             'adaptation': info['adaptation'],
             'parameters': json.loads(info['parameters'])} for info in record]


def add_applied_adaptation(adaptation_name, workflow_name, **parameters):
    """Add an applied adaptation to registry record.

    :param adaptation_name: [required] name of the applied adaptation
    :type adaptation_name: Unicode object

    :param workflow_name: [required] name of the workflow on which the
    adaptation is applied
    :type workflow_name: Unicode object
    """
    by_workflow = get_applied_adaptations_by_workflows()
    if (workflow_name in by_workflow and
            adaptation_name in by_workflow[workflow_name]):
        raise AdaptationAlreadyAppliedException

    serialized_params = json.dumps(parameters, sort_keys=True)
    value = {
        u'workflow': unicode(workflow_name),
        u'adaptation': unicode(adaptation_name),
        u'parameters': unicode(serialized_params),
        }

    record = api.portal.get_registry_record(RECORD_NAME)
    if record is None:
        record = []

    record.append(value)
    api.portal.set_registry_record(RECORD_NAME, record)


def get_applied_adaptations_by_workflows():
    """Return a list of applied adaptations for each workflow.

    :returns: A dict which keys are workflow names and values are the list of
    applied workflow adaptations for this workflow.
    :rtype: dict
    """
    applied_adaptations = api.portal.get_registry_record(RECORD_NAME)
    if applied_adaptations is None:
        return {}

    result = {}
    for adaptation in applied_adaptations:
        workflow = adaptation['workflow']
        adaptation = adaptation['adaptation']
        if workflow not in result:
            result[workflow] = []

        result[workflow].append(adaptation)

    return result


def get_applied_adaptations_for_workflow(workflow_name):
    """Return the list of applied adaptations for workflow_name.

    :param workflow_name: [required] name of the workflow
    :type workflow_name: Unicode object

    :returns: A list of applied workflow adaptations for this workflow.
    :rtype: dict
    """
    all_applied = get_applied_adaptations_by_workflows()
    if workflow_name not in all_applied:
        return []
    else:
        return all_applied[workflow_name]
