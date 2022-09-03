import requests
import xml.dom.minidom


def city_user():
    city_name = input("Podaj nazwe miasta: ")
    return city_name


def json_weather(city_name):
    api_key = "cbd4dde0b7..."


    current_endpoint = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    current_response = requests.get(current_endpoint).json()
    weather = current_response["weather"][0]["main"]
    temperature = current_response["main"]["temp"]

    print(weather)
    print(temperature)


def xml_weahter(city_name):
    api_key = "cbd4dde0b7..."


    source = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&mode=xml&units=metric"
    xml_response = requests.request("GET", source).text
    xmlparse = xml.dom.minidom.parseString(xml_response)
    # xml_pogoda = xmlparse.toprettyxml()

    weather = xmlparse.getElementsByTagName("weather")
    for element in weather:
        print(element.getAttribute("value"))
    temperature = xmlparse.getElementsByTagName("temperature")
    for element in temperature:
        print(element.getAttribute("value"))


def main():

    city_name = city_user()

    json_xml = input("Podaj, ktory format chcesz uzyskac json czy xml? ")
    if json_xml == "json":
        json_weather(city_name)
    elif json_xml == "xml":
        xml_weahter(city_name)
    else:
        print("Niepoprawny wybor sprobuj jeszcze raz! ")


if __name__ == "__main__":
    main()