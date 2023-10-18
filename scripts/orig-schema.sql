CREATE TABLE group_table (
    group_id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT,
    created_date DATE
);

CREATE TABLE user (
    user_id TEXT PRIMARY KEY,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    email TEXT,
    name TEXT
);

CREATE TABLE user_group (
    user_id TEXT NOT NULL,
    group_id TEXT NOT NULL,
    PRIMARY KEY (user_id, group_id),
    FOREIGN KEY (user_id) REFERENCES user(user_id),
    FOREIGN KEY (group_id) REFERENCES group_table(group_id)
);

CREATE TABLE post (
    post_id TEXT PRIMARY KEY,
    author_id TEXT NOT NULL,
    date_created DATE,
    likes INTEGER,
    recipe_id TEXT NOT NULL,
    tags TEXT,
    FOREIGN KEY (author_id) REFERENCES user(user_id),
    FOREIGN KEY (recipe_id) REFERENCES recipe(recipe_id)
);

CREATE TABLE recipe (
    recipe_id TEXT PRIMARY KEY,
    title TEXT,
    description TEXT,
    ingredients TEXT,
    instructions TEXT,
    difficulty_level INTEGER,
    image BLOB,
    food_type TEXT,
    recipe_source TEXT
);