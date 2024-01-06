class InvalidPhoneNumber(Exception):
    def __init__(self, message):
        super().__init__(message)


class InvalidPhoneService(Exception):
    def __init__(self, message):
        super().__init__(message)


class PhoneTextFileNotFound(Exception):
    def __init__(self, message):
        super().__init__(message)
