# Windows Operating System Vulnerability Scanner

My project is a vulnerability scanner for modern Windows operating systems (Windows 10 & 11). The scanner will inform the user if there are any known vulnerabilities in the installed OS. The scanner will also check for vulnerabilities in the top 20 most popular applications if the user has them installed. If any vulnerabilities are found, the scanner will notify the user via email. 

## Compile/Deploy

In order to compile and deploy this program, you will need to download Python 3.13 [here](https://www.python.org/downloads/) and download an Integrated Developing Environment (IDE) of your choosing. If you are unfamiliar with IDEs, I personally use [Visual Studio Code](https://code.visualstudio.com/) and would recommend it. You will also need to download the files in this repository. Once you have installed Python, your IDE of choice, and the files in the repository, navigate to the "src" folder using the command line. Once there, type "pip install requests" and let the module install. Then type "pip install beautifulsoup4" and let the module install. Open the src folder in the IDE, click on "VulnScanner.py" and run the program. 

## Usage and Options

In order to use the program, enter your email into the text box labeled "New Email" once you have started the program. Then, press the "Change Email" button. Finally, begin the scan by pressing the "Begin Scan" button.

## Testing

Testing for my program was done manually. More detailed test cases and results can be found in the "tests" folder in this repository.
