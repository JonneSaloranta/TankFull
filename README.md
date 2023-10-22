# Refuel Data Tracker

## Description

The Refuel Data Tracker is a tool designed to help users keep track of their refueling data. It is a simple and user-friendly application that allows users to input their refueling data, such as the date, the amount of fuel, and the cost of fuel. The application then calculates the fuel efficiency and displays it to the user. This information can be useful for those who want to monitor their fuel consumption and make adjustments to their driving habits to save money and reduce their carbon footprint. The Refuel Data Tracker is a great tool for anyone who wants to keep track of their fuel consumption and make informed decisions about their driving habits.

## Table of Contents

-   [Installation](#installation)
-   [Usage](#usage)
-   [License](#license)
-   [Contribution](#contribution)
-   [Tests](#tests)
-   [Questions](#questions)

## Installation

Create a .env file in the root directory and add the following environment variables:

```bash
SECRET_KEY=your_secret_key
DEBUG=True or False
ALLOWED_HOSTS='localhost', '*', '123.45.67.89' # example
```

### Docker

To install the Refuel Data Tracker using Docker, follow these steps:

1. Clone the repository to your local machine.

2. Install [Docker](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install/).

3. Run the application using the following command:

    ```bash
    docker-compose up
    ```

### Bare metal

To install the Refuel Data Tracker, follow these steps:

1. Clone the repository to your local machine.

2. Install Python 3.9.6 or later.

3. Install the required packages using the following command:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the application using the following command:

    ```bash
    python manage.py runserver
    ```

## Usage

To use the Refuel Data Tracker, follow these steps:

1. Navigate to the Refuel Data Tracker website.

2. Click on the "Sign Up" button to create an account.

3. Enter your information and click on the "Sign Up" button.

4. Click on the "Log In" button to log in to your account.

5. Enter your information and click on the "Log In" button.

6. Click on the "Add Data" button to add your refueling data.

7. Enter your refueling data and click on the "Add Data" button.

8. Click on the "View Data" button to view your refueling data.

9. Click on the "Log Out" button to log out of your account.

## License

This project is licensed under the MIT license.

## Contribution

To contribute to the Refuel Data Tracker, follow these steps:

1. Fork this repository.

2. Create a branch: `git checkout -b <branch_name>`.

3. Make your changes and commit them: `git commit -m '<commit_message>'`

4. Push to the original branch: `git push origin <project_name>/<location>`

5. Create the pull request.

Alternatively, see the GitHub documentation on [creating a pull request](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).

## Tests

WIP

## Questions

If you have any questions, comments, or concerns about the Refuel Data Tracker, you can post an issue on this repository.
