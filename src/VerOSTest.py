import platform
import subprocess
import json
import requests
from bs4 import BeautifulSoup

top20apps = ["Outlook", "WhatsApp", "Netflix", "Spotify", "iTunes", 
             "iCloud", "Telegram", "GamingApp", "Prime", "Firefox", 
             "AppleMusic", "Instagram", "TikTok", "317180B0BB486", ".FACEBOOK",
             "Slack", "AppleDevices", "OfficeHub", "AppleTV", "LinkedIn"]

def get_os():
    system = platform.system()
    release = platform.release()
    version = platform.version()

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
    for package in packages:
        if app_name.lower() in package['Name'].lower():
            return f"{package['Name']} - Version: {package['Version']}"
        
    return f"{app_name} is not installed."

def get_vulnSumm(url):
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
}
    response = requests.get(link, headers=headers)
    if response.status_code == 200:
        html_content = response.text

			# Parse HTML with BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')

			# Find divs labeled 'cvesummarylong py-0'
        cve_summaries = soup.find_all('div', class_='cvesummarylong py-0')

			# Print vulnerabilities
        for summary in cve_summaries:
            print(summary.get_text(strip=True))  # `strip=True` removes leading/trailing whitespaces
            print("\n")

    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
		

system, release, version = get_os()

print(f"Operating System: {system}")
print(f"Release: {release}")
print(f"Version: {version}")

ct = 1

for element in top20apps:
    app_name = element
    app_version = get_app_version(app_name)
    print(ct,")", app_version)
    ct = ct + 1

#URL = "https://www.cvedetails.com/vulnerability-list/vendor_id-26/product_id-125376/version_id-1840311/Microsoft-Windows-10-22h2-10.0.19045.5011.html"

'''headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
}'''

#r = requests.get(URL, headers=headers)

#soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib
#print(soup.prettify())

urls = ["https://www.cvedetails.com/vulnerability-list/vendor_id-26/product_id-125376/version_id-1840311/Microsoft-Windows-10-22h2-10.0.19045.5011.html",
        "https://www.cvedetails.com/vulnerability-list/vendor_id-26/product_id-113/Microsoft-Outlook.html",
        "https://www.cvedetails.com/vulnerability-list/vendor_id-19851/product_id-73154/Whatsapp-Whatsapp-Desktop.html",
        "https://www.cvedetails.com/vulnerability-list/vendor_id-16257/Netflix.html",
        ]
for link in urls:
	get_vulnSumm(link)
	print("\n" + "-"*40 + "\n")
	'''response = requests.get(link, headers=headers)
	if response.status_code == 200:
		html_content = response.text

		# Step 2: Parse the HTML content with BeautifulSoup
		soup = BeautifulSoup(html_content, 'html.parser')

		# Step 3: Find all divs with the class 'cvesummarylong py-0'
		cve_summaries = soup.find_all('div', class_='cvesummarylong py-0')

		# Step 4: Extract and print the text of each summary
		for summary in cve_summaries:
			print(summary.get_text(strip=True))  # `strip=True` removes leading/trailing whitespaces

	else:
		print(f"Failed to retrieve the page. Status code: {response.status_code}")'''