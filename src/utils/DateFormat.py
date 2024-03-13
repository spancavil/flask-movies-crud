import datetime


class DateFormat():

    # For use it without instance the class
    @classmethod
    def convert_date(self, date):
        return datetime.datetime.strftime(date, '%d/%m/%Y')
