
def find_num_1(response_list):
    responses = []
    for r in response_list:
        responses.extend([i for i in r])
    responses = list(set(responses))
    return len(responses)

def find_num_2(response_list):
    if len(response_list) == 0:
        return 0
    responses = set(response_list[0])
    if len(response_list) == 1:
        print(str(list(responses)) + "\t" + str(len(responses)))
        return len(list(responses))
    responses = list(responses.intersection(*response_list[1:]))
    print(str(responses) + "\t" + str(len(responses)))
    return len(responses)

def parse_file(input_file):
    responses = []
    family = []
    for r in input_file:
        if not r.strip():
            responses.append(family)
            family = []
        else:
            family.append(r)
    responses.append(family)

    return responses


file = "input_day6.txt"

with open(file, "r") as input:
    input_file = input.read().splitlines()

parsed_input_file = parse_file(input_file)

num_1 = 0
num_2 = 0
for family in parsed_input_file:
    num_1 += find_num_1(family)
    num_2 += find_num_2(family)

print("Number of exceptions, pt1:\t"+str(num_1))
print("Number of exceptions, pt2:\t"+str(num_2))
