from behave import *

from features.locators import dict_locators
from user_flow.user import User

use_step_matcher("re")


@given("the user is on the SauceDemo login page")
def do_nothing(context):
    """Do nothing in this step
    :param context: behave context.
    :type context: behave.runner.Context
    """
    pass


@when("the user enters valid login credentials")
def user_enter_valid_credentials(context):
    """User enters valid login credentials

    :param context: behave context.
    :type context: behave.runner.Context
    """
    context.user = User(context.page, context, "standard_user", "secret_sauce")
    context.user.enter_text(dict_locators["username_text_box"], "standard_user")
    context.user.enter_text(dict_locators["password_text_box"], "secret_sauce")


@step("clicks the login button")
def user_click_login_button(context):
    """User click login button

    :param context: behave context.
    :type context: behave.runner.Context
    """
    context.user.click_btn(dict_locators["login_button"])


@then("the Products page is displayed")
def verify_display_of_product_page(context):
    """Verify product page is displayed

    :param context: behave context.
    :type context: behave.runner.Context
    """
    try:
        assert context.page.locator("//*[@class='title']").text_content() == "Products"
    except Exception as e:
        raise AssertionError("The product page is not displayed") from e
