
-- Table: user
CREATE TABLE IF NOT EXISTS user (
    id INTEGER NOT NULL AUTO_INCREMENT, 
    login VARCHAR(128) NOT NULL, 
    password VARCHAR(1000) NOT NULL, 
    status BOOLEAN NOT NULL, 
    created_at DATETIME, 
    updated_at DATETIME, 
    PRIMARY KEY (id)
);

-- Table: user_details
CREATE TABLE IF NOT EXISTS user_details (
    id INTEGER NOT NULL AUTO_INCREMENT, 
    name VARCHAR(45) NOT NULL, 
    email VARCHAR(128) NOT NULL, 
    birthday DATE NOT NULL, 
    address VARCHAR(128) NOT NULL, 
    created_at DATETIME, 
    updated_at DATETIME, 
    user_id INTEGER, 
    PRIMARY KEY (id), 
    FOREIGN KEY(user_id) REFERENCES user (id)
);

-- Table: quotes_category
CREATE TABLE IF NOT EXISTS quotes_category (
    id INTEGER NOT NULL AUTO_INCREMENT, 
    title VARCHAR(45) NOT NULL, 
    created_at DATETIME NOT NULL, 
    created_by VARCHAR(45) NOT NULL, 
    modified_at DATETIME NOT NULL, 
    modified_by VARCHAR(45) NOT NULL, 
    deleted_by VARCHAR(45) NOT NULL, 
    deleted_at DATETIME NOT NULL, 
    PRIMARY KEY (id)
);

-- Table: quotes
CREATE TABLE IF NOT EXISTS quotes (
    id INTEGER NOT NULL AUTO_INCREMENT, 
    content VARCHAR(300) NOT NULL, 
    status BOOLEAN NOT NULL, 
    created_at DATETIME, 
    deleted_at DATETIME, 
    visibility BOOLEAN NOT NULL, 
    modified_at DATETIME NOT NULL, 
    modified_by VARCHAR(45) NOT NULL, 
    deleted_by VARCHAR(45) NOT NULL, 
    category_id INTEGER, 
    PRIMARY KEY (id), 
    FOREIGN KEY(category_id) REFERENCES quotes_category (id)
);

-- Table: quote_user
CREATE TABLE IF NOT EXISTS quote_user (
    user_id INTEGER NOT NULL, 
    quote_id INTEGER NOT NULL, 
    PRIMARY KEY (user_id, quote_id), 
    FOREIGN KEY(user_id) REFERENCES user (id), 
    FOREIGN KEY(quote_id) REFERENCES quotes (id)
);

-- Table: review
CREATE TABLE IF NOT EXISTS review (
    id INTEGER NOT NULL AUTO_INCREMENT, 
    content VARCHAR(450) NOT NULL, 
    score INTEGER NOT NULL, 
    PRIMARY KEY (id)
);

-- Table: review_user
CREATE TABLE IF NOT EXISTS review_user (
    user_id INTEGER NOT NULL, 
    review_id INTEGER NOT NULL, 
    PRIMARY KEY (user_id, review_id), 
    FOREIGN KEY(user_id) REFERENCES user (id), 
    FOREIGN KEY(review_id) REFERENCES review (id)
);

-- Table: user_role
CREATE TABLE IF NOT EXISTS user_role (
    id INTEGER NOT NULL AUTO_INCREMENT, 
    title VARCHAR(250) NOT NULL, 
    user_id INTEGER NOT NULL, 
    PRIMARY KEY (id), 
    FOREIGN KEY(user_id) REFERENCES user (id)
);
