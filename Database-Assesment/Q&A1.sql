CREATE TABLE Noble_win (
    year INT,
    subject VARCHAR(255) NOT NULL,
    winner VARCHAR(255) NOT NULL,
    country VARCHAR(255) NOT NULL,
    category VARCHAR(255) NOT NULL
);

INSERT INTO Noble_win (year, subject, winner, country, category) VALUES
    (1970, 'physics', 'hannes alfven', 'sweden', 'scientist'),
    (1970, 'physics', 'louis neel', 'france', 'scientist'),
    (1970, 'chemistry', 'luis federco leloir', 'france', 'scientist'),
    (1970, 'physiology', 'ulf von euler', 'sweden', 'scientist'),
    (1970, 'physiology', 'bernard ketz', 'germany', 'scientist'),
    (1970, 'literature', 'aleksandr solzhenitsyn', 'russia', 'linguist'),
    (1970, 'economics', 'paul samuelson', 'USA', 'economics'),
    (1970, 'physiology', 'julius axelrod', 'USA', 'scientist'),
    (1971, 'physics', 'dennis gabor', 'hungary', 'scientist'),
    (1971, 'chemistry', 'gerhard harzberg', 'germany', 'scientist'),
    (1971, 'peace', 'willy brandit', 'germany', 'chancellor'),
    (1971, 'literature', 'pablo neruda', 'chile', 'linguist'),
    (1971, 'economics', 'simon kuznets', 'russia', 'economist'),
    (1978, 'peace', 'anwar al-sadat', 'egypt', 'president'),
    (1978, 'peace', 'menachem begin', 'israel', 'prime minister'),
    (1987, 'chemistry', 'donald j cram', 'usa', 'scientist'),
    (1987, 'chemistry', 'jean-marie lehn', 'france', 'scientist'),
    (1987, 'physiology', 'susumu tonegawa', 'japan', 'scientist'),
    (1994, 'economics', 'reinhard selten', 'germany', 'economist'),
    (1994, 'peace', 'yitzhak rabin', 'israel', 'prime minister'),
    (1987, 'physics', 'johannes george bednorz', 'germany', 'scientist'),
    (1987, 'literature', 'joseph brodsky', 'russia', 'linguist'),
    (1987, 'economics', 'robert solow', 'USA', 'economist'),
    (1994, 'literature', 'kenzaburo oe', 'japan', 'linguist');

SELECT * FROM Noble_win;


--  Q-1  Write sql query to find the nobel prize winners of the year 1970. Return year,subject and winner

SELECT year, subject, winner
FROM Noble_win
WHERE year = 1970;


-- Q-2 Write sql query to find the nobel prize winners in chemistry between the years 1965 and 1975. Begin and end values are includedReturn year, subject, winner and country

SELECT year, subject, winner, country
FROM Noble_win
WHERE subject = 'chemistry' AND year BETWEEN 1965 AND 1975;


--  Q-3 Write sql query to retrieve the details of the winners whose first name matches with the string ‘Louis’. Return year,subject,winner,country


SELECT year, subject, winner, country
FROM Noble_win
WHERE winner LIKE 'Louis%';

--  Q-4 Write sql query to find Nobel prize winners for the subject that does not begin with the letter ‘P’. Order the result by year, descending and winner in ascending

SELECT year, subject, winner, country
FROM Noble_win
WHERE NOT subject LIKE 'P%'
ORDER BY year DESC, winner ASC;



-- Q-5  Write sql query to find the details of 1970 Nobel prize winners. Order the result by subject, ascending except for ‘Chemistry’ and ‘Economics’ which will come at the end of the result set. Return year, subject, winner , country and category




SELECT year, subject, winner, country, category
FROM Noble_win
WHERE year = 1970
ORDER BY
    CASE
        WHEN subject IN ('Chemistry', 'Economics') THEN 2
        ELSE 1
    END,
    subject ASC;
