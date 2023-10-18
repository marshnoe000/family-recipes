#!python
import libsql_client as libsql
import sys
import os


def main():
    if len(sys.argv) > 1:
        db_file = sys.argv[1]
    else:
        db_file = "./recipes.db"

    if os.path.isfile(db_file):
        yn = input(f"found existing db: '{db_file}', delete and rebuild this db? y/n ")
        if yn.lower() == "n" or yn.lower() == "no":
            print("Pass in a file path to create db at a different location")
            sys.exit(0)

    db = libsql.create_client_sync(url=f"file:{db_file}")

    statements = None
    # todo: should this be dynamic?
    with open("./scripts/schema.sql") as f:
        statements = [libsql.Statement(stat) for stat in f.read().split(';')]

    print(f"creating db at '{db_file}' ...")
    _ = db.batch(statements)
    print("done!")

    db.close()


if __name__ == "__main__":
    main()
