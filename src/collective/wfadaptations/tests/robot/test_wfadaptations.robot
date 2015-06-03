# ============================================================================
# ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s collective.wfadaptations -t test_wfadaptations.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src collective.wfadaptations.testing.COLLECTIVE_WFADAPTATIONS_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot src/collective/wfadaptations/tests/robot/test_wfadaptations.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a manager I want to be able to associate a workflow adaptation
  Given a logged in manager
   When I associate a workflow adaptation
   Then I see parameters form

Scenario: Valid workflow adaptation parameters lead to success message
  Given a logged in manager
   When I associate a workflow adaptation
   And I enter valid parameters
   Then I see success message

Scenario: Invalid workflow adaptation parameters lead to failure message
  Given a logged in manager
   When I associate a workflow adaptation
   And I enter invalid parameters
   Then I see failure message


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a manager
  Log in as site owner


# --- WHEN / AND --------------------------------------------------------------

I associate a workflow adaptation
  Go to  ${PLONE_URL}/@@associate_workflow_adaptation
  Select from list  form.widgets.workflow:list  intranet_workflow
  Click Button  Next

I enter valid parameters
  Input text  form.widgets.state_name  internal
  Input text  form.widgets.new_state_title  New title
  Click Button  Save

I enter invalid parameters
  Input text  form.widgets.state_name  foobar
  Input text  form.widgets.new_state_title  Internal draft
  Click Button  Save


# --- THEN -------------------------------------------------------------------

I see parameters form
  Wait until page contains  Site Map
  Page should contain  Choose parameters for your workflow adaptation
  Page should contain element  form.widgets.state_name
  Page should contain element  form.widgets.new_state_title

I see success message
  Wait until page contains  Site Map
  Page should contain  The workflow adaptation has been successfully applied.

I see failure message
  Wait until page contains  Site Map
  Page should contain  The workflow adaptation has not been successfully applied.