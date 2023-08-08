-- USED_GOODS_BOARD와 USED_GOODS_REPLY
-- 테이블에서 2022년 10월에 작성된 게시글 제목, 게시글 ID, 댓글 ID, 댓글 작성자 ID, 댓글 내용, 댓글 작성일을 조회하는 SQL문을 작성해주세요.
-- 결과는 댓글 작성일을 기준으로 오름차순 정렬해주시고, 댓글 작성일이 같다면 게시글 제목을 기준으로 오름차순 정렬해주세요.


SELECT UGB.TITLE,
       UGB.BOARD_ID,
       UGR.REPLY_ID,
       UGR.WRITER_ID,
       UGR.CONTENTS,
       UGR.CREATED_DATE
FROM (SELECT *
      FROM USED_GOODS_BOARD
      WHERE CREATED_DATE BETWEEN '2022-10-01 00:00:00' AND '2022-10-21 23:59:59') as UGB
    INNER JOIN USED_GOODS_REPLY UGR ON UGB.BOARD_ID = UGR.BOARD_ID
    ORDER BY UGR.CREATED_DATE,TITLE  ASC