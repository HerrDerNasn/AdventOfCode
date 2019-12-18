import math


def parse_chemical(value):
    key, quantity = value.split(" ")[1], value.split(" ")[0]
    return {"quantity": int(quantity), "key": key}


def parse_input(lines):
    parsed_reactions = {}
    for line in lines:
        split = line.rstrip().split(" => ")
        incoming = split[0].split(", ")
        incoming = list(map(parse_chemical, incoming))
        key, quantity = split[1].split(" ")[1], split[1].split(" ")[0]
        parsed_reactions[key] = {"quantity": int(quantity), "incoming": incoming}
    parsed_reactions["ORE"] = {"quantity": 1, "incoming": []}
    return parsed_reactions


def calc_stocks_for_fuel_target(reaction_dict, target_stocks):
    ingredient = next((target_stocks[i] for i in target_stocks.keys() if i != "ORE" and target_stocks[i]["target"] < 0), "null")
    while ingredient != "null":
        production_cycles = math.ceil(abs(ingredient["target"]) / reaction_dict[ingredient["key"]]["quantity"])
        target_stocks[ingredient["key"]]["target"] += reaction_dict[ingredient["key"]]["quantity"] * production_cycles
        for further_ingredient in reaction_dict[ingredient["key"]]["incoming"]:
            target_stocks[further_ingredient["key"]]["target"] -= further_ingredient["quantity"] * production_cycles
        ingredient = next((target_stocks[i] for i in target_stocks.keys() if i != "ORE" and target_stocks[i]["target"] < 0), "null")
    return target_stocks


with open('input.txt', 'r') as file:
    reactions = parse_input(file.readlines())
    target = 0
    next_step = 10000
    last_ore_consumption = 0
    while True:
        stocks = {}
        for key in reactions.keys():
            stocks[key] = {"key": key, "target": 0}
        stocks["ORE"] = {"key": "ORE", "target": 0}
        stocks["FUEL"]["target"] = -target
        new = calc_stocks_for_fuel_target(reactions, stocks)
        ore_consumption = abs(new["ORE"]["target"])
        print(last_ore_consumption, ore_consumption, target)
        if ore_consumption > 1000000000000:
            if next_step == 1:
                if last_ore_consumption != 0 and last_ore_consumption <= 1000000000000:
                    break
                else:
                    target -= next_step
            else:
                next_step = int(next_step / 2)
                target = target - next_step
        else:
            target += next_step
        last_ore_consumption = ore_consumption
    print(stocks, target)