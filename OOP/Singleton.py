# singleton pattern

class ApplicationState:
    instance = None

    def __init__(self):
        self.is_logged_in = False

    @staticmethod
    def get_application_state():
        if not ApplicationState.instance:
            ApplicationState.instance = ApplicationState()
        return ApplicationState.instance


app_state = ApplicationState.get_application_state()
print(app_state.is_logged_in)  # False

app_state.is_logged_in = True
print(app_state.is_logged_in)  # True

app_state2 = ApplicationState.get_application_state()
print(app_state.is_logged_in)  # True
print(app_state2.is_logged_in)  # True

# in this example, we have a class that has a single instance
# and we can access it from anywhere in the Application
# this is a very useful pattern when you want to have a single
# instance of a class that is shared across the ApplicationState
# for example, you can use it to store the state of the Application
# and you can access it from anywhere in the ApplicationState
# without having to pass it as a parameter to every function
# that needs it (which is a very common pattern in Python)
