### Instruction
Activate virtual env. Here is a link: https://docs.python.org/3/library/venv.html


Open root directory and enter following commands:
```
pip3 install -r requirments.txt
cd api/
python3 manage.py makemigration
python3 manage.py migrate
python3 manage.py runserver
```


And open front/index.html in your browser. Enter some keyword, you will show 2 authors who fit better. 

Should working!