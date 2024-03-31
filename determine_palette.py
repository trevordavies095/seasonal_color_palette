def determine_palette(skin_color, eye_color, hair_color):
    # Define color palettes and their associated characteristics
    palettes = {
        "Spring": {
            "skin": ["#F0CDBB", "#FDD7B6", "#FFDCB7"],
            "eye": ["#76776E", "#4C504E", "#5E6D70"],
            "hair": ["#3E2E23", "#392F27", "#61462F"]
        },
        "Summer": {
            "skin": ["#D9BFA9", "#E0C1AC", "#E8D0BE"],
            "eye": ["#5C757D", "#7E888B", "#9BA5A6"],
            "hair": ["#2E2A29", "#3B3638", "#4E474B"]
        },
        "Autumn": {
            "skin": ["#FDD7B6", "#FFDABF", "#EFC4B0"],
            "eye": ["#4C504E", "#5A605A", "#6D746D"],
            "hair": ["#392F27", "#61462F", "#5A3E34"]
        },
        "Winter": {
            "skin": ["#CABFB2", "#C2BEB2", "#B8B9B8"],
            "eye": ["#2B2C2E", "#353A3E", "#454A4F"],
            "hair": ["#19191A", "#1F1E1F", "#272425"]
        }
    }

    # Calculate the distance between the input colors and each palette
    distances = {}
    for palette, colors in palettes.items():
        distance = sum(abs(int(skin_color, 16) - int(color, 16)) +
                       abs(int(eye_color, 16) - int(color, 16)) +
                       abs(int(hair_color, 16) - int(color, 16)) for color in colors["skin"] + colors["eye"] + colors["hair"])
        distances[palette] = distance

    # Determine the palette with the minimum distance
    min_distance_palette = min(distances, key=distances.get)
    
    return min_distance_palette

# Example usage:
skin_color = "#FDD7B6"
eye_color = "#4C504E"
hair_color = "#392F27"

palette = determine_palette(skin_color, eye_color, hair_color)
print("Your color palette is:", palette)
