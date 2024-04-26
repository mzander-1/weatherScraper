import requests, time
from bs4 import BeautifulSoup


def weather_scraper():
    url = "https://forecast.weather.gov/MapClick.php?lat=40.7146&lon=-74.0071"

    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        fahrenheit = soup.find(class_="myforecast-current-lrg").get_text()
        celsius = soup.find(class_="myforecast-current-sm").get_text()
        print(f"The current temperature in New York City is {fahrenheit} or {celsius}.")

    else:
        print("Error: Could not retrieve data.")
        print(f"Status code: {response.status_code}")

while True:
    weather_scraper()
    print("Sleeping...")
    time.sleep(60)  # Run every 60 seconds