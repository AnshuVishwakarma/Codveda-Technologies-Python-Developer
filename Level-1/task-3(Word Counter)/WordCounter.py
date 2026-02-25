def count_words_in_file(filename):
    try:
        # Open the file in read mode
        with open(filename, 'r') as file:
            content = file.read()
            
            # Split content into words
            words = content.split()
            
            # Count words
            word_count = len(words)
            
            print(f"\nTotal number of words: {word_count}")

    except FileNotFoundError:
        print("Error: File not found. Please check the file name.")
    
    except Exception as e:
        print("An error occurred:", e)


# Take file name from user
filename = input("Enter the file name (with .txt extension): ")

count_words_in_file(filename)