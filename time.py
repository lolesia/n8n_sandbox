import datetime
import pytz
import os


TIMEZONES = {
    "Kyiv, Ukraine": "Europe/Kyiv",
    "New York, USA": "America/New_York",
    "London, UK": "Europe/London",
    "Tokyo, Japan": "Asia/Tokyo",
    "Sydney, Australia": "Australia/Sydney"
}


def display_current_time(city_timezones):
    """
    Получает текущее время для каждого города и выводит его.
    """
    

    max_city_len = max(len(city) for city in city_timezones.keys())
    

    time_format = "%H:%M:%S"
    
    print("-" * (max_city_len + 30))
    print("🌍 Current Time in Key Cities 🕒")
    print("-" * (max_city_len + 30))
    

    utc_now = datetime.datetime.now(pytz.utc)
    
    for city, tz_name in city_timezones.items():
        try:

            tz = pytz.timezone(tz_name)
            

            city_time = utc_now.astimezone(tz)
            

            print(
                f"| {city.ljust(max_city_len)} | "
                f"{city_time.strftime('%A, %B %d').ljust(18)} | "
                f"**{city_time.strftime(time_format)}** |"
            )

        except pytz.exceptions.UnknownTimeZoneError:
            print(f"Error: Unknown timezone name for {city}: {tz_name}")
            
    print("-" * (max_city_len + 30))



if __name__ == "__main__":
    display_current_time(TIMEZONES)