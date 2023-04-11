# MY_SQL
## CMD 명령어

### 1. mysql -u ["root"] - p
- mysql : 실행할 프로그램(mysql)을
- -u root :접속할 서버 이름 (root)에 접속하여
- -p : 패스워드를 입력하라


### 2. show databases;
- 데이터베이스들의 목록을 보여줘라

### 3. create database ["dbname"]
- "dbname"의 데이터베이스를 생성하라

### 4. use ["dbname"]
- "dbname"의 데이터베이스를 사용한다.

### 5. show tables;
- 현재 데이터베이스의 테이블들을 보여줘라

### 6. desc ["tablename"]
- "tablename"의 테이블의 구조를 보여줘라

## SQL Query

### DDL : CAD (CREATE / ALTER / DROP)
1. CREATE
    ``` sql
    CREATE DATABASE ["dbname"]
    - "dbname"의 데이터베이스 생성
    ```
    ``` sql
    CREATE TABLE ["table name"] (
        '속성 이름1' '데이터 타입' '[DEFAULT 형식]',
        '속성 이름2' '데이터 타입' '[DEFAULT 형식]',
        '속성 이름3' '데이터 타입' '[DEFAULT 형식]',
        
        '[DEFAULT 형식]'에는 다음과 같은 내용이 들어갈 수 있다.
        - PRIMARY KEY
        - UNIQUE KEY
        - NOT NULL
        - CHECK
        - FOREIGN KEY
        ...
        ...
        ...

        '제약조건(CONSTRAINT)'
        - 컬럼 LEVEL 방식 : 
            - 속성, 데이터 타입을 기술할 때 조건을 같이 기술하는 방식
            - EX) 'NAME' 'VARCHAR(20)' 'NOT NULL', 
        - 테이블 LEVEL 방식 : 
            - 쿼리의 마지막에 모든 제약 조건을 기술하는 방식
            - EX) CONSTRAINT PLAYER_PK PRIMARY KEY (PLAYER_ID),

    );
    ```
- 테이블명은 객체를 의미할 수 있는 적절한 이름을 사용한다. 가능한 "단수형"을 권고한다.
- 테이블 명은 다른 테이블의 이름과 중복되지 않아야 한다.
- 한 테이블 내에서는 컬럼명이 중복되게 지정될 수 없다.
- 테이블 이름을 지정하고 각 컬럼들은 괄호 "( )" 로 묶어 지정한다.
- 각 컬럼들은 콤마 ","로 구분되고, 테이블 생성문의 끝은 항상 세미콜론 ";"로 끝난다.
- 컬럼에 대해서는 다른 테이블까지 고려하여 데이터베이스 내에서는 일관성 있게 사용하는 것이 좋다.
- 컬럼 뒤에 데이터 유형은 꼭 지정되어야 한다.
- 테이블명과 컬럼명은 반드시 문자로 시작해야 하고, 벤더별로 길이에 대한 한계가 있다.
- 벤더에서 사전에 정의한 예약어(Reserved word)는 쓸 수 없다.
- A-Z, a-z, 0-9, _, $, # 문자만 허용된다.
- 출처: [개발이 하고 싶어요](https://hyeonstorage.tistory.com/291)

2. ALTER

3. DROP
``` sql
DROP DATABASE IF EXISTS ["dbname"]
- "dbname"의 데이터베이스가 존재하면 삭제

DROP USER IF EXISTS [username@["주소"]]
- 주소의 "username"의 유저가 존재하면 삭제

```
<hr>

### DML : SIDU (SELECT / INSERT / DELETE / UPDATE)
1. SELECT 
    ``` sql
    SELECT [찾는 속성] FROM [테이블 명]
    - "테이블 명"의 테이블에서 "찾는 속성"의 속성을 찾음

    -------------------------------------------------


    ```

    ``` sql
    SELECT [찾는 속성] FROM [테이블 명] WHERE [조건]
    - "테이블 명"의 테이블에서 "조건"을 만족하는 "찾는 속성"의 속성을 찾음

    WHERE의 조건
    비교 : =, >, <, >=, <=              EX) price<20000
    범위 : BETWEEN                      EX) price BETWEEN 10000 AND 20000
    집합 : IN, NOT IN                   EX) price IN (100000, 20000, 30000)
    패턴 : LIKE                         EX) bookname LIKE '축구의 역사'
        - 와일드 문자
            - +     : 문자열을 연결                 EX) '골프'+'바이블'
            - %     : 0개 이상의 문자열과 일치       EX) '%축구%' : 축구를 포함하는 문자열
            - []    : 1개 문자와 일치               EX) '[0-5]%' : 0-5 사이의 숫자로 시작하는 문자열
            - [^]   : 1개의 문자와 불일치            EX) '[^0-5]%' : 0-5 사이의 숫자로 시작하지 않는 문자열
            - _     : 특정 위치의 1개의 문자와 일치   EX) '_구%' : 두번째 위치에 '구'가 들어가는 문자열
    'NULL' : IS NULL, IS NOT NULL       EX) price IS NULL
    복합조건 : AND, OR, NOT              EX) (price<20000) AND (bookname LIKE '축국의 역사')

    -----------------------------------------------------------------------------------------
    
    ```
    ``` sql
    SELECT [찾는 속성] FROM [테이블 명] ORDER BY [정렬 속성 | DESC / ASC, 정렬 속성2 | DESC / ASC ...]
    - "테이블 명"의 테이블에서 "찾는 속성"을 찾아 "정렬 속성"으로 정렬한다. 만약 "정렬 속성"의 값이 같은 경우 "정렬 속성2"로 정렬한다.
        - DESC : 내림차순
        - ASC  : 오름차순
    ```
    ``` sql
    SELECT [집계함수(속성)] FROM [테이블 명]
    - "테이블 명"의 테이블에서 "속성"에 해당하는 값을 "집계함수"로 연산
    
    집계 함수
    - SUM([ALL | DISTINCT] 속성이름)
    - AVG([ALL | DISTINCT] 속성이름)
    - COUNT([ALL | DISTINCT] 속성이름 | *)
    - MAX([ALL | DISTINCT] 속성이름)
    - MIN([ALL | DISTINCT] 속성이름)
    ```
    ``` sql
    SELECT [집계함수(속성)] FROM [테이블 명] GROUP BY [묶으려는 속성]
    - "테이블 명"의 테이블에서 "묶으려는 속성"의 값이 같은 속성들을 "집계함수"로 연산하여 묶는다.
    
    SELECT [집계함수(속성)] FROM [테이블 명] GROUP BY [묶으려는 속성] HAVING [그룹 조건]
    - "테이블 명"의 테이블에서 "묶으려는 속성"의 값이 같은 속성들을 "집계함수"로 연산하여 묶는데, 그룹 조건을 맞춘 것만 출력한다.
    ```
    ``` sql
    동등 조인 ('equi join')
    SELECT * FROM [테이블1], [테이블2][,테이블3 ...] WHERE [테이블1.ID] = [테이블2.ID]  
    # 이때의 ID는 서로 같은것을 칭하는 ID를 의미
    
    외부 조인('outer join')
    ```


### DCL : CRGR (COMMIT / ROLLBACK / GRANT / REVOKE)

# 시작할때 참고
``` sql
DROP DATABASE IF EXISTS madang;
DROP USER IF EXISTS  madang@localhost;
create user madang@localhost identified WITH mysql_native_password  by 'madang';
create database madang;
grant all privileges on madang.* to madang@localhost with grant option;
commit;

/* madang DB 자료 생성 */
USE madang;

CREATE TABLE ~~
```