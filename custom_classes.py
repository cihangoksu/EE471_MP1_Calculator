class Calculator:
    def __init__(self):
        # The single underscore is a convention for internal/private attributes
        self._current_val = 0
    def subtract(self, x, y):
            """Adds two numbers and updates the internal value."""
            self._current_val = x - y
            return self._current_val