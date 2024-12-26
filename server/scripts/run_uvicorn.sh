
# For some reason, running it while within the project source directory causes import error
# Doing this allows both fastapi and uvicorn cli to work.
echo "Changing directory"
pushd .. > /dev/null

uvicorn source.main_fastapi:app --host 0.0.0.0 --port 80 --log-config configurations/logging.yaml