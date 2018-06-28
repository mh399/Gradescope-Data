import yaml
import json

with open('MARKOV_submission_metadata.yml', 'r') as stream:
    y = yaml.load(stream)

with open('MARKOV_submission_metadata.json', 'w') as outfile:
    json.dump(y, outfile, default=str)