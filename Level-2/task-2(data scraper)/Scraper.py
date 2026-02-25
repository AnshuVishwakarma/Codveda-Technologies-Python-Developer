import requests
from bs4 import BeautifulSoup
import csv

URL = "http://quotes.toscrape.com/"

try:
    # Step 1: Get webpage content
    response = requests.get(URL)
    response.raise_for_status()  # Raise error if request fails

    # Step 2: Parse HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # Step 3: Extract specific data (quotes + authors)
    quotes = soup.find_all("span", class_="text")
    authors = soup.find_all("small", class_="author")

    # Step 4: Save data to CSV
    with open("scraped_data.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Quote", "Author"])  # Header

        for quote, author in zip(quotes, authors):
            writer.writerow([quote.text, author.text])

    print("✅ Data scraped and saved to scraped_data.csv successfully!")

except requests.exceptions.RequestException as e:
    print("❌ Error fetching the webpage:", e)

except Exception as e:
    print("❌ An unexpected error occurred:", e)