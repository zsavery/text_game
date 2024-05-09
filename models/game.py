from models.location import Location


class Game:
    """
    Parent class for game creation

    """

    set_of_locations = None

    def __init__(self, prestige, atmosphere, title, introduction, description,
                 starting_locaation: Location):
        """
        Arguments:
            prestige: Difficulty of game
            atmosphere: Tone of game
            title: Game title
            introduction: A short line/quote to add impact to game atmosphere
            description:
            location_map: List of of locations
        """
        self.prestige = prestige
        self.atmosphere = atmosphere
        self.title = title
        self.introduction = introduction
        self.description = description
        self.current_location = starting_locaation

    def _add_location(self, *locations):

        if locations:
            if isinstance(locations[0], dict):
                self.locations.extend(Location(location["name"], location["description"]) for location in locations)
                return
            elif isinstance(locations[0], tuple):
                self.locations.extend(Location(name, desc) for name, desc in locations)
                for name, desc in locations:
                    self.locations.append(Location(name, desc))
                    return
            elif isinstance(locations[0], ):
                for name, desc in locations:
                    self.locations.append(Location(name, desc))
                    return

        return

