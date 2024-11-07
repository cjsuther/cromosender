# SmartClaimMedicalValidation
This project is the service main orchestration.
Path projects includes:
- /invoicevision

## How start with this project locally

1. `virtualenv env`
2. `source env/bin/activate`
3. `pip install -r requirements.txt`
4. `python process.py`

## How run this project locally with Docker

1. `docker compose up -d`

### REMEMBER!!!
If you add a new library, please update requirements.txt.
You can use this command if tou prefere.

`pip freeze > requirements.txt`
