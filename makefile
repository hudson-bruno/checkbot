dev:
	poetry run watchmedo auto-restart -p "*.py" -R python -- src/__main__.py

