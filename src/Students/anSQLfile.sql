
--As this SQL file should be reviewed by AI agent, it should properly identify below object name and its relevant folder names are equal or not.
--example if folder name is dothis, table should create table dothis ( ... )
--Change the folder name...
create table Employees (
    EmployeeID int primary key,
    FirstName varchar(50),
    LastName varchar(50),
    HireDate date
);