
# For some reason, running it while within the project source directory causes import error
# Doing this allows both fastapi and uvicorn cli to work.
echo "Changing directory"
pushd .. > /dev/null

gunicorn -c configurations/gunicorn.config.py -w 2 'source.main_fastapi:app'