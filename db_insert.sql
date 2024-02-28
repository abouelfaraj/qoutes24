
-- Inserting data into `user` table
INSERT INTO `user` (`Id`, `login`, `password`, `status`)
VALUES
    (4, 'user4', 'password4', 1)

-- Inserting data into `user_details` table
INSERT INTO `user_details` (`Id`, `name`, `email`, `birthday`, `Created_at`, `Modified_at`, `user_Id`)
VALUES
    (4, 'John Doe', 'john@example.com', '1990-05-15', '2024-02-27 08:00:00', '2024-02-27 08:00:00', 1),
    (5, 'Jane Smith', 'jane@example.com', '1985-10-20', '2024-02-27 09:00:00', '2024-02-27 09:00:00', 2),
    (6, 'Bob Johnson', 'bob@example.com', '1978-03-12', '2024-02-27 10:00:00', '2024-02-27 10:00:00', 3);