python_requirement_library( 
  name = 'python_requirement_library',
  requirements = [python_requirement('heronpy==0.0.0')] 
)

python_library( 
  name = 'spout-bolt-py',
  sources = ['*.py', '!topology.py']
)

python_binary( 
  name = "exclamation-topology",
  sources = ['topology.py'], 
  dependencies = [':spout-bolt-py', 
                  ':python_requirement_library'] 
)