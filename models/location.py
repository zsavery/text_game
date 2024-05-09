class Location:
    @classmethod
    def from_nested_dict(cls, data: dict[dict]):
        """
        I pass in a nested dict of dict

        :param data:
        :type data: dict
        :return: Location
        """

        return cls(**data.items())

    def __init__(self, name: str, description: str, dir_choices=None):
        if dir_choices is None:
            dir_choices = {"North": None, "South": None,
                           "West": None, "East": None}
        try:
            self.name = name
        except TypeError:
            print("Wrong type entered in parameter: `name`\n" + "`str` expected")

        try:
            self.description = description
        except TypeError:
            print("Wrong type entered in parameter: `description`\n" + "`str` expected")

        self.north = dir_choices["North"]
        self.west = dir_choices["West"]
        self.south = dir_choices["South"]
        self.east = dir_choices["East"]



