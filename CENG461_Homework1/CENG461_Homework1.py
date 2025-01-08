class PartyGoer:
    def __init__(self, actual):
        self.food_domain = ["egg roll", "fries", "gingerbread", "hummus"]
        self.time_domain = [4.30, 4.35, 4.40, 4.45]
        self.actual_values = actual

    def get_food_domain(self):
        return self.food_domain

    def get_time_domain(self):
        return self.time_domain

    def get_actual_values(self):
        return self.actual_values


# creating an object of class Party_goer for
# each party-goer
amber = PartyGoer({"food": "", "arrival_time": 0})
brian = PartyGoer({"food": "", "arrival_time": 0})
chris = PartyGoer({"food": "", "arrival_time": 0})
diane = PartyGoer({"food": "", "arrival_time": 0})


def actual_value_assignment(lcv, position, any_domain):
    if isinstance(lcv, str):
        if position == 0:
            (amber.get_actual_values())["food"] = lcv

        elif position == 1:
            (brian.get_actual_values())["food"] = lcv

        elif position == 2:
            (chris.get_actual_values())["food"] = lcv

        elif position == 3:
            (diane.get_actual_values())["food"] = lcv

        for i in range(0, len(any_domain)):  # try making comment
            if lcv in any_domain[i] and position != i:
                any_domain[i].remove(lcv)

        any_domain[position] = [""]

    elif isinstance(lcv, float):
        if position == 0:
            (amber.get_actual_values())["arrival_time"] = lcv

        elif position == 1:
            (brian.get_actual_values())["arrival_time"] = lcv

        elif position == 2:
            chris.get_actual_values()["arrival_time"] = lcv

        elif position == 3:
            (diane.get_actual_values())["arrival_time"] = lcv

        for i in range(0, len(any_domain)):
            if lcv in any_domain[i] and position != i:
                any_domain[i].remove(lcv)
        any_domain[position] = [""]


def apply_arc_consistency(lcv, index):
    for i in brian.get_food_domain():
        if i != "hummus" or i != "fries":
            (brian.get_food_domain()).remove(i)
        if "hummus" not in brian.get_food_domain():
            brian.get_food_domain().append("hummus")

    if "gingerbread" in chris.get_food_domain():
        (chris.get_food_domain()).remove("gingerbread")

    if "hummus" in diane.get_food_domain():
        (diane.get_food_domain()).remove("hummus")

    if index == 1 and lcv == 'hummus':
        (chris.get_food_domain()).remove("fries")

    if 4.45 in amber.get_time_domain():
        (amber.get_time_domain()).remove(4.45)

    if 4.40 in brian.get_time_domain():
        (brian.get_time_domain()).remove(4.40)

    if 4.30 in brian.get_time_domain():
        (brian.get_time_domain()).remove(4.30)

    if 4.40 in chris.get_time_domain():
        chris.get_time_domain().remove(4.40)

    if 4.30 in diane.get_time_domain():
        diane.get_time_domain().remove(4.30)

    if (brian.get_actual_values())["food"] == "hummus" and 4.45 in brian.get_time_domain():
        (brian.get_time_domain()).remove(4.45)

    if brian.get_actual_values()["food"] == "hummus" and amber.get_actual_values()["arrival_time"] == 4.30:
        if "fries" in amber.get_food_domain():
            amber.get_food_domain().remove("fries")

    if (brian.get_actual_values())["arrival_time"] != 0:
        for i in amber.get_time_domain():
            if i != ((brian.get_actual_values())["arrival_time"]) - 0.05:
                (amber.get_time_domain()).remove(i)

    general_food_domain = [amber.get_food_domain(), brian.get_food_domain(), chris.get_food_domain(),
                           diane.get_food_domain()]

    general_time_domain = [amber.get_time_domain(), brian.get_time_domain(), chris.get_time_domain(),
                           diane.get_time_domain()]

    return general_food_domain, general_time_domain


