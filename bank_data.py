#! /usr/bin/python3.8.7
import json
from typing import Dict

import pandas as pd


class BankConfig(dict):
    def __init__(self):
        with open('bank_config.json') as json_file:
            self.__dict__ = json.load(json_file)
            super().__init__(self.__dict__)

    def in_pretty(self):
        return json.dumps(self.__dict__, indent=4)


def extract_bank_data_from_csv(csv_file, bank: str = "Norisbank", sort_by_date: bool = True):
    CONFIG = BankConfig()
    print(CONFIG.in_pretty())

    if bank not in CONFIG:
        raise AttributeError(f"Until now there is no config for Bank: {bank}")

    options = CONFIG[bank]["options"]

    bank_df = pd.read_csv(csv_file, **options).iloc[::-1]

    if sort_by_date:
        bank_df = bank_df.reset_index(drop=True)

    bank_df = clean_up_bank_data(bank_df.copy(), bank)

    return bank_df


def load_bank_config(bank: str) -> Dict[int, int]:
    if bank == "Norisbank":
        return 4, 151


def clean_up_bank_data(bank_df: pd.DataFrame, bank: str) -> pd.DataFrame:
    if bank == "Norisbank":
        return clean_up_norisbank_data(bank_df)


def clean_up_norisbank_data(bank_df: pd.DataFrame) -> pd.DataFrame:
    # rename columns to lower case
    bank_df.columns = bank_df.columns.str.lower()

    # calculates value of column "soll" and "haben"
    bank_df["soll"] = bank_df["soll"].str.replace(",", ".").astype(float)
    bank_df["haben"] = bank_df["haben"].str.replace(",", ".").astype(float)
    bank_df["soll"] = bank_df["soll"].fillna(0)
    bank_df["haben"] = bank_df["haben"].fillna(0)
    bank_df["betrag"] = bank_df["soll"] + bank_df["haben"]

    # deletes unused columns
    columns_to_delete = ["wert",
                         "fremde gebühren",
                         "abweichender empfänger",
                         "anzahl der aufträge",
                         "anzahl der schecks",
                         "kundenreferenz",
                         "mandatsreferenz ",
                         "gläubiger id",
                         "iban",
                         "bic",
                         "soll",
                         "haben"]

    bank_df.drop(columns_to_delete, axis=1, inplace=True)

    # renames columns
    bank_df = bank_df.rename({"begünstigter / auftraggeber": "person"}, axis=1)

    # changes entries of column "umsatzart" to specific names
    types = ["Kartenzahlung",
             "SEPA-Lastschrift",
             "SEPA-Gutschrift",
             "SEPA-Überweisung",
             "SEPA-Dauerauftrag"]

    result = [next(type for type in types if type in data) if any(
        type in data for type in types) else data for data in bank_df["umsatzart"]]
    bank_df["umsatzart"] = result

    return bank_df
