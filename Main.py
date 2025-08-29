# calling the main text file
def main():
    #Checking if the code was found
    try:
        #opens the text file and makes it look nice
        with open("Positive-Words.txt") as f:
            lines = f.readlines()
            words = [line.strip() for line in lines]

        print(words)
    #   If the file was not found
    except FileNotFoundError:
        print(f"Error: File Not Found.")
    # If there was a differnt code
    except Exception as e:
        print(f"Error Occurred {e}")

if __name__ == "__main__":
    main()