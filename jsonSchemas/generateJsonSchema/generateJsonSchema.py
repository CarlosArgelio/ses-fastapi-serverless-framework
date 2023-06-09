# python
import os
import json

# dotenv
from dotenv import load_dotenv

# services
from models.emailModels import inbox_schema

load_dotenv()

JSON_SCHEMA_URL = os.getenv('JSON_SCHEMA_URL')
PATH_SAVE = 'jsonSchemas/schemas'

inbox_schema['$schema'] = JSON_SCHEMA_URL

if not os.path.exists(PATH_SAVE):
    os.makedirs(PATH_SAVE)

with open(PATH_SAVE + f'/{str( inbox_schema["title"]).lower() }.json', 'w', encoding='utf-8') as f:
    json.dump(inbox_schema, f, ensure_ascii=False, indent=4)