import json
import os

import difflib

database = ["Dog", "cat", "dagg"]
user_input = ["deg", "Deg", "dDoGg", "horse", "fish"]

new_list = [difflib.get_close_matches(word, database) for word in user_input]

print(new_list)