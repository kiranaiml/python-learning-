#"The AI Data Scrubber"
clean_data = []
while True:
    variable=input("Enter data (or type 'quit' to stop): ")
    if variable=="quit":
        print("Shutting down scanner...")
        break
    elif variable == "bug" or variable == "virus":
        print("Corrupted data found! Skipping...")
        continue
    else:
        clean_data.append(variable)
        print("Data saved.")
        print(f"\nFinal clean database: {clean_data}")