# TankFull Tracker

## Disclaimer

Please note that TankFull is currently in development and not production-ready. It may contain bugs and incomplete features. Also future releases may break backwards compatibility. Use at your own risk.

## Description

The TankFull Tracker is a straightforward and easy-to-use application designed to help vehicle owners keep track of their fuelings, charging, and distance driven. It's a practical tool for those who want to maintain a detailed record of their vehicle's energy use and travel distance. Users can log information like the date of fueling or charging, the amount of energy used, and the cost, along with the distance covered.

This application is especially useful for individuals looking to understand their vehicle's energy consumption patterns better. The TankFull Tracker offers a simple way to monitor and analyze fuel or electricity usage against the distance traveled, helping users make more informed decisions about their driving habits. While it may not have all the bells and whistles of more complex applications, its straightforward approach makes it accessible for anyone interested in tracking and improving their vehicle's energy efficiency.

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
SECRET_KEY=TankFull-changeme-u)(d4c7&icgd1wr_i5csk8@p8i56dsx9d@q14jyn&jyj8jj&l*
DEBUG=True
ALLOWED_HOSTS='*'
RESEND_API_KEY=changeme # api key for activating accounts
RESEND_FROM_EMAIL='info@example.com'
INTERNAL_IPS=127.0.0.1,localhost,0.0.0.0
REDIS_PASSWORD=changeme # redis cache password
```

### Docker

To install the TankFull Tracker using Docker, follow these steps:

1. Clone the repository to your local machine.

2. cd into the root directory.

3. Run the following command for redis cache:

    ```bash
    docker compose up
    ```

### Bare metal

To install the TankFull Tracker, follow these steps:

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

WIP

## License

This project is licensed under the MIT license.

## Contribution

To contribute to the TankFull Tracker, follow these steps:

1. Fork this repository.

2. Create a branch: `git checkout -b <branch_name>`.

3. Make your changes and commit them: `git commit -m '<commit_message>'`

4. Push to the original branch: `git push origin <project_name>/<location>`

5. Create the pull request.

Alternatively, see the GitHub documentation on [creating a pull request](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).

## Tests

WIP

## Questions

If you have any questions, comments, or concerns about the TankFull Tracker, you can post an issue on this repository.
