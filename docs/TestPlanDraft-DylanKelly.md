# Test Plan Document <!-- omit in toc -->

- [IDENTIFICATION INFORMATION SECTION](#identification-information-section)
  - [PRODUCT](#product)
  - [PROJECT DESCRIPTION](#project-description)
  - [TEST PERSONNEL](#test-personnel)
  - [PROGRAMMERS](#programmers)
- [MANUAL TESTING SECTION](#manual-testing-section)
  - [MANUAL TESTING STRATEGY / EXTENT OF MANUAL TESTING:](#manual-testing-strategy--extent-of-manual-testing)
  - [MANUAL TESTING](#manual-testing)
- [REGRESSION TEST SECTION](#regression-test-section)
  - [REGRESSION TEST STRATEGY](#regression-test-strategy)
  - [REGRESSION TEST CASES](#regression-test-cases)
- [INTEGRATION TEST SECTION](#integration-test-section)
  - [INTEGRATION TEST STRATEGY AND EXTENT OF INTEGRATION TESTING](#integration-test-strategy-and-extent-of-integration-testing)
  - [INTEGRATION TEST CASES](#integration-test-cases)
- [USER ACCEPTANCE TEST SECTION)](#user-acceptance-test-section)
  - [USER ACCEPTANCE TEST STRATEGY](#user-acceptance-test-strategy)
  - [USER ACCEPTANCE TEST CASES](#user-acceptance-test-cases)
- [Appendix](#appendix)

## IDENTIFICATION INFORMATION SECTION

### PRODUCT

- **Product Name:** Windows OS and Application Vulnerability Scanner
- **Product Line Portfolio:** Cybersecurity

### PROJECT DESCRIPTION

The purpose of this project is to create a free Windows vulnerability scanner that is capable of detecting when Windows OS or any of the top 20 most popular web apps are out-of-date. If the OS or any of the applications are found to be out-of-date, the program will notify the user of the security risks via email.

### TEST PERSONNEL

- Dylan A. Kelly

### PROGRAMMERS

- Dylan A. Kelly

## MANUAL TESTING SECTION

Verify that the core functions of the program work correctly by testing specific actions and their outcomes.

### MANUAL TESTING STRATEGY / EXTENT OF MANUAL TESTING:

Test each program requirement by evaluating program performance and output for specific tasks.

### MANUAL TESTING

| \#  | OBJECTIVE                                                                                                          | PRECONDITION                                                                                                                      | INPUT                                                               | EXPECTED RESULTS                                                                                                                                                                                         | TEST DELIVERABLES                                                                                                                                                                                             | Observed |
| --- | ------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| 1   | Display the installed OS version.                                                                                  | The user's computer has a Windows OS installed that is Windows 10 or 11.                                                          | Run Program                                                         | Operating System: \<OS Type><br/> Release: \<Release Number><br/> Version: \<Version Number>                                                                                                             | Program displays the correct version of the installed OS.                                                                                                                                                     |          |
| 2   | Display the installed application version.                                                                         | The user's computer has one of the top 20 most popular applications for windows devices installed.                                | Run Program                                                         | If application is installed:<br/>\<application version><br/> Otherwise:<br/> \<Application name> is not installed.                                                                                       | Program displays the correct version of the application if it is installed. Otherwise, it tells the user that the application is not installed.                                                               |          |
| 3   | Check if the OS is the most current version.                                                                       | The user's computer has a Windows OS installed that is Windows 10 or 11.                                                          | Run Program                                                         | If the OS is up to date: <br/>Your OS is up to date.<br/>Otherwise:<br/>Your OS is not up to date. The current version is \<version number>.                                                             | Program displays the message that the OS is up to date if it is up to date, and displays the message that the OS is out of date and what the new version number is if it is not up to date.                   |          |
| 4   | Check if the version of application is the most current version.                                                   | The user's computer has one or more of the top 20 most popular applications for windows devices installed.                        | Run Program                                                         | If the application is up to date: <br/> \<Application name> is up to date.<br/>Otherwise:<br/>\<Application name> is not up to date. The current version is \<version number>.                           | Program displays the message that the application is up to date if it is up to date, and displays the message that the application is out of date and what the new version number is if it is not up to date. |          |
| 5   | Check if the current version of the OS has any known vulnerabilities.                                              | The user's computer has a Windows OS installed that is Windows 10 or 11.                                                          | Run Program                                                         | If there are vulnerabilities:<br/>The known vulnerabilities for this OS version are \<list of vulnerabilities>.<br/>Otherwise: There are no known vulnerabilities for this OS version.                   | Program displays all of the known vulnerabilities for the current OS version.                                                                                                                                 |          |
| 6   | Check if the current version of an application has any known vulnerabilities.                                      | The user's computer has one or more of the top 20 most popular applications for windows devices installed.                        | Run Program                                                         | If there are vulnerabilities:<br/>The known vulnerabilities for this application version are \<list of vulnerabilities>.<br/>Otherwise: There are no known vulnerabilities for this application version. | Program displays all of the known vulnerabilities for the current application version.                                                                                                                        |          |
| 7   | Successfully accept, store, and update the user's email address.                                                   | Program is minimally viable.                                                                                                      | My personal email address.                                          | Program stores the user's email address and can be retrieve or edited.                                                                                                                                   | Program is able to accept input for the user's email address and is capable of retrieveing or updating the email.                                                                                             |          |
| 8   | Successfully send an email to the user containing a lost of the known vulnerabilities for the OS and applications. | Program is able to receive and store the user's email address and retrieve vulnerability information from the cvedetails website. | Run Program                                                         | The user recieves an email from the program containing relevant vulnerability information.                                                                                                               | Program is able to send an email to the user's email address containing a list of the known vulnerabilities for the current OS and application versions.                                                      |          |
| 9   | Program accurately retrieves information for current Windows OSs (Windows 10 and 11).                              | Program runs and is able to determine what OS and version is on a given computer.                                                 | Run Program                                                         | The program displays the OS information to the user when the program is run on a computer with Windows 10 or 11.                                                                                         | Program displays the correct version of the installed OS.                                                                                                                                                     |          |
| 10  | Program begins running when the user's computer starts up.                                                         | Program is installed on computer and computer is powered on.                                                                      | User powers on and signs into their computer.                       | The program runs automatically every time the user's computer is turned on.                                                                                                                              | Program automatically runs and sends the user a report when they turn on their computer.                                                                                                                      |          |
| 11  | Program has a consistent code structure and digital layout that is conducive to future maintenence and support.    | Program is minimally viable.                                                                                                      | Request feedback from individuals with experience coding in Python. | Someone with more experience in Python programming informs me that my program is written in a manner that is conducive to future maintenece and support.                                                 | Written confirmation from the individuals contacted that the program is designed in a way that is conducive to future maintenence and support.                                                                |          |
| 12  | Program does not request or access sensitive user information stored on the user's computer.                       | Program is minimally viable.                                                                                                      | Run Program                                                         | The program does not ask for sensitive user information, nor does the program attempt to store any sensitive user information it may come across.                                                        | Program outputs the last value of all variables to ensure that no sensitive information was mistakenly recorded.                                                                                              |          |
| 13  | Program properly handles and stores any sensitive information required in order to complete its core functions.    | Program is minimally viable.                                                                                                      | Run Program                                                         | The program stores the user's email and only the user's email in a secure manner.                                                                                                                        | Program encrypts the user's email so it cannot be easily identified.                                                                                                                                          |          |
| 14  | Program complies with industry ethical standards.                                                                  | N/A                                                                                                                               | N/A                                                                 | The program is designed in such a way that it does not violate any ethical standards for computing professionals.                                                                                        | The influence of computing professional ethics standards will be apparent in all facet's of the program's design, creation, implementation, and testing.                                                      |          |

## REGRESSION TEST SECTION

Ensure that previously developed and tested software still performs after change.

### REGRESSION TEST STRATEGY

No regression testing will be performed.<!--- Evaluate all reports introduced in previous releases--->

### REGRESSION TEST CASES

| #   | OBJECTIVE | INPUT | EXPECTED RESULTS | OBSERVED |
| --- | --------- | ----- | ---------------- | -------- |
| 1   |           |       |                  |          |
| 2   |           |       |                  |          |
| 3   |           |       |                  |          |

## INTEGRATION TEST SECTION

Combine individual software modules and test as a group.

### INTEGRATION TEST STRATEGY AND EXTENT OF INTEGRATION TESTING

No integration testing will be performed.. <!---Evaluate all integrations with locally developed shared libraries, with consumed services, and other touch points. --->

### INTEGRATION TEST CASES

| #   | OBJECTIVE | INPUT | EXPECTED RESULTS | TEST DELIVERABLES |
| --- | --------- | ----- | ---------------- | ----------------- |
| 1   |           |       |                  |                   |
| 2   |           |       |                  |                   |
| 3   |           |       |                  |                   |

## USER ACCEPTANCE TEST SECTION

Verify that the structure and "feel" of the program works for the user.

### USER ACCEPTANCE TEST STRATEGY

Due to the fact that the user acceptance tests will primarily test subjective criteria, an objective system must be made in order to accurately determine if the program passes the user acceptance tests. To this end, user satsifaction with dufferent factes of the program will be recorded using a survey. The user will fill ut this survey, rating each aspect of the program on a scale of one to five stars. In order to pass the tests, the average score for each section must be *at least* four stars.

### USER ACCEPTANCE TEST CASES

| #                             | TEST ITEM                                                                                                             | EXPECTED RESULTS                                                                                                                                                                                 | ACTUAL RESULTS | DATE |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------- | ---- |
| 1                             | Program is visually appealing.                                                                                        | Survey score of 4 stars.                                                                                                                                                                         |                |      |
| 2                             | Program is responsive to user commands and input.                                                                     | Survey score of 4 stars.                                                                                                                                                                         |                |      |
| 3                             | Program displays clear, specific, and helpful error messages.                                                         | Survey score of 4 stars.                                                                                                                                                                         |                |      |
| 4                             | Program is easy to set up and run.                                                                                    | Survey score of 4 stars. The program takes no longer than five minutes to perform the initial set-up and requires no more than one button press and one instance of user text input.             |                |      |
| 5                             | Program is easy to navigate and use.                                                                                  | Survey score of 4 stars.                                                                                                                                                                         |                |      |
| 6                             | Program provides the user with clear and consise feedback on their actions and the information that is given to them. | Survey score of 4 stars.                                                                                                                                                                         |                |      |
| 7                             | Program will start in a timely manner once the user's computer is turned on or when the program itself is run.        | Survey score of 4 stars. The program takes no longer than one minute to begin performing its core functions on subsequent uses after it has been set up for the first time.                      |                |      |
| 8 | Program completes its core functions accurately and in a timely manner.                                               | Survey score of 4 stars. The program completes the vulnerability scans in three minutes or less, scans for updates in one minute or less, and emails the user its finding in one minute or less. |                |      |

## Appendix
