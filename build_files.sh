# build_files.sh
#!/bin/bash

# Collect static files
echo "Collecting static files"
python3 manage.py collectstatic --noinput

# Any other build steps go here
