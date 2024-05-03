from models.location import Location


class Game:
    """
    Parent class for game creation

    """

    def __init__(self, prestige: int, atmosphere: str, title: str, introduction: str, description: str,
                 *location_map: dict):
        self.prestige = prestige
        self.atmosphere = atmosphere
        self.title = title
        self.introduction = introduction
        self.description = description
        self.locations = [Location(key, value) for key, value in location_map]
        self.current_location = self.locations[0] if self.locations else None

    def start(self):
        """
        Start the game
        :return: void
        """
        pass

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
