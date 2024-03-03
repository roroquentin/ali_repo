import requests
from bs4 import BeautifulSoup
from database import create_database, insert_car

def scrape_arabam():
    url = "https://www.arabam.com/ikinci-el/otomobil"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    car_list = []

    for car in soup.find_all("div", class_="list-item"):
        title = car.find("h3").text.strip()
        price = car.find("span", class_="color-red4 font-semibold").text.strip()
        year = car.find("p", class_="crop-middle mb-4").text.strip()
        car_list.append((title, price, year))

    return car_list

def main():
    create_database()
    cars = scrape_arabam()
    for car in cars:
        insert_car(*car)
    print("Car information has been scraped and stored in the database.")

if __name__ == "__main__":
    main()
