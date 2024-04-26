import requests, time
from bs4 import BeautifulSoup


def weather_scraper():
    url = "https://forecast.weather.gov/MapClick.php?lat=40.7146&lon=-74.0071"

    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        fahrenheit = soup.find(class_="myforecast-current-lrg").get_text()
        fahrenheit_only_numbers = fahrenheit[:-2]
        celsius = (int(fahrenheit_only_numbers) - 32) * 5/9
        print(f"The current temperature in New York City is {fahrenheit} or {round(celsius)}°C.")

    else:
        print("Error: Could not retrieve data.")
        print(f"Status code: {response.status_code}")

while True:
    weather_scraper()
    print("Sleeping...")
    time.sleep(60)  # Run every 60 seconds