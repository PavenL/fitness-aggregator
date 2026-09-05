#File that makes requests to https://api.hevyapp.com/v1/workouts (Hevy API)

import requests
import os

from dotenv import load_dotenv

load_dotenv()
HEVY_API_KEY = os.getenv("HEVY_API_KEY")

def get_hevy_workouts():
    workouts = requests.get('https://api.hevyapp.com/v1/workouts',params={"page": 1,"pageSize": 1},headers={'api-key':HEVY_API_KEY})
    return(workouts.json())