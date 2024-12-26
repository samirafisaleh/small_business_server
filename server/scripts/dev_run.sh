
echo "Changing directory"
pushd ../source/ > /dev/null

echo "Loading configurations"
export $(cat ../configurations/common.env | xargs) 
export $(cat ../configurations/dev.env | xargs) 

fastapi dev main_fastapi.py