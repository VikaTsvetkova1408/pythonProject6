import json
import requests
from config import exchanges


class APIException(Exception):
    pass


class Convertor:
    @staticnetnod
    def get_price(base, sym, amout):
        try:
            base_key = exchanges[base.lower()]
        except KeyError:
            raise APIException(f"Валюта {base} не найдена!")

        try:
            sym_key = exchanges[sym.lower()]
        except KeyError:
            raise APIException(f"Валюта {sym} не найдена!")

        if base_key == sym_key:
            raise APIException(f"невозможно перевести одинаковые валюты {base} !")

        try:
            amout = float(amout)
        except ValueError:
            raise APIException(f"Не удалось обработать колличество {amout} !")

        r = requests.get(f"https://api.exchangerate.host/convert?from={base_key}&to={sym_key}&amount={amount}")
        resp = json.loads(r.content)
        new_price = resp['result']
        new_price = round(new_price, 3)
        message = f"Цена {amount} {base} в {sym} : {new_price}"
        return message
    