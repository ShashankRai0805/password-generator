# Password Generator

## Overview
This Python script generates random, secure passwords using a mix of nouns, adjectives, numbers, and special symbols. The program utilizes an external API to fetch random words, ensuring unique and creative password combinations. Users can generate multiple passwords, and the program runs interactively until the user decides to exit.

## Features
- **Randomly generated password**: Combines a noun and an adjective from an API, random numbers, and special characters.
- **User choice**: After each password generation, users can choose to generate another password or exit the program.
  
### Generated Password Structure:
- Two random words (noun + adjective), with the first letter of each capitalized.
- Three random digits.
- Three random special symbols from a predefined list.

## Requirements
- Python 3.x
- `requests` library for making API calls.

### Installation of Dependencies:
To install the required Python package, run:
```bash
pip install requests
```

## How to Run the Program
1. Download or clone the repository to your local machine.
2. Navigate to the directory where the script is located.
3. Run the script using the following command:
   ```bash
   python password_generator.py
   ```
   
### Example Output:
```bash
WELCOME TO PASSWORD GENERATOR!
GENERATING PASSWORD...
GENERATED PASSWORD : SunnyCat123!@#
DO YOU WANT TO GENERATE ANOTHER PASSWORD(Y/N) : Y
GENERATING PASSWORD...
GENERATED PASSWORD : BrightDog456$%?
DO YOU WANT TO GENERATE ANOTHER PASSWORD(Y/N) : N
```

## How the Password is Generated
- The script makes API requests to retrieve random nouns and adjectives:
  - Noun API: `https://random-word-form.herokuapp.com/random/noun`
  - Adjective API (Note: There’s a typo in the code, where the adjective API is currently set to a noun endpoint, which should be corrected): `https://random-word-form.herokuapp.com/random/adjective`
- **Random Numbers**: Three digits are randomly selected.
- **Special Symbols**: Three random symbols are picked from a list of common symbols like `!`, `@`, `#`, `$`, etc.

The final password is constructed in the following format:
```python
"{Adjective}{Noun}{Digit1}{Digit2}{Digit3}{Symbol1}{Symbol2}{Symbol3}"
```

## Example of the Code Snippet:
```python
password = f"{adjective.capitalize()}{noun.capitalize()}{num1}{num2}{num3}{symbol1}{symbol2}{symbol3}"
```

## Notes
- Ensure that the adjective URL is correctly used in the code to get the desired word type:
  ```python
  adjectiveURL = "https://random-word-form.herokuapp.com/random/adjective"
  ```

## License
This project is licensed under the MIT License, allowing you to freely use, modify, and distribute the script with proper attribution.