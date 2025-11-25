from datetime import datetime


class TimeUtils:
    @staticmethod
    def current_date_str() -> str:
        return datetime.now().strftime("%Y%m%d")
