PRAGMA foreign_keys = ON;

CREATE TABLE users(
  username  varchar(20) NOT NULL,
  fullname  varchar(40) NOT NULL,
  email     varchar(40) NOT NULL,
  filename  varchar(64) NOT NULL,
  password  varchar(256) NOT NULL,
  created   datetime default current_timestamp,
  PRIMARY KEY(username)
);