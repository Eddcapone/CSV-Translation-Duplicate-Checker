# CSV Translation Checker

This application was developed to assist in the translation process by allowing users to check a list of new translated strings against an existing CSV file of translations. It helps ensure that strings are not duplicated in the CSV before being added.

**Note**: There is also a webapp Version for this application [here](https://github.com/Eddcapone/CSV-Translation-Duplicate-Checker-Webapp).

## Features

- Compare a list of strings (e.g., new translations) with the entries in a CSV file.
- Check against both the first column and the column after the first comma in the CSV.
- Identify duplicates in the CSV for the column after the first comma.
- Display results dynamically in the GUI, including:
  - **Found Strings**: Strings from the input list that already exist in the CSV.
  - **Not Found Strings**: Strings from the input list that are not in the CSV.
  - **Duplicates After Comma**: Strings in the second column of the CSV that are duplicated.

## How to Use

1. **Clone the Repository**:
   ```
   git clone https://github.com/Eddcapone/CSV-Translation-Duplicate-Checker
   cd csv-translation-checker
   ```

2. **Install Python**: Ensure you have Python 3 installed on your system.

3. **Run the Application**:
   - On Windows:
     ```
     python main.py
     ```
   - On macOS/Linux:
     ```
     python3 main.py
     ```

4. **Use the Application**:
   - Upload a CSV file containing your existing translations.
   - Enter a list of new translations (one string per line) into the text area.
   - Click the **Check Words** button to process the data.

5. **View the Results**:
   - **Found Words**: Strings from your input list that match entries in the CSV.
   - **Not Found Words**: Strings from your input list that do not match any entries in the CSV.
   - **Duplicates After Comma**: Entries in the second column of the CSV that are duplicated.

## Example Input and Output

### Example CSV (`translations.csv`):
```
"Your Address", "Votre adresse"
Personal Details, Informations personnelles
"Password Strength","Force du mot de passe"
"No Password","aucun mot de passe"
"No Password","Foo"
"Bar","aucun mot de passe"
```

### Example Input (Text Area):
```
Password Strength
Votre adresse
Prix
```

### Example Output:

![image](https://github.com/user-attachments/assets/70604afd-c9c4-477f-84a7-0ae180411a6b)

```
Found Words:
  password strength
  votre adresse

Not Found Words:
  Prix

Duplicates in CSV:
  no password
  aucun mot de passe
```

## Notes

- Strings are compared without case sensitivity or surrounding quotes (e.g., `"Password Strength"` and `password strength` are treated as equal).
- The application dynamically updates the progress bar and results list to ensure responsiveness.

#### Fixed
- Ensured accurate comparison of input strings against both columns.

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
