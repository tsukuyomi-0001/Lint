import json

def load(name):
    with open(name+'-map.linx', 'r') as f:
        map = json.load(f)
    
    with open(name+'-fom.linx', 'r') as f:
         fom = json.load(f)

    return [map, fom]

def store(directory, file, name):
    with open(name+'-map.linx', 'w') as f:
        json.dump(directory, f)

    with open(name+'-fom.linx', 'w') as f:
            json.dump(file, f)