import logging

from behave import step
logging.getLogger().setLevel(logging.INFO)

@step('get start')
def step_impl(context):
    logging.info('get start')
    print('test print')

@step('do something <{name}>')
def step_impl(context, name):
    # log = logging.getLogger()
    # handler = logging.StreamHandler()
    # log.addHandler(handler)
    # log.setLevel(logging.INFO)
    # log.info('do something '+ str(name))
    print('hrer2222')
    logging.error('do something '+ str(name))

@step('always true')
def step_impl(context):
    logging.warning('always true')
    assert 1 == 1


