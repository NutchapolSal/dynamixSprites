import os
folderList = [
    "angelxangel",
    "arcanaidola",
    "blacksourruby",
    "chinesenewyear2019",
    "christmas2020",
    "corona",
    "crimson",
    "crosssoul",
    "deadsoul",
    "destroy_stress",
    "destruction",
    "dragonboatfestival2020",
    "easter2020",
    "emulisy",
    "fatalitysaga",
    "fireworks",
    "fl0atonair",
    "gessou",
    "glory_of_the_sacred_kingdom",
    "hakushokunoyumede",
    "halloween2018",
    "halloween2019",
    "halloween2020",
    "highschoolqueen",
    "hoshizoratoraberu",
    "hyper-nova",
    "joaochimd",
    "kumoru",
    "lastarcady",
    "lifestyle",
    "lonelycat",
    "lumina",
    "masscontrol",
    "mindblast",
    "mlg",
    "moonlit_party",
    "moshimoshibit",
    "movingon",
    "nacl",
    "nameless",
    "ngan4mui4faa1",
    "noisia",
    "omohidefantasia",
    "petalstep",
    "prismaticflipper",
    "reefhideout",
    "road_to_773h",
    "rudy",
    "sin",
    "sky_land",
    "snowylight",
    "speedstertrickster",
    "strawberrypassion",
    "summer2018",
    "thepath",
    "wonderfuldays",
    "xmas2017",
    "youth"
]


def main():
    for v in folderList:
        # os.mkdir(v)
        os.mkdir('../' + v)
        print(v)
        input(">")
        for w in os.listdir('./out'):
            os.rename('./out/' + w, '../' + v + '/' + w)


if __name__ == "__main__":
    main()