from behave import then


@then('Verify Sign In page is opened')
def verify_signin_page_opened(context):
    context.app.cart_page.verify_login_page()


@then('Verify Sign In form is opened')
def verify_signin_form_opened(context):
    context.app.login_page.verify_signin_form_opened()


@then('Input email and password on SignIn page')
def input_email_password(context):
    context.app.login_page.input_email_password()


@then('Click Sign In')
def click_sign_in(context):
    context.app.login_page.click_sign_in()


@then('Verify user is logged in (sign in form should disappear)')
def verify_signin_success(context):
    context.app.login_page.verify_signin_success()
