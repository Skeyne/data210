# JSON Basics (in Python)

### Reading JSON from a file

`json.load(file)` # actual file != file name.

use with context:
`with open('data.json','r') as json_file:`

returns a python dictionary object

### Reading JSON from a string

`json.loads(json_string)`

returns a python dictionary object

### Writing JSON to a file

`json.dump(object, out_json_file)`

use with context:
`with open('data.json','w') as json_file:`

### Writing JSON to a string

`json.dumps(object)` returns a json string