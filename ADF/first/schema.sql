drop table if exists Students;
create table Students (
  Student_id integer primary key autoincrement,
  First varchar,
  Last varchar
);

drop table if exists Classes;
create table Classes (
  Class_id integer primary key autoincrement,
  Name varchar,
  Credits integer
);

drop table if exists Schedule;
create table Schedule (
  Schedule_id integer primary key autoincrement,
  Students_id integer,
  Class_id integer
)
