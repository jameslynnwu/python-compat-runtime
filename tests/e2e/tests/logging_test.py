from google.appengine.api.logservice import logservice
import json
import logging
import os
import pytest



@pytest.fixture
def request_id():
  return os.environ.get('REQUEST_LOG_ID')

@pytest.mark.xfail
def do_not_run_test_logservice_fetch(request_id):
  """This test fails at logservice.fetch"""
  logging.info('TESTING')
  found_log = False
  for req_log in logservice.fetch(
      request_ids=[request_id],
      include_app_logs=True):
    for app_log in req_log.app_logs:
      if app_log.message == 'TESTING':
        found_log = True

  assert found_log
