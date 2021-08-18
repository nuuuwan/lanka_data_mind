"""Uploaded data to nuuuwan/lanka_data_mind:data branch."""

import os


def upload_data():
    """Upload data."""
    os.system('echo "test data" > /tmp/lanka_data_mind.test.txt')
    os.system('echo "# lanka_data_mind" > /tmp/README.md')


if __name__ == '__main__':
    upload_data()
