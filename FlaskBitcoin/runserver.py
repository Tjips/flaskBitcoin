"""
This script runs the FlaskBitcoin application using a development server.
"""

from os import environ
from FlaskBitcoin import app

if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True)