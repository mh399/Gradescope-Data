import yaml
import json


def default_ctor(loader, tag_suffix, node):
    print(loader)
    print(tag_suffix)
    print(node)
    return tag_suffix + " " + node.value


yaml.add_multi_constructor("", default_ctor)


with open('MARKOV_submission_metadata.yml', 'r') as stream:
    y = yaml.load(stream)

yaml.ScalarNode(tag=u'!binary', value=u'')

with open('MARKOV_submission_metadata.json', 'w') as outfile:
    json.dump(y, outfile, default=str)