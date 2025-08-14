from dice_probability import chance_to_hit_target

def parse_dice_input(dice_str):
    try:
        num, sides = dice_str.lower().split("d")
        return int(num), int(sides)
    except ValueError:
        raise ValueError("Invalid dice format. Use format like 2d6.")

def main():
    dice_input = input("Enter dice roll (e.g., 2d6): ")
    target = int(input("Enter target number: "))
    num_dice, sides = parse_dice_input(dice_input)
    chance = chance_to_hit_target(num_dice, sides, target)
    print(f"Chance of rolling {target} or higher: {chance:.2f}%")
    input("Press Enter to exit")

if __name__ == "__main__":
    main()
