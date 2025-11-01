import types
import uuid
import os
import datetime

# Create a custom module called 'helpers'
helpers = types.ModuleType("helpers")

# Define helper functions and variables
def uuid4():
    """Return a random UUID4 string."""
    return str(uuid.uuid4())

def ls(path="."):
    """List files in the given directory."""
    return os.listdir(path)

def now():
    """Return the current timestamp."""
    return datetime.datetime.now().isoformat()

# Attach them to the helpers module
helpers.uuid4 = uuid4
helpers.ls = ls
helpers.now = now

# Inject the helpers module into sys.modules
import sys
sys.modules["helpers"] = helpers

print("✅ Custom Python startup loaded!")
print("Available: helpers.uuid4(), helpers.ls(), helpers.now()")
