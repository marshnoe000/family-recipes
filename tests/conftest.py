import os
import sys
from pathlib import Path

import pytest
from dotenv import load_dotenv

from app import app
from scripts import init_db

TEST_DB = "scripts/test.db"
INIT_DB = "scripts/init_db.py"


@pytest.fixture
def client():
    BASE_DIR = Path(__file__).resolve().parent.parent
    os.environ["TESTING"] = "True"
    os.environ["ENV_PATH"] = "test.env"

    with app.app_context():
        sys.argv = [BASE_DIR.joinpath(INIT_DB), BASE_DIR.joinpath(TEST_DB),
                    "--force"]  # tell init_db where to build the database
        init_db.main()
        load_dotenv(BASE_DIR.joinpath("test.env"))
        yield app.test_client()  # tests run here
