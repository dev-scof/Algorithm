use madang;
SELECT * 
FROM Book;

SELECT bookname, price
FROM Book;

SELECT bookid, bookname, publisher, price
FROM Book;

SELECT publisher
FROM Book;

SELECT DISTINCT publisher # 중복을 제거할 때 DISTINCT를 사용한다.
FROM Book;

/* WHERE */
SELECT *
FROM Book
WHERE price < 20000;
# price가 20000 미만인 모든 속성을 출력

SELECT * 
FROM Book
WHERE price BETWEEN 10000 AND 20000;
# price가 10000이상 20000이하인 모든 속성을 출력

SELECT * 
FROM Book
WHERE publisher IN ('굿스포츠', '대한미디어');
# publisher가 ('굿스포츠', '대한미디어') 중에 있으면 모든 속성 출력

SELECT * 
FROM Book
WHERE publisher NOT IN ('굿스포츠', '대한미디어');
# publisher가 ('굿스포츠', '대한미디어') 중에 없으면 모든 속성 출력

SELECT bookname, publisher
FROM Book
WHERE bookname LIKE '축구의 역사';
# bookname이 '축구의 역사'인 bookname과 publisher를 출력

SELECT *
FROM Book
WHERE bookname LIKE '%축구%';
# bookname에 축구가 들어간 모든 속성 출력

SELECT *
FROM Book
WHERE bookname LIKE '_구%';
# bookname의 두번째 글자가 '구'가 들어간 모든 속성 출력
/* 와일드 문자
 +     : 문자열을 연결                 EX) '골프'+'바이블'
 %     : 0개 이상의 문자열과 일치        EX) '%축구%' : 축구를 포함하는 문자열
 []    : 1개 문자와 일치               EX) '[0-5]%' : 0-5 사이의 숫자로 시작하는 문자열
 [^]   : 1개의 문자와 불일치            EX) '[^0-5]%' : 0-5 사이의 숫자로 시작하지 않는 문자열
 _     : 특정 위치의 1개의 문자와 일치    EX) '_구%' : 두번째 위치에 '구'가 들어가는 문자열
*/

/* ORDER BY */
SELECT *
FROM Book
ORDER BY price, bookname;
# price로 정렬, 같은경우 bookname으로 정렬하여 모든 속성 출력 (default값은 오름차순이다.)

SELECT *
FROM Book
ORDER BY price DESC, publisher ASC;
# price로 내림차순 정렬을 하는데, 같은경우 publisher로 오름차순으로 정렬하여 모든 속성 출력

/* 집계함수 */
/*
- SUM([ALL | DISTINCT] 속성이름)
- AVG([ALL | DISTINCT] 속성이름)
- COUNT([ALL | DISTINCT] 속성이름 | *)
- MAX([ALL | DISTINCT] 속성이름)
- MIN([ALL | DISTINCT] 속성이름)
*/

SELECT (SUM(saleprice))
FROM Orders;
# Orders테이블의 모든 saleprice를 합한 값

SELECT SUM(saleprice) AS Total,
		AVG(saleprice) AS Average,
		Min(saleprice) AS Minimum,
        MAX(saleprice) AS Maximum
FROM Orders;
# 총 판매액, 평균값, 최저값, 최고가를 출력

/* GROUP BY */
SELECT custid, COUNT(*) AS 도서수량, SUM(saleprice) AS 총액
FROM Orders
GROUP BY custid;
# custid, COUNT(*), SUM(*)을 출력하는데, custid로 묶어서 연산하여 출력함

/* GROUP BY의 HAVING */
SELECT custid, COUNT(*) AS 도서수량
FROM Orders
WHERE saleprice >= 8000
GROUP BY custid
HAVING COUNT(*) >=2;
# custid, COUNT(*)을 출력하는데, saleprice >= 8000이고, 묶은 그룹의 COUNT(*)이 >= 2인 것을 출력

/* JOIN */
SELECT *
FROM Customer, Orders;
# 조건이 주어지지 않아서 카티전 프로덕트 연산이 이루어진다. // 논리에 맞지않는 레코드를 만들 수 있다.alter

SELECT *
FROM Customer, Orders
WHERE Customer.custid = Orders.custid;
# custid가 맞는 행들간으로 두 테이블을 합친다.

SELECT Customer.name, Book.bookname
FROM Customer, Orders, Book
WHERE Customer.custid = Orders.custid AND Orders.bookid=Book.bookid;
# 고객의 이름과 고객이 주문한 도서의 이름을 구하라 
# (Cutomer의 custid가 같은 Orders테이블에 접근하여, orders의 bookid가 같은 Book테이블을 연결함)
# Cutomer -> Orders -> Book

SELECT Customer.name, Book.bookname
FROM Customer, Orders, Book
WHERE Customer.custid = Orders.custid
	AND Orders.bookid = Book.bookid
    AND Book.price = 20000;
# 가격이 20000원인 도서를 주문한 고객의 이름과 도서의 이름을 구하시오

##########################################
SELECT Customer.name, saleprice
FROM Customer LEFT OUTER JOIN Orders
			ON Customer.custid = Orders.custid;

###########################################
/*부속질의*/
SELECT bookname FROM Book WHERE price = (SELECT MAX(price) FROM Book);

SELECT name FROM Customer WHERE custid IN (SELECT custid FROM Orders); # custid가 orders에 들어있는 name출력

#########################################
/*UNION 연산자*/
SELECT name FROM Customer WHERE address LIKE '대한민국%'
UNION
SELECT name FROM Customer WHERE custid IN (SELECT custid FROM Orders);
# address가 대한민국%인 customer의 이름과 
# custid가 orders에 있는 customer의 이름을 출력하라

# UNION ALL 연산은 중복된 것까지 모두 출력함

#############################################
/*Exists 존재하는지?*/
SELECT name, address 
FROM Customer cs 
WHERE EXISTS(
	SELECT * 
    FROM Orders od 
    WHERE cs.custid=od.custid)



SELECT * FROM Customer;
SELECT * FROM Orders;



# INSERT INTO Book VALUES(123, '들어간축구의 역사가', '삼성미디어', 12000);
 