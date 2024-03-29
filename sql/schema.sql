CREATE TABLE users(
  ID            SERIAL PRIMARY KEY,
  exid          varchar(100) NOT NULL,
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
  created       TIMESTAMP default current_timestamp,
  paid          INTEGER default 0
  -- 0 is false, 1 is true
);


CREATE TABLE answers(
  ID        INTEGER PRIMARY KEY,
  answer1   varchar(100) NOT NULL,
  answer2   varchar(100) NOT NULL,
  answer3   varchar(100) NOT NULL,
  answer4   varchar(100) NOT NULL,
  answer5   varchar(100) NOT NULL,
  answer6   varchar(100) NOT NULL,
  answer7   varchar(100) NOT NULL,
  answer8   varchar(100) NOT NULL,
  answer9   varchar(100) NOT NULL,
  answer10  varchar(100) NOT NULL,
  answer11  varchar(100) NOT NULL,
  answer12  varchar(100) NOT NULL,
  answer13  varchar(100) NOT NULL,
  answer14  varchar(100) NOT NULL,
  answer15  varchar(100) NOT NULL,
  answer16  varchar(100) NOT NULL,
  answer17  varchar(100) NOT NULL,
  FOREIGN KEY(ID) REFERENCES users(ID)
);
