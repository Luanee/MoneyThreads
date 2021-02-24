#! /usr/bin/python3.8.7
import numpy as np
import pandas as pd
from bank_data import extract_bank_data_from_csv


def day(day):
    return pd.to_datetime(day, dayfirst=True)


def days(start, end):
    start = day(start)
    end = day(end)

    return int((end - start) / np.timedelta64(1, "D"))


def weeks(start, end):
    start = day(start)
    end = day(end)

    return int((end - start) / np.timedelta64(1, "W"))


def months(start, end):
    start = day(start)
    end = day(end)

    return int((end - start) / np.timedelta64(1, "M"))


class BankStatementAnalyzer(object):
    def __init__(self, filename: str, skiprows: int = None, nrows: int = None, sort_by_date: bool = True):
        self._filename = filename
        self._skiprows = skiprows
        self._nrows = nrows
        self._account = None
        self._title = None
        self._bank_df = None
        self._start_date = None
        self._end_date = None
        self._period = None
        self._currency = None
        self._start_balance = 0
        self._end_balance = 0

        self._set_general_information()
        self._bank_df = extract_bank_data_from_csv(self._filename, "Norisbank", True)

    def _set_general_information(self):
        with open(self._filename, "r", encoding="ISO-8859-1", errors="ignore") as csvfile:
            lines = csvfile.readlines()
            _title, _account = lines[0].split(";;;")

            self._title = " ".join([word.capitalize() for word in _title[8:-4].split()])
            self._account = int(''.join(filter(str.isdigit, _account)))

            self._start_date, self._end_date = lines[1].split(" - ")
            self._period = {"days": days(self._start_date, self._end_date),
                            "weeks": weeks(self._start_date, self._end_date),
                            "months": months(self._start_date, self._end_date)}

            self._end_balance = float(lines[2].split(";")[4].replace(",", "."))
            self._start_balance = float(lines[-1].split(";")[4].replace(",", "."))
            self._currency = {"code": "EUR", "symbol": "€"}

    @property
    def data(self):
        return self._bank_df

    def getTimePeriod(self):
        return "from: {}, to: {}, {}".format(self._start_date, self._end_date, self._period)

    def getColumns(self):
        return list(self.data.columns)

    def statistics(self):
        print(f'{("#" * 45)}\n'
              f'Bank account statistics\n\n'
              f'Bank Institute:  {self._title}\n'
              f'nAccount number: {self._account}\n'
              )

        # print(overview[overview["Auftraggeber"] == "Pit Nahrstedt"])
        # clients = overview["Auftraggeber"].dropna().unique().tolist()
        # print()
        # for client in clients:
        #     print(client)
        #     shop = overview[overview["Auftraggeber"] == client]
        #     print("\tTime period: {:10}-{:10}".format(shop["Buchungstag"].iloc[0], shop["Buchungstag"].iloc[-1]))
        #     print("\tCount of payments:{:6d}".format(len(shop.index)))
        #     print("\tSum of payments:{: 11.2f}".format(shop["Betrag"].sum()))
        #
        #     weeks_diff = weeks(shop["Buchungstag"].iloc[0], shop["Buchungstag"].iloc[-1])
        #     # weeks_diff = weeks(period["start"], period["end"])
        #     months_diff = months(shop["Buchungstag"].iloc[0], shop["Buchungstag"].iloc[-1])
        #     # months_diff = months(period["start"], period["end"])
        #
        #     if weeks_diff:
        #         print("\tTotal peer week:{: 11.2f}".format(shop["Betrag"].sum() / weeks_diff))
        #     else:
        #         print("\tTotal peer week:{: 11.2f}".format(shop["Betrag"].sum()))
        #
        #     if months_diff:
        #         print("\tTotal peer month:{: 10.2f}".format(shop["Betrag"].sum() / months_diff))
        #     else:
        #         print("\tTotal peer month:{: 10.2f}".format(shop["Betrag"].sum()))


if __name__ == '__main__':
    BS = BankStatementAnalyzer("Kontoumsaetze_431632008900_Norisbank.csv", 4)
    print(BS.data)
    # print(BS.getTimePeriod())
    BS.statistics()
