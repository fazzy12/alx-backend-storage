# MongoDB NoSQL Python Scripts

This repository contains a collection of Python scripts for working with MongoDB NoSQL databases. Each script performs a specific task related to data manipulation, querying, and analysis using pymongo, a Python driver for MongoDB.

## Table of Contents

1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Scripts Overview](#scripts-overview)
5. [Contributing](#contributing)
6. [License](#license)

## Introduction

MongoDB is a popular NoSQL database that provides flexible schema design and scalability for modern applications. These scripts offer practical solutions for common database operations such as querying, updating, inserting, and analyzing data stored in MongoDB collections.

## Installation

To use these scripts, follow these steps:

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/your-username/mongodb-nosql-python-scripts.git
    ```

2. Install the required Python packages:

    ```bash
    pip install pymongo
    ```

## Usage

Each script is designed to perform a specific task and can be executed independently. To run a script, simply navigate to the project directory and execute the script using Python:

```bash
python script_name.py
```

Replace `script_name.py` with the name of the script you want to execute.

## Scripts Overview

Here is an overview of the scripts available in this repository:

1. **[1-find](1-find.py)**: Finds documents in a collection based on specified criteria.
2. **[2-insert](2-insert.py)**: Inserts a new document into a collection.
3. **[3-update](3-update.py)**: Updates existing documents in a collection.
4. **[4-match](4-match.py)**: Lists all documents with a specific name in the collection.
5. **[5-count](5-count.py)**: Displays the number of documents in a collection.
6. **[6-update](6-update.py)**: Adds a new attribute to documents with a specific name in the collection.
7. **[7-delete](7-delete.py)**: Deletes all documents with a specific name in the collection.
8. **[8-all](8-all.py)**: Lists all documents in a collection.
9. **[9-insert_school](9-insert_school.py)**: Inserts a new document into a collection based on specified arguments.
10. **[10-update_topics](10-update_topics.py)**: Updates topics of a school document based on the name.
11. **[11-schools_by_topic](11-schools_by_topic.py)**: Returns the list of schools having a specific topic.
12. **[12-log_stats](12-log_stats.py)**: Provides statistics about Nginx logs stored in MongoDB.
13. **[100-find](100-find.py)**: Lists all documents with names starting with "Holberton" in the collection.
14. **[101-students](101-students.py)**: Returns all students sorted by average score.
15. **[102-log_stats](102-log_stats.py)**: Improved version of log_stats script with top 10 most present IPs.

## Contributing

Contributions to this repository are welcome. If you have any suggestions for improvements or new scripts to add, feel free to open an issue or create a pull request.

## License

This project is licensed under the MIT License. Feel free to modify and distribute the code for personal or commercial use.
