import csv
from collections import Counter


def reader_file(file):
    if not file.endswith(".csv"):
        raise FileNotFoundError(f"No such file or directory: '{file}'")
    rows = []
    try:
        with open(file, "r") as file_ref:
            fieldnames = ["name", "food", "day"]
            table = csv.DictReader(file_ref, fieldnames, delimiter=",")

            for recipt in table:
                rows.append(recipt)
            return rows
    except FileNotFoundError:
        raise FileNotFoundError(f"No such file or directory: '{file}'")


def how_many_times(path_to_file, costumer):
    data = reader_file(path_to_file)
    orders = list()

    for line in data:
        if line.get("name") == costumer:
            orders.append(line.get("food"))
    return orders


def data_by_client(path_to_file):
    data = reader_file(path_to_file)
    all_foods = set()
    all_days = set()
    joao_foods = set()
    joao_days = set()

    for line in data:
        all_foods.add(line.get("food"))
        all_days.add(line.get("day"))

        if line.get("name") == "joao":
            joao_foods.add(line.get("food"))
            joao_days.add(line.get("day"))

    for item in Counter(how_many_times(path_to_file, "maria")).most_common(1):
        most_requested = item

    what_dishes_did_joao_never_order = all_foods - joao_foods
    what_days_did_joao_never_go_to_the_cafeteria = all_days - joao_days

    result = {
        "maria": most_requested[0],
        "arnaldo": how_many_times(path_to_file, "arnaldo").count("hamburguer"),
        "joao_foods": what_dishes_did_joao_never_order,
        "joao_days": what_days_did_joao_never_go_to_the_cafeteria,
    }
    return result


def analyze_log(path_to_file):
    data = data_by_client(path_to_file)

    maria_eats = data.get("maria")
    arnaldo_ask_hamburguer = data.get("arnaldo")
    joao_never_ask = data.get("joao_foods")
    joao_never_went = data.get("joao_days")
    with open("data/mkt_campaign.txt", "w") as file:
        file.writelines(
            maria_eats
            + "\n"
            + str(arnaldo_ask_hamburguer)
            + "\n"
            + str(joao_never_ask)
            + "\n"
            + str(joao_never_went)
        )
