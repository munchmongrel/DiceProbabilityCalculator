from dice_probability import calculate_top_two_probability

def main():
    try:
        num_dice = int(input("Enter number of d6 dice to roll: "))
        if num_dice < 2:
            print("Error: You must roll at least 2 dice to calculate top two results.")
            input("Press Enter to exit")
            return
        target = int(input("Enter target sum for the top two dice: "))
        chance, note = calculate_top_two_probability(num_dice, target)
        print(f"\nRolling {num_dice}d6:")
        print(f"Chance that the top two dice sum to {target} or higher: {chance:.2f}%")
        if note:
            print(f"({note})")
    except ValueError:
        print("Error: Please enter valid integers.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    input("\nPress Enter to exit")

if __name__ == "__main__":
    main()
