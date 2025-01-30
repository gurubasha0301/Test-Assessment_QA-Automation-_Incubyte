def before_all(context):
    pass  

def after_all(context):
    if context.driver:
        context.driver.quit()
