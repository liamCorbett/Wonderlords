from urllib.request import urlopen
import json

# Import JSON
HEROES_JSON_URL = 'https://raw.githubusercontent.com/SteamDatabase/GameTracking-Underlords/master/game/dac/pak01_dir/scripts/units.json'  # noqa
ALLIANCES_JSON_URL = 'https://raw.githubusercontent.com/SteamDatabase/GameTracking-Underlords/master/game/dac/pak01_dir/scripts/synergies.json'  # noqa

with urlopen(HEROES_JSON_URL) as h_url:
    heroes_json = json.load(h_url)

with urlopen(ALLIANCES_JSON_URL) as a_url:
    alliances_json = json.load(a_url)

# Lowercase all alliance identifiers to match w/ heroes_json
alliances_json = {k.lower(): v for (k, v) in alliances_json.items()}

# Lists
heroes = []
classes = []
races = []

# Add to lists
for hero, attributes in heroes_json.items():

    # Only add if unit is playable
    if attributes['draftTier'] > 0:

        heroes.append(hero)

        for alliance in attributes['keywords'].split():

            if alliance in races or alliance in classes:
                continue
            if alliances_json[alliance]['type'] == 'Class':
                classes.append(alliance)
            if alliances_json[alliance]['type'] == 'Race':
                races.append(alliance)

heroes.sort(key=str.lower)
classes.sort(key=str.lower)
races.sort(key=str.lower)
