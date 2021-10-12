PRAGMA foreign_keys = ON;

CREATE TABLE users(
  sender   varchar(20) NOT NULL,
  receiver  varchar(40) NOT NULL,
  email     varchar(40) NOT NULL,
  phone     varchar(64) NOT NULL,
  created   datetime default current_timestamp,
  PRIMARY KEY(sender)
);
