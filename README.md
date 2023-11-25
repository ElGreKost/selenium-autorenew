# LibraryBookAutoRenewal

## Overview
LibraryBookAutoRenewal is an automated tool designed to streamline the process of renewing library books. Utilizing Python and Selenium, this application automates the interaction with library systems to extend the loan periods of borrowed books, ensuring timely renewals and helping users avoid overdue fines.
There are two versions one for windows with Microsoft edge web driver not yet implemented the auto executable to startup and one for linux where everything is automated.
## Features
- **Automated Renewal**: Automatically renews library books on or near their due dates.
- **Selenium Integration**: Leverages the power of Selenium for web automation to interact with online library systems.
- **Ease of Use**: Simple setup and minimal user intervention required once configured.

## Prerequisites
- Python 3.x
- Selenium WebDriver
- Libraries: `selenium`, `webdriver_manager`, `datetime`

## Installation and Setup

### Step 1: Clone the Repository
Clone the repository to your local machine:

```
git clone https://github.com/[YourUsername]/LibraryBookAutoRenewal.git
cd LibraryBookAutoRenewal
```

### Step 2: Install Dependencies
Install the required Python packages:

``````
pip install -r requirements.txt
``````


## Usage
Once set up, the application will run automatically at system startup, checking and renewing books as needed based on their due dates.

## Contributing
Contributions to the LibraryBookAutoRenewal project are welcome. Please feel free to fork the repository, make improvements, and submit pull requests.

## Disclaimer
This tool is provided as-is, and users should ensure it complies with their library's terms of service.
