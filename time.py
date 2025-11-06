import datetime
import pytz
import os

# ----------------------------------------------------
# 1. Список городов и их часовых поясов
# ----------------------------------------------------
# Используется формат 'Континент/Город' (стандарт IANA Time Zone Database)
TIMEZONES = {
    "Kyiv, Ukraine": "Europe/Kyiv",
    "New York, USA": "America/New_York",
    "London, UK": "Europe/London",
    "Tokyo, Japan": "Asia/Tokyo",
    "Sydney, Australia": "Australia/Sydney"
}

# ----------------------------------------------------
# 2. Функция для получения и вывода времени
# ----------------------------------------------------
def display_current_time(city_timezones):
    """
    Получает текущее время для каждого города и выводит его.
    """
    
    # Определяем ширину для красивого форматирования
    max_city_len = max(len(city) for city in city_timezones.keys())
    
    # Формат времени: Час:Минута:Секунда (например, 14:30:59)
    time_format = "%H:%M:%S"
    
    print("-" * (max_city_len + 30))
    print("🌍 Current Time in Key Cities 🕒")
    print("-" * (max_city_len + 30))
    
    # Текущее время в формате UTC (универсальный стандарт)
    utc_now = datetime.datetime.now(pytz.utc)
    
    for city, tz_name in city_timezones.items():
        try:
            # 1. Получаем объект часового пояса
            tz = pytz.timezone(tz_name)
            
            # 2. Конвертируем UTC время в местное время города
            city_time = utc_now.astimezone(tz)
            
            # 3. Форматируем вывод
            # .ljust() используется для выравнивания по левому краю
            print(
                f"| {city.ljust(max_city_len)} | "
                f"{city_time.strftime('%A, %B %d').ljust(18)} | "
                f"**{city_time.strftime(time_format)}** |"
            )

        except pytz.exceptions.UnknownTimeZoneError:
            print(f"Error: Unknown timezone name for {city}: {tz_name}")
            
    print("-" * (max_city_len + 30))


# ----------------------------------------------------
# 3. Запуск программы
# ----------------------------------------------------
if __name__ == "__main__":
    display_current_time(TIMEZONES)