import platform
import subprocess
import json
import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import tkinter as tk
from tkinter import ttk
import sys
import threading

root = tk.Tk()
root.title("Top 20 Applications and OS Vulnerability Scanner")
root.geometry('800x450+0+0')


top20apps = ["Outlook", "WhatsApp", "Netflix", "Spotify", "iTunes", 
             "iCloud", "Telegram", "GamingApp", "Prime", "Firefox", 
             "AppleMusic", "Instagram", "TikTok", "317180B0BB486", ".FACEBOOK",
             "Slack", "AppleDevices", "OfficeHub", "AppleTV", "LinkedIn"]


###IMPORTANT INFORMATION FOR APP VULNERABILITY LINKS###

	#Amazon Prime link is for Cloudfront, which Prime video uses. 
	#This is because there is no CVE Details page for Prime Video.

	#Apple Music link is the same link as iTunes.
	#This is because the Apple Music Desktop App uses iTunes.

	#Instagram link provides security vulnerabilities for the Android and iOS versions.
	#This is because there is no distinct desktop version for Instagram on CVE Details.
	#Instagram also uses the same tools and frameworks as Facebook.
	#See Facebook's vulnerabilities for other potential vulnerabilities.

	#TikTok link provides security vulnerabilities for the Android and iOS versions.
	#This is because there is no distinct desktop version for TikTok on CVE Details.

	#The Apple Devices link is the same link as iTunes.
	#This is because the Apple Devices application uses iTunes to syn information.

	#The OfficeHub link is a link for Microsoft 365 Apps because it no longer exists.
	#All of OfficeHub's functionality has now been take over by 365.

	#The AppleTV link is a link for Tvos, as AppleTV was deprecated.
	#Tvos is the current effective product.


urls = ["https://www.cvedetails.com/vulnerability-list/vendor_id-26/product_id-125376/version_id-1840311/Microsoft-Windows-10-22h2-10.0.19045.5011.html",
        "https://www.cvedetails.com/vulnerability-list/vendor_id-26/product_id-113/Microsoft-Outlook.html",
        "https://www.cvedetails.com/vulnerability-list/vendor_id-19851/product_id-73154/Whatsapp-Whatsapp-Desktop.html",
        "https://www.cvedetails.com/vulnerability-list/vendor_id-16257/Netflix.html",
        "https://www.cvedetails.com/vulnerability-list/vendor_id-17900/product_id-45593/version_id-591758/Spotify-Spotify-1.0.69.336.html",
        "https://www.cvedetails.com/vulnerability-list/vendor_id-49/product_id-4956/version_id-1635201/Apple-Itunes-12.12.9.html",
        "https://www.cvedetails.com/vulnerability-list/vendor_id-49/product_id-34308/version_id-702660/Apple-Icloud-13.0.html",
        "https://www.cvedetails.com/vulnerability-list/vendor_id-16210/product_id-51060/version_id-1496043/Telegram-Telegram-Desktop-2.8.8.html",
        "https://www.cvedetails.com/vulnerability-list/vendor_id-26/product_id-169218/Microsoft-Xbox-Gaming-Services.html",
        "https://www.cvedetails.com/vulnerability-list/vendor_id-12126/product_id-99467/Amazon-Amazon-Cloudfront.html",
        "https://www.cvedetails.com/vulnerability-list/vendor_id-452/product_id-3264/version_id-380425/Mozilla-Firefox-preview-release.html",
        "https://www.cvedetails.com/vulnerability-list/vendor_id-49/product_id-4956/version_id-1635201/Apple-Itunes-12.12.9.html",
        "https://www.cvedetails.com/vulnerability-list/vendor_id-7758/product_id-87909/version_id-975872/Facebook-Instagram-128.0.0.26.128.html",
        "https://www.cvedetails.com/vulnerability-list/vendor_id-19245/product_id-59124/version_id-614787/Tiktok-Tiktok-12.8.0.html",
        "https://www.cvedetails.com/vulnerability-list/vendor_id-7758/product_id-111854/Facebook-Messenger.html",
        "https://www.cvedetails.com/vulnerability-list/vendor_id-7758/product_id-13216/version_id-974773/Facebook-Facebook-3.0.4.html",
        "https://www.cvedetails.com/vulnerability-list/vendor_id-22135/product_id-73569/version_id-1450682/Slack-Wp-Slacksync-1.8.5.html",
        "https://www.cvedetails.com/vulnerability-list/vendor_id-49/product_id-4956/version_id-1635201/Apple-Itunes-12.12.9.html",
        "https://www.cvedetails.com/vulnerability-list/vendor_id-26/product_id-80308/version_id-1782441/Microsoft-365-Apps-2401.17231.20236.html",
        "https://www.cvedetails.com/vulnerability-list/vendor_id-49/product_id-34427/version_id-1874293/Apple-Tvos-18.2.html",
        "https://www.cvedetails.com/vulnerability-list/vendor_id-6955/product_id-11702/version_id-411390/Linkedin-Toolbar-3.0.2.1098.html"
        ]


