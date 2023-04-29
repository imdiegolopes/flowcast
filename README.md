<p align="center">
  <img src="./docs/moody.png" alt="Logo" width="80" height="80">

  <h3 align="center">Moody</h3>
  <p align="center">Track your moods, find your balance with Moody.</p>
</p>

# Moody

Moody is a powerful platform designed to help people track and manage their mental health. By providing a simple and intuitive interface, Moody allows users to easily log their daily moods and emotions, and track how they change over time. With features like personalized recommendations and community support, Moody helps users take charge of their mental well-being and stay on top of their emotional health. Whether you're struggling with depression, anxiety, or just looking to better understand your emotions,

As an MVP developed for the first sprint of PUC-Rio's Post Graduation Course in Software Engineering, this product currently offers only basic functionalities.

## Moody Server

This repository contains all the necessary files to run the API project that powers the Moody platform. The application was built using the software design philosophy of Clean Architecture and Domain-Driven Design, using Python and Flask technology.

## Prerequisites

Before running the project, you need to have the following prerequisites installed on your system:

- Python 3.x version
- Pip
- sqlite3

To install all dependencies within the requirements.txt file, use the following command:

```bash
make install
```

To run the project and bootstrap the server on localhost on port 5000, use the following command:

```bash
make run
```

Alternatively, if you prefer to execute the project using Poetry, you can run:

```bash
poetry add $( cat requirements.txt )
```

## Running tests

To run the tests, you must have Python 3 and Pytest installed on your system.

To run the tests, follow these steps:

- Clone this repository to your local machine.
- In your terminal, navigate to the project's root directory.
- Install Pytest by running pip install pytest.
- Run pytest to execute all tests.

```bash
make test
```

If all tests pass, you should see a summary of the tests run and their results.

If you would like to run a specific test file or test case, you can use the -k option followed by the name of the test file or test case.

For example, to run only the test cases for the Moody class, run pytest -k "test_moody".
