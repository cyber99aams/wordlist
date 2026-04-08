import random

def generate_random_list():
    try:
        # Taking input from the user
        d = int(input("Enter number of digits (e.g., 4, 6): "))
        filename = f"{d}digit.txt"
        
        total_combinations = 10**d
        print(f"Processing... Generating {total_combinations} combinations.")
        
        # Creating a list of numbers from 0 to 10^d
        nums = [f"{i:0{d}}\n" for i in range(total_combinations)]
        
        print("Shuffling passwords to randomize the order...")
        # Shuffling the list
        random.shuffle(nums)
        
        # Saving to file
        print(f"Saving to '{filename}'...")
        with open(filename, "w") as f:
            f.writelines(nums)
            
        print(f"Success! Your {d}-digit random list has been created.")

    except ValueError:
        print("Invalid input! Please enter a number only (e.g., 4 or 6).")
    except MemoryError:
        print("Memory Error! The list is too large for your device's RAM.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    generate_random_list()

