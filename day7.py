def parse_rule(rule_text):
    parent = rule_text[:rule_text.find("bags contain") - 1]
    remaining_text = rule_text[len(parent) + len("bags contain") + 2:]
    rule = {parent: {}}
    for bag_rule in remaining_text.split(", "):
        if "no other bags" in bag_rule:
            continue
        num = int(bag_rule.split(" ")[0])
        bag_type = " ".join(bag_rule.split(" ")[1:3])
        rule[parent].update({bag_type: num})

    return rule


def could_contain(bag_color, rule_set, containing_bags=[]):
    bags_contain = [
        col for col in rule_set.keys()
        if rule_set.get(col).get(bag_color, False)
    ]
    if bags_contain == []:
        return list(set(containing_bags))
    else:
        for c in bags_contain:
            containing_bags.extend(could_contain(
                c, rule_set, bags_contain.copy()))
        return list(set(containing_bags))

def num_bags(bag_color, rule_set):
    contained_bags = rule_set.get(bag_color)
    if contained_bags == {}:
        return 0
    else:
        contains_bags = 0
        for color, num in contained_bags.items():
            contains_bags += num * (1 + num_bags(color, rule_set))
        return contains_bags


def parse_rule2(rule_set, rule_dict={}):
    if len(rule_set) == 0:
        return rule_dict
    rule_text = rule_set.pop(0)
    parent = rule_text[:rule_text.find("bags contain") - 1]
    remaining_text = rule_text[len(parent) + len("bags contain") + 2:]
    if not rule_dict.get(parent):
        rule_dict[parent] = []
    for bag_rule in remaining_text.split(", "):
        if "no other bags" in bag_rule:
            continue
        bag_type = " ".join(bag_rule.split(" ")[1:3])
        if rule_dict.get(bag_type):
            rule_dict[bag_type].append(parent)
        else:
            rule_dict[bag_type] = [parent]
    return parse_rule2(rule_set, rule_dict)


def could_contain2(bag_color, rule_set):
    bags_contain = rule_set.get(bag_color)
    if bags_contain == []:
        return []
    else:
        containing_bags = bags_contain.copy()
        for containing_color in bags_contain:
            containing_bags.extend(could_contain2(
                containing_color, rule_set))
        return list(set(containing_bags))


file = "input_day7.txt"
test_color = "shiny gold"

with open(file, "r") as input:
    input_file = input.read().splitlines()

#rule_set = parse_rule(input_file)
rule_set = {}
for i in input_file:
    rule_set.update(parse_rule(i))
bags_could_contain = could_contain(test_color, rule_set)
print(len(bags_could_contain))
num_contained_bags = num_bags(test_color, rule_set)
print(f"Contains:\t{num_contained_bags}")