def get_os():
    system = platform.system()
    release = platform.release()
    version = platform.version()

    f = open("testoutput.txt", "w")
    f.write("System: " + system + '\n')
    f.write("Release: " + release + '\n')
    f.write("Version: " + version + '\n')
    f.close()
    return system, release, version


def get_app_version(app_name):
    # PowerShell command execution
    result = subprocess.run(
        ['powershell', '-Command', 'Get-AppxPackage | ConvertTo-Json'],
        capture_output=True,
        text=True,
        check=True
    )
    
    packages = json.loads(result.stdout)
    # Determines if application is installed (and version if installed)
    f = open("appversions.txt", "a")
    
    for package in packages:
        if app_name.lower() in package['Name'].lower():
            f.write(app_name + f" - Version: {package['Version']}" + '\n')
            return f"{package['Name']} - Version: {package['Version']}"
    f.close()
    return f"{app_name} is not installed."


def get_vulnSumm(url):
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
}
    response = requests.get(url, headers=headers) #url was link
    f = open("vulnerabilities.txt", "a")
    f.write("-"*40+ '\n')
    if response.status_code == 200:
        html_content = response.text

			# Parse HTML with BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')

			# Find divs labeled 'cvesummarylong py-0'
        cve_summaries = soup.find_all('div', class_='cvesummarylong py-0')

			# Print vulnerabilities
        for summary in cve_summaries:
            #print(summary.get_text(strip=True))  # `strip=True` removes leading/trailing whitespaces
            f.write(summary.get_text(strip=True) + '\n')
            #print("\n")
        #f.close()

    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")


def email_login(filepath):
    with open(filepath, 'r') as f:
        lines = f.read().splitlines()
    return lines[0], lines[1] #Top20VulnSum email and password


def send_email(subject, body, recipient, files, login):
    email, password = email_login(login)

    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_username = email
    smtp_password = password

    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = recipient
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    for file_path in files:
        try:
            with open(file_path, 'rb') as f:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(f.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', f'attachment; filename={file_path}')
                msg.attach(part)
        except Exception as e:
            print(f"Error attaching file {file_path}: {e}")

    try:
        # Connect to the server and send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Secure the connection
            server.login(smtp_username, smtp_password)
            server.sendmail(email, recipient, msg.as_string())
            #print("Email sent successfully")
    except Exception as e:
        print(f"Error sending email: {e}")


def end_scan():
    sys.exit(0)


def run_scan():
	
	f = open("appversions.txt", "w")
	f.close()

	f = open("vulnerabilities.txt", "w")
	f.close()

	#system, release, version = 
	get_os()

	#print(f"Operating System: {system}")
	#print(f"Release: {release}")
	#print(f"Version: {version}")

	ct = 1

	for element in top20apps:
		app_name = element
		#app_version = 
		get_app_version(app_name)
		#print(ct,")", app_version)
		ct = ct + 1

	for link in urls:
		get_vulnSumm(link)
		#print("\n" + "-"*40 + "\n") 

	subject = "Top 20 Apps Vulnerability Summary"
	body = "The attached files provide information on your vulnerability summary."
	#recipient = "VulSumUserEmail.txt"
	files = ["testoutput.txt", "appversions.txt", "vulnerabilities.txt"] # List of all relevant text files
	login = "appdata.txt"
	f = open("VulSumUserEmail.txt", 'r')
	recipient = f.read()
	f.close()

	if len(recipient) == 0:
		print("Please press the 'View or Change Email' button to add your email.")

	send_email(subject, body, recipient, files, login)
	progressbar.stop()


def user_email():

    userEmail = str(newEmail.get())
    if len(userEmail) == 0:
        return

    f = open("VulSumUserEmail.txt", "w")
    f.write(userEmail)
    f.close()
    print("Changed User Email")


def run_scanner():
    start_loading()
    run_scan()


def start_loading():
    progressbar.start()


emailLabel = tk.Label(root, text="New Email: ", font=("arial", 10, "bold"), fg="black").place(x=50, y=350)
#emailLabel.pack()

newEmail = tk.StringVar()
entry_box = tk.Entry(root, textvariable=newEmail, width=50, bg="gray70").place(x=250, y=350)

progressLabel = tk.Label(root, text="Scan Progress", font=("arial", 10, "bold"), fg="black").place(x=350, y=200)

progressbar = ttk.Progressbar(root, orient="horizontal", length=250, mode="indeterminate")
progressbar.place(x=275, y=220)

email = tk.Button(root, text="Change Email", bg="lightblue", command=user_email)
email.place(x=650, y=345)
#email.pack(pady=10)

scan = tk.Button(root, text="Begin Scan", bg="lightgreen", command=threading.Thread(target=run_scanner).start)
scan.place(x=200, y=80)
#scan.pack(pady=10)

stop = tk.Button(root, text="Stop Program", bg="firebrick2", command=end_scan)
stop.place(x=500, y=80)
#stop.pack(pady=10)

root.mainloop()