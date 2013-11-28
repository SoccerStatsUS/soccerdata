import os
import yaml

from soccerdata.settings import ROOT_DIR

DIR = os.path.join(ROOT_DIR, 'soccerdata/data/')


def load_teams():
    p = os.path.join(DIR, 'teams.yaml')
    return yaml.load(open(p))

if __name__ == "__main__":
    print(load_teams())
