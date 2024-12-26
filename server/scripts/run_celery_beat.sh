

echo "Changing directory"
pushd .. > /dev/null

celery -A source.shared.celery beat 