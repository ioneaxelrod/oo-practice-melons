############
# Part 1   #
############


class MelonType:
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""

        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name
        self.pairings = []

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    muskmelon = MelonType("musk", 1998, "green", True, True, "Muskmelon")
    muskmelon.add_pairing("mint")

    casaba = MelonType("cas", 2003, "orange", False, False, "Casaba")
    casaba.add_pairing("strawberries")
    casaba.add_pairing("mint")

    crenshaw = MelonType("cren", 1996, "green", False, False, "Crenshaw")
    crenshaw.add_pairing("proscuitto")

    yellow_watermelon = MelonType("yw", 2013, "yellow", False, True, "Yellow Watermelon")
    yellow_watermelon.add_pairing("ice cream")

    all_melon_types.append(muskmelon)
    all_melon_types.append(casaba)
    all_melon_types.append(crenshaw)
    all_melon_types.append(yellow_watermelon)

    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""
    for melon_type in melon_types:
        print(f"{melon_type.name} pairs with ")
        for pairing in melon_type.pairings:
            print(f"- {pairing}")
        print()

    # Fill in the rest


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melon_type_lookup = {}

    for melon_type in melon_types:
        melon_type_lookup[melon_type.code] = melon_type

    return melon_type_lookup

    # Fill in the rest

############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""

    def __init__(self, melon_type, shape_rating, color_rating, field_harvested,
                 harvester):

        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.field_harvested = field_harvested
        self.harvester = harvester

    def is_sellable(self):
        return self.shape_rating > 5 and self.color_rating > 5 and self.field_harvested != 3


def make_melons(melon_types):
    """Returns a list of Melon objects."""
    melon_list = []
    melon_types = make_melon_type_lookup()


    melon_1 = Melon(melon_types["yw"], 8, 7, 2, "Sheila")
    melon_2 = Melon(melon_types["yw"], 3, 4, 2, "Sheila")
    melon_3 = Melon(melon_types["yw"], 9, 8, 3, "Sheila")
    melon_4 = Melon(melon_types["cas"], 10, 6, 35, "Sheila")
    melon_5 = Melon(melon_types["cren"], 8, 9, 35, "Michael")
    melon_6 = Melon(melon_types["cren"], 8, 2, 35, "Michael")
    melon_7 = Melon(melon_types["cren"], 2, 3, 4, "Michael")
    melon_8 = Melon(melon_types["musk"], 6, 7, 4, 'Michael')
    melon_9 = Melon(melon_types["yw"], 7, 10, 3, "Sheila")

    melon_list.extend([melon_1, melon_2, melon_3, melon_4, melon_5, melon_6,
                       melon_7, melon_8, melon_9])
    return melon_list


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""
    for melon in melons:
        if melon.is_sellable():
            can_be_sold = "# CAN BE SOLD"
        else:
            can_be_sold = "# NOT SELLABLE"
        print(f"Harvest by {melon.harvester} from Field {melon.field_harvested} {can_be_sold}")


def get_melons_from_file(filename):
    
    melons = []
    melon_type_lookup = make_melon_type_lookup(make_melon_types())

    with open(filename) as file:
        for line in file:
            data = line.split()
            shape = int(data[1])
            color = int(data[3])
            melon_type = melon_type_lookup[data[5]]
            harvester = data[8]
            field = int(data[11])
            melon = Melon(melon_type, shape, color, field, harvester)
            melons.append(melon)

    return melons


melon_types = make_melon_types()
print_pairing_info(melon_types)
lookup = make_melon_type_lookup(melon_types)
# get_sellability_report(make_melons(melon_types))

get_sellability_report(get_melons_from_file("harvest_log.txt"))
