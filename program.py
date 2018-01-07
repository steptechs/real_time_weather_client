import requests
import bs4


def main():
    print_the_header()

    code = input("What zipcode do you want the weather for (e.g. 90210)? ")

    html = get_html_from_web(code)


    get_weather_from_html(html)
    # parse the html
    # display the forecast


def print_the_header():
    print("-----------------------------")
    print("         WEATHER APP")
    print("-----------------------------")
    print()


def get_html_from_web(zipcode):
    url = "http://www.wunderground.com/weather-forecast/{}".format(zipcode)
    response = requests.get(url)
    return response.text


def get_weather_from_html(html):
    # cityCss = '.region-content-header h1'
    # weatherScaleCss = '.wu-unit-temperature .wu-label'
    # weatherTempCss = '.wu-unit-temperature .wu-value'
    # weatherConditionCss = '.condition-icon'

    soup = bs4.BeautifulSoup(html, 'html.parser')
    loc = soup.find(class_='region-content-header').find('h1').get_text()
    condition = soup.find(class_='condition-icon').get_text()
    temp = soup.find(class_='wu-unit-temperature').find(class_='wu-value').get_text()
    scale = soup.find(class_='wu-unit-temperature').find(class_='wu-label').get_text()

    loc = cleanup_text(loc)
    condition = cleanup_text(condition)
    temp = cleanup_text(temp)
    scale = cleanup_text(scale)

    print(condition, temp, scale, loc)


def cleanup_text(text: str):
    if not text:
        return text

    text = text.strip()
    return text


if __name__ == "__main__":
    main()


