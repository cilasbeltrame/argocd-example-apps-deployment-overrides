#! /usr/bin/env python3

import yaml
from jinja2 import Environment, FileSystemLoader

# Load YAML data
import sys

# Check if config path is provided as an argument
if len(sys.argv) <= 1:
    print("Warning: Config file path is required as an argument")
    sys.exit(0)

config_path = sys.argv[1]
with open(config_path, "r") as file:
    data = yaml.safe_load(file)

# Set up Jinja2 environment
env = Environment(loader=FileSystemLoader("templates"))  # Look in templates directory
template = env.get_template("application.j2")

# Render the template with YAML data
output = template.render(data)

print(output)
# Get output file path from arguments or use a default
output_file = sys.argv[2] if len(sys.argv) > 2 else "application.yaml"

# Write the rendered template to a file
try:
    with open(output_file, "w") as file:
        file.write(output)
except Exception as e:
    print(f"Error writing to {output_file}: {e}")
    sys.exit(1)

print(f"Application manifest written to {output_file}")
