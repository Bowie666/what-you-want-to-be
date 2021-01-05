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

-- 2.查询每门课程被选修的学生数
-- -- 思路-->先分组 在左关联
-- select 
--     t1.cou,
--     t2.Cname
-- from
--     (select count(Sid) cou, CId from sc group by CId) t1
-- left join
--     course t2
-- on
--     t1.CId=t2.CId


-- # -------------------- 偏难 ---------------
-- 1.查询没有学全所有课程的同学的信息
-- 思路-->按数量去找
-- select
--     student.SId,
--     ifnull(t1.cou, 0),
--     student.Sname,
--     student.Sage,
--     student.Ssex
-- from
--     (select SId, count(CId) cou from sc group by SId) t1 
-- right join
--     student 
-- on t1.SId = student.SId
-- where ifnull(cou, 0) < (select count(CId) from course)