% Facts: Student, Teacher, and Subject Code relationships
teaches(mr_smith, math101).
teaches(ms_jones, cs102).
teaches(dr_adams, phy103).

student(john, math101).
student(alice, cs102).
student(bob, phy103).
student(eve, math101).

% Rule to find the teacher of a student based on subject code
student_teacher_code(Student, Teacher, SubCode) :-
    student(Student, SubCode),
    teaches(Teacher, SubCode).

% Query Example:
% ?- student_teacher_code(john, Teacher, SubCode).
% Expected Output:
% Teacher = mr_smith, SubCode = math101.