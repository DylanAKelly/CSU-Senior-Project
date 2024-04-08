

# Senior Project Requirements Document



## Project Purpose

The purpose of this project is to create a free Windows vulnerability scanner that is capable of detecting when Windows OS is out-of-date and informing the user via email of what vulnerabilities are present in the current version of the software. Additionally, the vulnerability scanner will be capable of determining if any of the top 20 most popular applications installed on the computer are out-of-date and will notify the user of the security risks via email. 



## Stakeholders

The project stakeholders are the users who will be relying on the program to notify them when their computer's OS or installed applications are out of date and pose a security risk.

## Project Constraints

The program must accurately and routinely check for security risks in the current Windows OS version & the top 20 most popular applications. The program must also notify the user via email when a vulnerability or update is found.

## Naming Conventions and Terminology

- OS - Operating System

- Security risk - anything that could result in the damage, theft, or unauthorized access of data on a computer.

- Vulnerability - a flaw or weakness in a program or application.

## Relevant Facts and Assumptions

###### There is one relevant fact relating to the goals of this program:

If an OS or application is not kept up-to-date, the computer and the data stored on it are much more vulnerable to various threats and vulnerabilities that have been patched out in the latest version[^1].

###### There are two relevant assumptions relating to the goals of this program:

1. People in positions of control (i.e., parents, IT staff, etc.) over multiple computers will not always know when a specific computer's OS or installed applications are out-of-date and pose a security risk.

2. Providing the ability to be notified of such security risks via email is a beneficial service to those individuals. 

## Project Scope

Currently, some individuals with control over and responsibility for multiple computers may not always have access to every computer they are responsible for. This could result in a security risk due to a vulnerability in an outdated OS or application version. Providing those in charge with a way to be notified of any potential security risks would have a positive effect on their overall digital security.

## Functional Requirements

###### **Example Requirement ID: VS-REQ-AB**

