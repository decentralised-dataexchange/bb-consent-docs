from behave import *
import requests


@given("an organization admin for Data4Diabetes organization")
def step_impl(context):
    pass


@when("the admin logs into the Admin dashboard")
def step_impl(context):
    data = {
        "username": "admin@retail.com",
        "password": "qwerty123",
    }
    url = "https://staging-consent-bb-api.igrant.io/v2" + "/onboard/admin/login"
    response = requests.post(url, json=data)
    context.response = response


@then("the admin should be able to access pages in the admin dashboard")
def step_impl(context):
    assert context.response.status_code == 200
