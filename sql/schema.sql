PRAGMA foreign_keys = ON;

CREATE TABLE users(
  ID            INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  senderName    varchar(40) NOT NULL,
  senderEmail   varchar(50) NOT NULL,
  senderPhone   varchar(20) NOT NULL,
  receiverName  varchar(40) NOT NULL,
  receiverEmail varchar(50) NOT NULL,
  receiverPhone varchar(15) NOT NULL,
  street        varchar(150),
  city          varchar(30),
  zipcode       INTEGER NOT NULL,
  method        varchar(10) NOT NULL,
  created       datetime default current_timestamp
);


CREATE TABLE answers(
  ID        INTEGER NOT NULL PRIMARY KEY,
  answer0   varchar(50) NOT NULL,
  answer1   varchar(50) NOT NULL,
  answer2   varchar(50) NOT NULL,
  answer3   varchar(50) NOT NULL,
  answer4   varchar(50) NOT NULL,
  answer5   varchar(50) NOT NULL,
  answer6   varchar(50) NOT NULL,
  answer7   varchar(50) NOT NULL,
  answer8   varchar(50) NOT NULL,
  answer9   varchar(50) NOT NULL,
  answer10  varchar(50) NOT NULL,
  answer11  varchar(50) NOT NULL,
  answer12  varchar(50) NOT NULL,
  answer13  varchar(50) NOT NULL,
  answer14  varchar(50) NOT NULL,
  answer15  varchar(50) NOT NULL,
  FOREIGN KEY(ID) REFERENCES users(ID)
);