| Example ID Segment | Meaning/Classification                                                                                                                                                                          |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| VS                 | Vulnerability Scanner                                                                                                                                                                           |
| REQ                | Requirement                                                                                                                                                                                     |
| A                  | Requirement Type (#, 1 - Functional, 2 - Look and Feel, 3 - Usability, 4 - Performance, 5 - Maintainability/Support, 6 - Security, 7 - Cultural, 8 - Operational/Environmental, 9 - Compliance) |
| B                  | Requirement Priority/Importance (Numeric, lower number has a higher priority, i.e 1 > 2 > 3, etc.)                                                                                              |



##### Requirement 1: Program checks for known vulnerabilities in the current Windows OS version

* ID Number - VS-REQ-11

* Type - Functional

* Description - When the user runs the program, the program will determine what version of the Windows OS is installed and if there are any known vulnerabilities for that version.

* Rationale - Detecting vulnerabilities in the Windows OS increases security and is a core function of the program.

* Fit Criterion - The program will retrieve information on the current Windows OS version, listing any and all security vulnerabilities present in that version. 

* Priority - High Priority

* Dependencies - No dependencies

##### Requirement 2: Program checks if a new version of the Windows OS is available

* ID Number - VS-REQ-12

* Type - Functional

* Description - When the user runs the program, the program will check if a new version of the Windows OS is available.

* Rationale - Checking if a new OS version is available increases security and is a core function of the program.

* Fit Criterion - The program will check if there is an update for the OS and will notify the user if there is.

* Priority - High Priority

* Dependencies - No dependencies

##### Requirement 3: Program checks for known vulnerabilities in current versions of the top 20 most popular apps installed

* ID Number - VS-REQ-13

* Type - Functional

* Description - When the user runs the program, the program will determine what version, if any, of the top 20 most popular applications is installed. The program will then check if there are any known vulnerabilities for the installed version(s).

* Rationale - Detecting vulnerabilities in any of the top 20 popular applications installed on the computer increases security and is a core function of the program.

* Fit Criterion - The program will retrieve information on the current versions of the top 20 popular applications, and if any are installed, the program will list any and all security vulnerabilities present in the installed applications.

* Priority - High Priority

* Dependencies - No dependencies

##### Requirement 4: Program checks if any of the top 20 most popular apps have a new version available

* ID Number - VS-REQ-14

* Type - Functional

* Description - When the user runs the program, it will check if there is a new version for any of the top 20 applications currently installed on the computer.

* Rationale - Checking if a new version of any of the top 20 popular applications is available increases security and is a core function of the program.

* Fit Criterion - The program will check if there is an update for each of the top 20 popular programs *if* it is already installed on the computer. If an update is found, the program will notify the user. 

* Priority - High Priority

* Dependencies - No dependencies

##### Requirement 5: Program is able to accept, store, and remember the user's email, and their email can be updated

* ID Number - VS-REQ-15

* Type - Functional

* Description - The program will provide the user with the ability to enter and store an email address. The email address will be used to notify the user when any vulnerabilities in the OS/installed application are found or when a new version of the OS/installed application is available. The program will also allow the user to change the email address.

* Rationale - The program must be able to accept, store, and remember the email address provided by the user in order to email them when vulnerabilities are found in the OS/installed apps or a new version of the OS/installed app is available. The program must allow the user to update the email that alerts will be sent to in case a mistake was made during the input process or the email the user wants to use for alerts has changed. 

* Fit Criterion - The program will prompt the user for an email address that it can store. The user will be able to verify that the stored email address is correct by having the program output the address. 

* Priority - High Priority

* Dependencies - No dependencies

##### Requirement 6: Program emails the stored email if any vulnerabilities are found or if any updates are available

* ID Number - VS-REQ-16

* Type - Functional

* Description - The program will send an email to the user using the stored email address. The email will inform the user of the vulnerabilities found in the current OS/installed application version and/or if a new version of the OS/installed application is available.

* Rationale - The program must be able to alert the user that vulnerabilities have been found or that an update is available, even if the user does not currently have physical access to the computer. This is a core function of the program. 

* Fit Criterion - When a vulnerability or update is found, the program will send an email to the stored email address to notify the user that an update or vulnerability was found.

* Priority - High Priority

* Dependencies - VS-REQ-15

##### Requirement 7: Program automatically runs on computer startup

* ID Number - VS-REQ-17

* Type - Functional

* Description - The program will automatically run when the user turns their computer on. 

* Rationale - The program should run when the computer starts up so that the scanner checks for vulnerabilities and updates as frequently as the computer is used. This ensures that the computer is kept up-to-date.

* Fit Criterion - The program will open when the user starts their computer, showing the user if any updates or vulnerabilities are found. 

* Priority - Medium Priority

* Dependencies - No dependencies

## Look and Feel Requirements

##### Requirement 8: Program is visually appealing and easy to look at

* ID Number - VS-REQ-23

* Type - Look and Feel (i.)

* Description - The program will look clean and professional, which will make it easier for the user to effectively use the program.

* Rationale - If the program looks nice, it will reduce user stress and make the user's experience more enjoyable. 

* Fit Criterion - The program will maintain a consistent layout and style.

* Priority - Medium Priority

* Dependencies - VS-REQ-11 through VS-REQ-16

##### Requirement 9: Program is responsive to user commands

* ID Number - VS-REQ-21

* Type - Look and Feel (i.)

* Description - The program will provide clear indication to the user that they attempted to perform an action, both visually and through text. 

* Rationale - Proper feedback is essential for users to understand how a program functions. It will also allow the user to become more adept at using the program in a shorter amount of time.

* Fit Criterion - The program will provide users with visual cues that indicate when an action has occurred successfully. 

* Priority - Medium Priority

* Dependencies - VS-REQ-11 through VS-REQ-16

##### Requirement 10: Program has clear, specific, and helpful error messages

* ID Number - VS-REQ-22

* Type - Look and Feel (ii.)

* Description - In the event a user's command does not work, the program will inform the user that the command failed. The program will also inform the user as to why the command failed and provide possible solutions. 

* Rationale - Clear, specific, and helpful error messages will help the user get back on track when something goes wrong. 

* Fit Criterion - Error messages will specify what the user was trying to do, why it did not work, and what can be done to avoid the error going forward. 

* Priority - Medium Priority

* Dependencies - VS-REQ-11 through VS-REQ-16

## Usability Requirements

##### Requirement 11: Program is easy to set up

* ID Number - VS-REQ-32

* Type - Usability (i.)

* Description - The program will be easy for the user to set up. 

* Rationale - If the program is easy to set up, it will reduce user stress and make the user's experience more enjoyable.

* Fit Criterion - The program's initial set-up time will be under five minutes and will require minimal user input.

* Priority - Medium Priority

* Dependencies - VS-REQ-11 through VS-REQ-16

##### Requirement 12: Program is easy to navigate and use

* ID Number - VS-REQ-31

* Type - Usability (i.)

* Description - The program will be easy to use, understand, and navigate, even for a first-time user.

* Rationale - If the program is easy to navigate and use, it will allow the user to become more adept at using the program in a shorter amount of time.

* Fit Criterion - Possible input and navigation will be visually distinct from the other parts of the program. 

* Priority - Medium Priority

* Dependencies - VS-REQ-11 through VS-REQ-16

##### Requirement 13: Program provides clear and concise feedback for user actions

* ID Number - VS-REQ-33

* Type - Usability (iii.)

* Description - When the user performs an action, the program will provide the user with clear and concise feedback that the action occurred.

* Rationale - Clear and concise feedback for user input will help the user get used to using the program. The increased sense of familiarity will allow the user to become proficient with the program much faster than they otherwise would. 

* Fit Criterion - Feedback for successful actions will be visually discernible from the rest of the program. 

* Priority - Medium Priority

* Dependencies - VS-REQ-11 through VS-REQ-16

## Performance Requirements

##### Requirement 14: Program quickly starts when the user's computer is started or when the program is launched

* ID Number - VS-REQ-42

* Type - Performance (i.)

* Description - The program will start quickly when the computer is turned on or the program is launched.

* Rationale - Having the program quickly start when the computer is turned on or the program is launched  will reduce the amount of time the program is running, which will reduce the amount of resources that the program uses.

* Fit Criterion - Once the user's computer has started and reached the home screen, *or* the program has been launched, it will take no longer than one minute for the program to allow for user input.

* Priority - Low Priority

* Dependencies - VS-REQ-11 through VS-REQ-17, 

##### Requirement 15: Program completes core functions accurately and in a timely manner

* ID Number - VS-REQ-41

* Type - Performance (i., iv.)

* Description - The program will complete its primary functions (scanning for vulnerabilities, emailing the user when vulnerabilities are found, etc.) quickly and efficiently. 

* Rationale - Quickly completing its core functions will reduce the amount of time that the program needs to run, meaning it will consume fewer resources. 

* Fit Criterion - The program will complete vulnerability scans in less than three minutes, update scans in less than one minute, and send emails in less than one minute. 

* Priority - High Priority

* Dependencies - VS-REQ-11 through VS-REQ-16

## Operational and Environmental Requirements

##### Requirement 16: Program functions with modern Windows OSs (Windows 10 & 11)

* ID Number - VS-REQ-81

* Type - Operational and Environmental 

* Description - The program will be compatible with Windows 10 and Windows 11 systems. 

* Rationale - The program must function with modern Windows OSs, since scanning for vulnerabilities and checking for updates in Windows OSs is one of the program's core functions. 

* Fit Criterion - The program will list vulnerabilities in Windows 10 and 11, and will check for updates to Windows 10 and 11. 

* Priority - High Priority

* Dependencies - VS-REQ-11 through VS-REQ-17

## Maintainability and Support Requirements

##### Requirement 17: The program has a consistent structure that is conducive to future maintenance and support

* ID Number - VS-REQ-51

* Type - Maintainability and Support

* Description - The program will be designed in a way that allows for easy modification, adaptation, or maintenance. 

* Rationale - A consistent structure will allow for changes and additions to be made easily. Furthermore, a consistent structure will make maintenance or outside adaptation much simpler. 

* Fit Criterion - The program will maintain a consistent format, text structure, and layout. 

* Priority - Medium Priority

* Dependencies - No dependencies

## Security Requirements

##### Requirement 18: Program does not request and cannot access sensitive information not required for core functions

* ID Number - VS-REQ-61

* Type - Security (i.)

* Description - The program will only prompt the user for sensitive information that is vital to the program's ability to complete its core functions (i.e., the email address the user would like alerts sent to).

* Rationale - There is no reason for the program to request or store sensitive information that is not required for the program to complete its core functions. Storing any sensitive information that is not required would be a security risk. 

* Fit Criterion - The program will only prompt the user for an email address.

* Priority - High Priority

* Dependencies - No dependencies

##### Requirement 19: Program properly handles and stores any sensitive information required for core functions

* ID Number - VS-REQ-62

* Type - Security (iii.)

* Description - The program will store any required sensitive data (i.e., the email address) in a secure manner.

* Rationale - Improper storage or handling of sensitive information is a security risk. 

* Fit Criterion - The program will only store the user's email address.

* Priority - High Priority

* Dependencies - No dependencies

## Compliance Requirements

##### Requirement 20: Program complies with modern computer science ethical standards

* ID Number - VS-REQ-91

* Type - Compliance

* Description - The program will be created with modern ethical standards in mind. Specifically, the ACM and IEEE Codes of Ethics will be used as ethical guidelines for the construction, implementation, and maintenance of the program.

* Rationale - It is a great idea to practice and implement proper ethical standards in one's work. 

* Fit Criterion - The program will not violate any ACM or IEEE Code of Ethics standards. 

* Priority - High Priority

* Dependencies - No dependencies
  
  

## User Documentation and Training

All documentation necessary for users will be located in the program itself and will be accessible with a command. There are no training requirements for users, but a baseline familiarity with computers will be beneficial. 

[^1]: Radu, Constantinescu & Zota, Razvan Daniel. (2007). Issues of OperatingSystems Security.