def print_domains():
    print("\nDomains:")
    print("Amber food domain : ", amber.get_food_domain())
    print("Brian food domain : ", brian.get_food_domain())
    print("Chris food domain : ", chris.get_food_domain())
    print("Diane food domain : ", diane.get_food_domain(), "\n")

    print("Amber time domain : ", amber.get_time_domain())
    print("Brian time domain : ", brian.get_time_domain())
    print("Chris time domain : ", chris.get_time_domain())
    print("Diane time domain : ", diane.get_time_domain(), "\n")


def print_values():
    print("\nVALUES AFTER ASSIGNMENTS")
    print("Amber: ", amber.get_actual_values())
    print("Brian: ", brian.get_actual_values())
    print("Chris: ", chris.get_actual_values())
    print("Diane: ", diane.get_actual_values())


def assignment_check(value, any_domain):
    count = 0
    copied_list = create_list_copy(any_domain)
    for i in copied_list:
        if value in i:
            i.remove(value)

    for i in copied_list:
        count += len(i)

    return count


def create_list_copy(any_domain):
    copy_list = []

    for i in any_domain:
        sub_list = []
        for j in i:
            sub_list.append(j)
        copy_list.append(sub_list)

    return copy_list


def find_var_mrv(domain):
    len_min = 1000
    variable_min = []

    for variable in domain:
        if len(variable) < len_min and variable != [""]:
            len_min = len(variable)
            variable_min = variable

    return variable_min, domain.index(variable_min)


def find_val_lcv(any_domain, variable_min, position):
    temp = variable_min
    any_domain.remove(variable_min)
    real_count = 0
    lcv = ""

    for i in range(len(variable_min)):
        count = assignment_check(variable_min[i], any_domain)
        if count > real_count:
            real_count = count
            lcv = variable_min[i]

    any_domain.insert(position, temp)
    return lcv, position


def check_solution_reached(party_goer_list):
    stop = True

    for i in party_goer_list:
        if "" == i.get_actual_values()["food"] or 0 == i.get_actual_values()["arrival_time"]:
            stop = False

    return stop


def main():
    # for first arc_consistency check parameters does not matter
    # it applies when the program started for the first time
    domain_of_foods, domain_of_times = apply_arc_consistency(["null"], -5)
    print_values()
    print_domains()

    party_goer_list = [amber, brian, chris, diane]

    while True:

        variable_min_food, food_position = find_var_mrv(domain_of_foods)
        food_lcv, food_position = find_val_lcv(domain_of_foods, variable_min_food, food_position)
        apply_arc_consistency(food_lcv, food_position)
        print("\nARC CONSISTENCY CHECKED")
        if check_solution_reached(party_goer_list): break
        print_values()
        print_domains()

        for j in domain_of_foods:
            if len(j) == 1:
                actual_value_assignment(food_lcv, food_position, domain_of_foods)

        print_values()
        print_domains()
        if check_solution_reached(party_goer_list): break
        apply_arc_consistency(["null"], -5)
        print("\nARC CONSISTENCY CHECKED")
        if check_solution_reached(party_goer_list): break
        print_values()
        print_domains()
        variable_min_time, time_position = find_var_mrv(domain_of_times)
        time_lcv, time_position = find_val_lcv(domain_of_times, variable_min_time, time_position)

        for j in domain_of_times:
            if len(j) == 1:
                actual_value_assignment(time_lcv, time_position, domain_of_times)

        apply_arc_consistency(["null"], -5)
        print("\nARC CONSISTENCY CHECKED")
        if check_solution_reached(party_goer_list): break
        print_domains()
        print_values()

    print("SOLUTION IS REACHED")
    print("Amber: ", amber.get_actual_values())
    print("Brian: ", brian.get_actual_values())
    print("Chris: ", chris.get_actual_values())
    print("Diane: ", diane.get_actual_values())


# driver code
main()
