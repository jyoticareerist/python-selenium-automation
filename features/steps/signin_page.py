from behave import when, then


@when('Store original windows')
def store_windows(context):
    context.windows = context.app.page.get_all_windows()
    context.original_window = context.app.page.get_current_window()


@when('Click on Target terms and conditions link')
def click_terms_and_conditions(context):
    context.app.login_page.click_terms_and_conditions()


@when('Switch to the newly opened window')
def switch_window(context):
    context.app.page.switch_to_new_window()


@when('Enters incorrect email and password combination')
def input_incorrect_email_password(context):
    email = 'jyoti12@gmail.com'
    password = 'something12'
    context.app.login_page.input_email_password(email, password)


@when('Clicks login button')
def click_sign_in(context):
    context.app.login_page.click_sign_in()


@then('Verify Terms and Conditions page is opened')
def verify_terms_and_conditions_page_opened(context):
    context.app.terms_and_conditions_page.verify_terms_and_conditions_page_opened()


@then('User can close new window and switch back to original')
def close_and_switch_to_original(context):
    context.app.page.close_page()
    context.app.page.switch_to_window(context.original_window)


@then('Verify Sign In page is opened')
def verify_signin_page_opened(context):
    context.app.cart_page.verify_login_page()


@then('Verify Sign In form is opened')
def verify_signin_form_opened(context):
    context.app.login_page.verify_signin_form_opened()


@then('Input email and password on SignIn page')
def input_email_password(context):
    email = '****@****.***'
    password = '********'
    context.app.login_page.input_email_password(email, password)


@then('Click Sign In')
def click_sign_in(context):
    context.app.login_page.click_sign_in()


@then('Verify user is logged in (sign in form should disappear)')
def verify_signin_success(context):
    context.app.login_page.verify_signin_success()


@then("Verified that We can't find your account. message is shown")
def verify_invalid_login(context):
    context.app.login_page.verify_invalid_login()
