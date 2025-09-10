# Secure Password Manager

#### Video Demo: https://youtu.be/iBvYESLq5eU

#### Description:

The **Secure Password Manager** is a tool that helps users create, check, store, and manage passwords safely. It
improves security without needing any advanced technical knowledge.

Here’s what it can do:

1. **Check Password Strength:** It scores password strength based on length, uppercase/lowercase letters, numbers, and symbols. And then it displays a report and an overall score (weak, medium, or strong).

2. **Generate Random Passwords:** It creates a strong password of user-defined length with letters, numbers, and symbols. After it is generated, a user will be prompted if they would like to save it or not.

3. **Check for Breaches:** It checks if a password has appeared in known data breaches using the "Have I Been Pwned" API.

4. **Save Passwords Securely:** It encrypts a password and saves it to a local txt file. Ensuring that only this program can decrypt and read it.

5. **Load Saved Passwords:** It decrypts and displays all previously saved passwords for the user to view securely.


**File Descriptions:**

* `project.py`: Main code.
* `test_project.py`: Pytest tests.
* `requirements.txt`: List of Python packages needed.
* `README.md`: Project documentation.

#### Design Choices:

* **Encryption:** I chose to use Fernet encryption because it is simple to use and fulfills the function of protecting my passwords efficiently.
* **Checking Breaches:** The program connects to the "Have I Been Pwned" API to check if a password has appeared on their database. When a password is typed, it is hashed, and only a portion of the hash is sent to the API. When a list of possible matches is returned, they are compared with the original hash. If the password is found, the program warns the user so they can choose a safer one.

#### How to Use:


1. Install dependencies: using pip install

2. Run the program:

```
python project.py
```

3. Menu Usage:

   * **Press `0` to Quit:** to exit the program.

   * **Press `1` to Check Password Strength:**

     * Prompt: `Input your password here to check its strength:`
     * Input your password.
     * Output: it displays the conditions that the password passed or failed to pass (length, uppercase, lowercase, digit, symbol) and a total strength score (weak, medium, strong).

   * **Press `2` to Generate a Random Password:**

     * Prompt: `To generate a password, please type how many letters it should have (we recommend that the password be longer than 12 letters):` Enter a number.
     * Output: The generated password gets displayed.
     * Prompt: `Do you want to save this password for later use? (y/n):` Choose `y` to save or `n` to skip.

   * **Press `3` to Check if a Password Has Been Breached:**

     * Prompt: `Input your password here to check if your password has been breached:`
     * Output: Display either `this password has been leaked` or `Safe. not found in known breaches`.

   * **Press `4` to Save a Password Manually:**

     * Prompt: `Input your password here to save it:` Enter your password.
     * Output: Displays `Password saved successfully!` or displays an error if something goes wrong.

   * **Press `5` to Load All Saved Passwords:**

     * Output: Displays all decrypted passwords stored locally. If no passwords exist, it displays `No saved passwords found`.

4. Run tests to verify functionality:

```
pytest test_project.py
```

#### Limitations and Future Ideas:

* Right now, passwords are stored locally; cloud storage could be added in the future.
* Checking for breaches requires an internet connection.
* A graphical interface could make it easier for users who don’t like command lines.

This project demonstrates the practical application of Python for encryption, password security checks, file handling, and testing. It’s a tool I built to make password management straightforward, understandable, and safe.