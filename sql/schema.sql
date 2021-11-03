PRAGMA foreign_keys = ON;

CREATE TABLE users(
  ID INT IDENTITY(1,1) NOT NULL PRIMARY KEY,
  senderName varchar(50) NOT NULL,
  senderEmail varchar(50) NOT NULL,
  SenderPhone varchar(20) NOT NULL,
  receiverName  varchar(50) NOT NULL,
  receiverEmail varchar(50) NOT NULL,
  receiverPhone  varchar(20) NOT NULL,
  street VARCHAR(150),
  city VARCHAR(50),
  zipcode INTEGER NOT NULL,
  method INTEGER NOT NULL,
  created datetime default current_timestamp
);


CREATE TABLE answers(
  ID INTEGER NOT NULL PRIMARY KEY,
  answer0 INTEGER NOT NULL,
  answer1 INTEGER NOT NULL,
  answer2 INTEGER NOT NULL,
  answer3 INTEGER NOT NULL,
  answer4 INTEGER NOT NULL,
  answer5 INTEGER NOT NULL,
  answer6 INTEGER NOT NULL,
  answer7 INTEGER NOT NULL,
  answer8 INTEGER NOT NULL,
  answer9 INTEGER NOT NULL,
  answer10 INTEGER NOT NULL,
  answer11 INTEGER NOT NULL,
  answer12 INTEGER NOT NULL,
  answer13 INTEGER NOT NULL,
  FOREIGN KEY(ID) REFERENCES users(ID)
);
