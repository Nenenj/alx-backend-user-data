#!/usr/bin/env python3
"""
Main file
"""

from filtered_logger import get_db, filter_datum

def test_get_db():
    """Function to test database connection."""
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT COUNT(*) FROM users;")
    for row in cursor:
        print(f"Number of users: {row[0]}")
    cursor.close()
    db.close()

def test_filter_datum():
    """Function to test filter_datum."""
    fields = ["password", "date_of_birth"]
    messages = [
        "name=egg;email=eggmin@eggsample.com;password=eggcellent;date_of_birth=12/12/1986;",
        "name=bob;email=bob@dylan.com;password=bobbycool;date_of_birth=03/04/1993;"
    ]

    for message in messages:
        print(filter_datum(fields, 'xxx', message, ';'))

if __name__ == "__main__":
    # Test the get_db function
    test_get_db()

    # Test the filter_datum function
    test_filter_datum()
