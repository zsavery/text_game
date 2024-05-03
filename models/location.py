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

    def __init__(self, name: str, description: str):
        try:
            self.name = name
        except TypeError:
            print("Wrong type entered in parameter: `name`\n" + "`str` expected")

        try:
            self.description = description
        except TypeError:
            print("Wrong type entered in parameter: `description`\n" + "`str` expected")

