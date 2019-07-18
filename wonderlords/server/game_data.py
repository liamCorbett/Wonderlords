from urllib.request import urlopen
import json

# Import JSON
UNITS_JSON_URL = 'https://raw.githubusercontent.com/SteamDatabase/GameTracking-Underlords/master/game/dac/pak01_dir/scripts/units.json'  # noqa
ALLIANCES_JSON_URL = 'https://raw.githubusercontent.com/SteamDatabase/GameTracking-Underlords/master/game/dac/pak01_dir/scripts/synergies.json'  # noqa

with urlopen(UNITS_JSON_URL) as h_url:
    units_json = json.load(h_url)

with urlopen(ALLIANCES_JSON_URL) as a_url:
    alliances_json = json.load(a_url)

# Lowercase all alliance identifiers to match w/ units_json
alliances_json = {k.lower(): v for (k, v) in alliances_json.items()}

# Lists
heroes = []
classes = []
races = []

# Add to lists
for hero, attributes in units_json.items():

    # Only add if unit is playable hero
    if attributes['draftTier'] <= 0:
        continue

    heroes.append(hero)

    for alliance in attributes['keywords'].split():

        if alliance in races or alliance in classes:
            continue
        if alliances_json[alliance]['type'] == 'Class':
            classes.append(alliance)
        if alliances_json[alliance]['type'] == 'Race':
            races.append(alliance)

# Sort Lists
heroes.sort(key=str.lower)
classes.sort(key=str.lower)
races.sort(key=str.lower)


# Build Hero Matrix
def build_hero_matrix():

    # Initialize matrix with "None"s that will be replaced where necessary
    hero_matrix = [[None]*len(classes) for _ in range(len(races))]

    for hero, attributes in units_json.items():

        # Only add if unit is playable hero
        if attributes['draftTier'] <= 0:
            continue

        keywords = attributes['keywords'].split()

        unit_classes = [x for x in keywords if x in classes]
        unit_races = [x for x in keywords if x in races]

        for unit_race in unit_races:
            for unit_class in unit_classes:

                row = races.index(unit_race)
                col = classes.index(unit_class)

                if hero_matrix[row][col] is None:
                    hero_matrix[row][col] = [hero]
                else:
                    hero_matrix[row][col] += [hero]

    return hero_matrix

hero_matrix = build_hero_matrix()
