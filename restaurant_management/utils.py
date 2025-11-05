import datetime
from .models import DailyHours
def get_today_hours(restaurant):
    today = datetime.datetime.today().strtime('%A')
    try:
        hours = DailyHours.objects.get(restaurant=restaurant, day_of_week=today)

        return{
            "day":today,
            "open_time":hours.open_time,
            "close_time":hours.close_time
        }
        expect DailyHours.DoesNotExist:
        return None