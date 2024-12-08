def calculate_love_score(name1, name2):
    # Combine both names and convert to lowercase
    combined_names = (name1 + name2).lower()
    
    # Count occurrences of the letters in "TRUE"
    true_count = (
        combined_names.count('t') +
        combined_names.count('r') +
        combined_names.count('u') +
        combined_names.count('e')
    )
    
    # Count occurrences of the letters in "LOVE"
    love_count = (
        combined_names.count('l') +
        combined_names.count('o') +
        combined_names.count('v') +
        combined_names.count('e')
    )
    
    # Combine counts to form a 2-digit love score
    love_score = int(str(true_count) + str(love_count))
    
    # Print the result in the required format
    print(f"Love Score = {love_score}")

# Test the function with the example
calculate_love_score("Kanye West", "Kim Kardashian")
