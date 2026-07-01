import os

from dotenv import find_dotenv, load_dotenv

dotenv_path = find_dotenv()
load_dotenv(dotenv_path, verbose=True)
# print(dotenv_path)

find_you = os.environ.get("VERY_IMP_VARIABLE")
print(f"{find_you=}")
