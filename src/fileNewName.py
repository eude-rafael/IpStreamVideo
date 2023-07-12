import datetime

class FileNewName:
    @staticmethod
    def create_name():
        now = datetime.datetime.now()
        year = str(now.year)
        month = str(now.month).zfill(2)
        day = str(now.day).zfill(2)
        hour = str(now.hour).zfill(2)
        minute = str(now.minute).zfill(2)
        second = str(now.second).zfill(2)
        return f"{year}{month}{day}_{hour}{minute}{second}_vid.mp4"
