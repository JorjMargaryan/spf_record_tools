SUCCESS = 0
GENERAL_ERROR = 1
ELEMENT_NOT_FOUND = 2
TIMEOUT_ERROR = 3
ELEMENT_CLICK_INTERCEPTED = 4
UNEXPECTED_BEHAVIOR = 5
FILE_NOT_FOUND = 6
LOGGING_ERROR = 7
FILE_NAME_GENERATION_ERROR = 8
REPORT_CREATION_ERROR = 9
INVALID_VALUE_ERROR = 10
ASSERTION_ERROR = 11
URL_INTERACTION_ERROR = 12
JSON_DECODE_ERROR = 13
ATTRIBUTE_ERROR = 14
NO_SUCH_FRAME_ERROR = 15
ELEMENT_NOT_INTERACTABLE_ERROR = 16

MessageCodes = {
    0: "The automation tests ran successfully without any errors.",
    1: "General error occurred during test execution. This code is used for unspecified errors.",
    2: "Element not found error. This code is used when an expected element on the web page is not found.",
    3: "Timeout error while waiting for an element. This code is used when an expected element does not appear within the specified time limit.",
    4: "Element click intercepted exception. This code is used when an element is not clickable due to interception.",
    5: "Unexpected application behavior error. This code is used when the application behaves unexpectedly, indicating a potential bug.",
    6: "File not found error. This code is used when a required file is not found.",
    7: "Logging error. This code is used when An error occurred while logging (creating a log file).",
    8: "File Name generation error. This code is used when an error occurred while generating the html or xml report file name.",
    9: "Report creation error. This code is used when an error occurred while creating html or xml report file.",
    10: "Invalid or Unexpected Value Error. This code is used when there is an issue with data conversion, such as invalid or unexpected values, during the application's execution.",
    11: "Assertion error. This code is used when an assertion fails during the process.",
    12: "URL interaction error. This code is used when something went wrong with the interaction with the URL",
    13: "JSON Decode Error. This code is used when something went wrong with interaction with the JSON files.",
    14: "Attribute Error. This code is used when trying to get a non-existent or invalid attribute.",
    15: "No Such Frame Error. This code is used when trying to switch to a non-existent frame.",
    16: "Element Not Interactable Error. This code is used when an element is found but is not interactable (e.g., it's hidden or disabled)",
}
