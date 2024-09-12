# EasyDMARC SPF Tools

Automated tests for verifying the functionality of the EasyDMARC SPF Record tools. These tests are implemented using Python and Selenium WebDriver.

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Tests](#running-the-tests)

## Introduction

EasyDMARC SPF Tools include the SPF Record Generator, SPF Record Checker, and SPF Record Validator. These tools help users generate, check, and validate SPF records to ensure proper email authentication and security.

## Prerequisites

Before starting, please make sure the following requirements are met.
1. Python 3.x installed.
2. A web browser (Chrome) is available. 
3. One of the IDEs is installed (PyCharm, VisualStudioCode, etc...)
4. Internet access is available. 
5. The following Python packages are installed

    - `Selenium WebDriver`
    - `Webdriver-manager`
    - `pathlib` - library for working with file paths
    - `os` - library for interacting with the operating system
    - `logging` - library for generating log messages
    - `random` - library for random data generation
    - `Faker` - for generating fake data
    - `unittest-xml-reporting` - for generating XML report files
    - `HtmlTestReport` - for generating HTML report files
    - `dnspython` - for DNS toolkit
  
## Installation

1. Clone the repository to your local machine:

        git clone [repository_url]

2. Navigate to the project directory:
3. Install WebDriver Manager

        pip install webdriver-manager

4. Install the required Python packages:

        pip install -r requirements.txt

## Running the Tests

To run the tests, follow these steps:
1. Ensure your test environment is set up correctly.
2. Run the tests using the following commands:
   1. For generating HTML report after tests are processed run regressionRunner.py
   (file location - tests_/common_/runners_/htmlRunners_/regressionRunner.py)
   2. For generating XML report after tests are processed run regressionRunner.py
   (file location - tests_/common_/runners_/xmlRunners_/regressionRunner.py)
      
```
    python regressionRunner.py
```
Alternatively, you can run the tests directly from your IDE by executing the `regressionRunner.py` file or test files.

### Running Tests in PyCharm
- Open PyCharm and navigate to `regressionRunner.py`.
- Right-click the file and select "Run".
- Ensure that your Python interpreter is set up properly under `File > Settings > Project: spf_record_tool > Python Interpreter`.

### Running Tests in Visual Studio Code
- Open the project in Visual Studio Code.
- Install the Python and Test extensions if not already installed.
- Open `regressionRunner.py` and click "Run" in the top-right corner.
- Ensure your Python environment is correctly configured in VSCode.
