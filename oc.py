try:
    res = 190 / 0
except Exception as error:
    print("An exception occurred:", type(error).__name__)
