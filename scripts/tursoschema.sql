CREATE TABLE batch (
    batch_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    created_date DATE
);
CREATE TABLE post (
    post_id INTEGER PRIMARY KEY AUTOINCREMENT,
    author_id INTEGER NOT NULL,
    recipe_id INTEGER NOT NULL,
    date_created DATE,
    likes INTEGER,
    tags TEXT,
    FOREIGN KEY (author_id) REFERENCES user(user_id),
    FOREIGN KEY (recipe_id) REFERENCES recipe(recipe_id)
);
CREATE TABLE recipe (
    recipe_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    description TEXT,
    ingredients TEXT,
    instructions TEXT,
    difficulty_level INTEGER,
    image BLOB,
    food_type TEXT,
    recipe_source TEXT
);
CREATE TABLE user (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password_hash TEXT NOT NULL,
    password_salt TEXT NOT NULL,
    email TEXT,
    name TEXT
);
CREATE TABLE user_batch (
    user_id INTEGER NOT NULL,
    batch_id INTEGER NOT NULL,
    PRIMARY KEY (user_id, batch_id),
    FOREIGN KEY (user_id) REFERENCES user(user_id),
    FOREIGN KEY (batch_id) REFERENCES batch(_id)
);
