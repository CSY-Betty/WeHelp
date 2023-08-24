select database();
use website;

select * FROM member;

select * FROM member_test;
select * FROM member_test2;

SELECT * 
FROM member_test
WHERE username='test' and password='test';

SELECT * 
FROM member_test2
WHERE username='test' and password='test';

EXPLAIN SELECT name 
FROM member_test
WHERE username='test' and password='test';

EXPLAIN SELECT name 
FROM member_test2
WHERE username='test' and password='test';

SELECT * 
FROM member_test2
WHERE username='%test';

SELECT * 
FROM member_test2
WHERE username='test%';

EXPLAIN SELECT * 
FROM member_test2
WHERE username='%st';

EXPLAIN SELECT * 
FROM member_test2
WHERE username='te%';


CREATE INDEX name_idx ON member_test2 (username, password);
