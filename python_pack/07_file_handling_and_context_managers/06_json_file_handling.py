import json

profile = {
    "name": "Anita",
    "skills": ["Python", "SQL"],
    "active": True,
}

with open("profile.json", "w", encoding="utf-8") as file:
    json.dump(profile, file, indent=4)

with open("profile.json", "r", encoding="utf-8") as file:
    loaded_profile = json.load(file)
    print(loaded_profile)
