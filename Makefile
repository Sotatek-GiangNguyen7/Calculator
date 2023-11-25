install:
	pip install -r requirements.txt

test:	
	python tests/test_pyautogui.py 

report:
	pytest tests/ --html-report=./report