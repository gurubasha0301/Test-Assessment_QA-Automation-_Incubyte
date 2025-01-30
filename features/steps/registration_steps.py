from behave import given, when, then
from utils.driver_factory import get_driver
from pages.registration_page import RegistrationPage
import time


@given("I am on the Magento home page")
def step_impl(context):
    context.driver = get_driver()
    context.registration_page = RegistrationPage(context.driver)
    context.registration_page.visit("https://magento.softwaretestingboard.com/")

@when('I navigate to the "Create an Account" page')
def step_impl(context):
    context.registration_page.go_to_create_account()

@when("I fill in the registration form with valid details")
def step_impl(context):
    for row in context.table:
        field, value = row["Field"], row["Value"]
        if field == "First Name":
            context.first_name = value
        elif field == "Last Name":
            context.last_name = value
        elif field == "Email":
            context.email = value
        elif field == "Password":
            context.password = value
    context.registration_page.fill_registration_form(context.first_name, context.last_name, context.email, context.password)

@when("I submit the form")
def step_impl(context):
    context.registration_page.submit_form()
    time.sleep(7)

@then("I should be redirected to the account dashboard")
def step_impl(context):
    assert "My Account" in context.driver.title
    time.sleep(7)
    context.driver.quit()
