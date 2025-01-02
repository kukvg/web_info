
# Web Information Automation Script

This script automates the collection of web information for domains listed in a CSV file. It captures screenshots of webpages, retrieves HTTP status codes, and saves the results in a structured output file for analysis or reporting.

---

## Features

### 1. **Webpage Screenshot Capture**
- Captures screenshots of the webpages listed in the input CSV file. 
- Each screenshot is saved with a unique identifier based on the order of the URLs in the file.

### 2. **HTTP Status Code Retrieval**
- Checks the HTTP status code of each domain to verify availability or identify potential issues.

### 3. **Automated Reporting**
- Generates a result file (`result.txt`) that logs the HTTP status codes alongside the corresponding domain information for easy reference.

---

## Prerequisites

### Software Requirements
- **Python**: The primary programming language used in this script.
- **Selenium**: A Python library used for browser automation.
- **Requests**: A Python library used for making HTTP requests.
- **Pandas**: A Python library used for reading and processing the CSV file containing domain information.

### System Requirements
- **Google Chrome**: The browser used for automation.
- **Chromedriver**: A driver that allows Selenium to interact with Google Chrome.

### Files Needed
1. **Input File**: A CSV file (`domain.csv`) containing the list of domains to process. Each domain should be listed under a column named `url`.
2. **Output Files**:
   - `result.txt`: The file where HTTP status codes and domain results are saved.
   - **Screenshot Directory**: A folder where screenshots of the domains will be stored.

---

## Install Dependencies

To set up the environment and run the script, follow these steps:

### 1. Install Required Python Libraries
Run the following command to install the necessary libraries:
```bash
pip install selenium requests pandas
```

### 2. Download and Set Up Chromedriver
1. Download the appropriate version of Chromedriver for your Chrome browser from [Chromedriver Downloads](https://chromedriver.chromium.org/downloads).
2. Note the location where you save the Chromedriver executable.

### 3. Update the Script Variables
Edit the script (`web_info.py`) to set the paths.

### 4. Verify Folder Structure
Ensure your project directory contains the necessary folders and files:
```
/path_to/web_info/
├── domain.csv       # Input file with domain names
├── result.txt       # Output file for results
├── scr/             # Folder to store screenshots
```

### 5. Run the Script
Once all dependencies and paths are configured, run the script:
```bash
python web_info.py
```

---

## Usage

1. **Prepare the Input File**:  
   Ensure the input CSV file (`domain.csv`) is correctly formatted with a column named `url` containing the domains.

2. **Run the Script**:  
   Execute the script as described above.

3. **Check the Results**:  
   - Review the `result.txt` file for HTTP status codes and domain information.
   - Access the screenshot directory to view the captured webpage screenshots.

---

## Built With
- **Python** - The main programming language.
- **Selenium** - For browser automation and screenshot capturing.
- **Requests** - For retrieving HTTP status codes.
- **Pandas** - For processing domain data.

---

## Author
Dominik Kuka

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

## Inspiration
This script was created to automate the tedious process of webpage verification, making it easier to analyze and document domain accessibility efficiently.
