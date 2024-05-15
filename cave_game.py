from models.game import Game
from models.location import Location

"""
A game where an adventurer enters a mysterious cave
"""
# cave_game = Game(2, "spooky", "Dark Cave", "Find the lost treasure stolen from the Silver Tower.",
#                  "You have been tasked with hunting down the band of thieves that stolen this harvest taxes.",
#                  ["Cave Entrance", "Division in mountain wall.", {"North": Location("Glowing Path", "", {}),
#                                                                   "West": Location("Red Path", "", {}),
#                                                                   "East": Location("Green Path", "", {})}])


class DarkCave(Game):

    def __init__(self, prestige, atmosphere, title, introduction, description, locations):
        super().__init__(prestige, atmosphere, title, introduction, description, locations)

    def _go(self, direction: str):
        pass


def scene_cave_entrance(game: DarkCave, flag):
    if game.current_location.name == "Cave Entrance":
        while(True):
            print(f"West: {game.current_location.west.name}")
            print(f"East: {game.current_location.east.name}")
            print(f"North: {game.current_location.north.name}")
            print(f"South {game.current_location.west.name}")

            responce = input("\n Enter direction ")
            if (responce != )
    return flag

if __name__ == '__main__':
    game_details = {'prestige': 2, "atmosphere": "spooky", "title": "Dark Cave",
                    "introduction": "Find the lost treasure stolen "
                                    "from the Silver Tower.",
                    "description": "You have been tasked with hunting down the band of thieves that stolen this "
                                   "harvest taxes.",
                    "locations": None}
    loc_1 = ["Cave Entrance", "Division in mountain wall.", {"North": Location("Glowing Path", ""),
                                                             "West": Location("Red Path", ""),
                                                             "East": Location("Green Path", ""),
                                                             "South": None
                                                             }]
    loc_1 = Location(*loc_1)
    loc_2 = ["Shing Lake", "A glowing lake that sparkle with the light of the Moons.",
             {"North": loc_1.west,
              "West": Location("Red Path", ""),
              "East": Location("Green Path", ""),
              "South": None
              }
             ]
    loc_2 = Location(*loc_2)

    loc_1.east = loc_2
    game_details["locations"] = loc_1
    game = DarkCave(**game_details)

    print(game.current_location.name)
