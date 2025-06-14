from behave import *

use_step_matcher("re")


@given("the user is on the SauceDemo login page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Given the user is on the SauceDemo login page')