-- Create or update the user user_0d_1
CREATE USER IF NOT EXISTS user_0d_1 IDENTIFIED BY 'user_0d_1_pwd';
-- Grant all privileges to user_0d_1
GRANT ALL PRIVILEGES ON *.* TO user_0d_1;