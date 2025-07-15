from datetime import datetime, timedelta


def get_date_of_yesterday():
    # Get yesterday's date
    yesterday = datetime.now() - timedelta(days=1)
    yesterday_formatted = yesterday.strftime("%d/%m/%Y")

    return yesterday_formatted
