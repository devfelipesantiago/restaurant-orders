from collections import Counter


class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append({"name": costumer, "food": order, "day": day})

    def get_most_ordered_dish_per_costumer(self, costumer):
        how_many_times = list()
        for line in self.orders:
            if line.get("name") == costumer:
                how_many_times.append(line.get("food"))
        for item in Counter(how_many_times).most_common(1):
            most_requested = item
        return most_requested[0]

    def get_never_ordered_per_costumer(self, costumer):
        all_foods = set()
        foods = set()
        for line in self.orders:
            all_foods.add(line.get("food"))
            if line.get("name") == costumer:
                foods.add(line.get("food"))
        return all_foods - foods

    def get_days_never_visited_per_costumer(self, costumer):
        all_days = set()
        days = set()
        for line in self.orders:
            all_days.add(line.get("day"))
            if line.get("name") == costumer:
                days.add(line.get("day"))
        return all_days - days

    def get_busiest_day(self):
        all_days = []
        for line in self.orders:
            all_days.append(line.get("day"))
        return Counter(all_days).most_common()[0][0]

    def get_least_busy_day(self):
        all_days = []
        for line in self.orders:
            all_days.append(line.get("day"))
        return Counter(all_days).most_common()[-1][0]
