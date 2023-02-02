import requests
from bs4 import BeautifulSoup

username = input("Enter GitHub username: ")
url = f"https://github.com/{username}"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    img = soup.find("img", class_="avatar-user")
    if img is not None:
        img_url = img['src']
        img_data = requests.get(img_url).content
        with open(f"{username}_github_profile_pic.jpg", 'wb') as f:
            f.write(img_data)
    else:
        print("Profile picture not found.")

else:
    print("Failed to scrape URL. Response code:", response.status_code)


"""
This is another way for solving the same problem
"""

"""
import requests
from bs4 import BeautifulSoup as bs

github_profile = "https://github.com/amankharwal"
req = requests.get(github_profile)
scraper = bs(req.content, "html.parser")
profile_picture = scraper.find("img", class_="avatar-user")["src"]
print(profile_picture)
"""