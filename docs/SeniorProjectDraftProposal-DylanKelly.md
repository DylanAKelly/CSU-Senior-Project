**Student Name:** Dylan Kelly

**Degree and Major:** Applied Computing: Cybersecurity Concentration (BA Degree)

**Project Advisor:** Dr. Sean Hayes

**Expected Graduation Date:** 2025

**Problem Statement:**

The use of out-of-date Operating Systems or applications means there is an increased risk of various vulnerabilities, and a program that allows the user to check if they are running the latest version of their OS or application would allow them to mitigate these avoidable vulnerabilities. Computer operating systems and applications should be kept up-to-date so that security risks are mitigated. For various reasons, this is often not the case. Therefore, computer operating systems are not always updated to the latest version, meaning that the OS or application is susceptible to various threats that it would not otherwise be susceptible to. In an age where nearly everything can be done or stored online, any lapse in security could have disastrous consequences. If an OS or application is not kept up-to-date, the computer and the data stored on it are much more vulnerable to various threats and vulnerabilities that have been patched out in the latest version[^1]. A simple program that can detect if an OS or installed application is updated to the current version would provide users with a simple and efficient way to check if their computer is secure. Having the program would give users the ability to check if their OS or installed application is up-to-date at any time with a few simple steps. Preventing users from running an out-of-date OS or application is critical to increasing personal cybersecurity. In this proposal, a program that can detect and inform the user of an out-of-date OS or installed application is suggested as a mitigation.

**Project Description:**

The proposed project is a vulnerability scanner that compares the current Operating System/application version number (or patch status) against the most-recent version listed online. The program will show the user the amount of time that the update has been available, the known vulnerabilities of the current version or patch, and the risks posed based on the pillars of the CIA Triad (Confidentiality, Integrity, and Availability). My project will reference a web application vulnerability scanner called Grabber so that I can form ideas of how to construct my program. My project will also reference the website [CVE Details](https://www.cvedetails.com/) to determine the current version number or patch status for an OS or application. The program will work for the Windows Operating System, as it is the most-used OS for computers, and will scan for vulnerabilities in the twenty most commonly installed applications. Additionally, when the OS or an application is found to be out-of-date, an email will be sent to the user, notifying them of what is out-of-date and the vulnerabilities.

**Proposed Implementation Languages:**

The project will be done in either Python or C++. I am most familiar with C++, but I have coded some in Python, and the language is fairly easy to use and understand. The Grabber vulnerability scanner is also in Python, so if I decide to try and implement general concepts from Grabber, using Python to code my program might be beneficial. 

**Libraries, Packages, Development Kits, etc. to be Used:**

The standard libraries and packages for Python or C++ will be used to complete the project. I will evaluate the need for developer kits on a case-by-case basis.

**Additional Software/Equipment Needed:**

In addition to the aforementioned libraries, packages, and developer kits, I will need access to my computer's Operating System and installed applications. Additionally, I will reference the website "Grabber", which can be found by going to the link:

- [rgaucher.info/beta/grabber](https://www.rgaucher.info/beta/grabber/)

Grabber is a program that scans web applications for vulnerabilities. I will reference the source code and general process that Grabber uses to scan web applications for vulnerabilities and use it as a reference for my own project. Despite Grabber being used for web applications, the structure of the program could be a beneficial reference for me. 

**Personal Motivation:**

My major is the *B.A. in Applied Computing: Cybersecurity Concentration*, and this project is a perfect match for that major. When I graduate, I want to become a Cybersecurity Consultant or Analyst, and I believe that completing this project will help me realize that goal. There are many projects that would help me become a CS Consultant or Analyst, but I chose this project specifically due to how it is applicable to a large number of people. The feature that would notify the user when their OS or an application is out-of-date would be useful for families and companies. This is because the parents or IT departments would be able to recieve an email stating what is out of date, even if they do not have regular access to the computer. Additionally, this sort of automation would be helpful to a CS Consultant or Analyst, as it would save time when checking a client's system and applications. Furthermore, I believe completing this project will prove beneficial to the general public since it will be available for them to use. If just one person were to use my program to increase the security of their computer and/or installed applications, then I would have made a positive difference in terms of overall cybersecurity.

**Outline of Future Research Efforts:**

I will complete my project by making a program in Python or C++ that can determine the OS/application version or patch number and compare that to the current version or patch number found online. To do so, I will reference open-source vulnerability scanners (like Grabber and others) and adapt any applicable elements to my project. Although it will not be a one-to-one translation, I will use the open-source vulnerability scanners as a general roadmap and loose guide for my own project. I will also use CVE Details to determine the vulnerabilities of an OS or application version. Deliverables for this project will be in the form of code segments that complete a specific function, with a video showing that they work properly.

**Schedule:**

My schedule for the project will include regular updates (every 1-2 weeks) on project progress. The proposed schedule is as follows:

- **Weeks 1-2 (08/26 to 09/08/2024)** - Partial completion of program core functions for OS (finding vulnerabilities and updates)

- **Weeks 3-4 (09/09 to 09/22/2024)** - Completion of program core functions for OS

- **Weeks 5-6 (09/23 to 10/06/2024)** - Partial completion of program core functions for top 20 most popular applications

- **Weeks 7-8 (10/07 to 10/20/2024)** - Completion of program core functions for top 20 most popular applications

- **Weeks 9-10 (10/21 to 11/03/2024)** - Partial completion of email alert system

- **Weeks 11-12 (11/04 to 11/17/2024)** - Completion of email alert system

- **Weeks 13-14 (11/18 to 12/01/2024)** - Program refinement + implementation of extra functionality

- **Weeks 15-16 (12/02 to 12/15/2024)** - Program refinement + implementation of extra functionality 

[^1]: Radu, Constantinescu & Zota, Razvan Daniel. (2007). Issues of Operating
Systems Security.


