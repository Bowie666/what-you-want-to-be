-- # -------------------- 简单 ---------------
-- 1.查询「李」姓老师的数量
-- select count(Tname) d from teacher where Tname like '李%'
-- 2.查询男生、女生人数
-- select count(Ssex), Ssex from student group by Ssex;
-- 3.查询名字中含有「风」字的学生信息
-- select * from student where Sname like '%风%'


-- # -------------------- 中等 ---------------
-- 1.查询学过「张三」老师授课的同学的信息---------待优化
-- (1)先找张三老师的课程id
-- select Tid from teacher where Tname="张三"
-- (2)拿着tid去找教的课程
-- select Cid from course where Tid=(select Tid from teacher where Tname="张三")
-- (3)拿着cid去找课程
-- select * from sc where Cid=(select Cid from course where Tid=(select Tid from teacher where Tname="张三"))
-- (4)拿着cid去找sid
-- select * from student where Sid in (select Sid from sc where Cid=(select Cid from course where Tid=(select Tid from teacher where Tname="张三")))
-- (5)优化