from django.shortcuts import render
from django.db.models import Count
from django.core.exceptions import ObjectDoesNotExist
from .models import Student, Instructor, Course, StudentCourse
from .const_data import view_information


# <><><><><><><><><><><><><><><><><><><><><><><><><><><><>


# Find all students and print their first_name, last_name, and GPA to the terminal
# Example solution:
def example_solution(request):

    students = Student.objects.all()
    # instructors = Instructor.objects.all()

    for student in students:
        print(f'First Name: {student.first_name} Last Name: {student.last_name} GPA: {student.gpa}')


    return complete(request)


# Supporting Query Method Documentation:
"""
https://docs.djangoproject.com/en/4.0/ref/models/querysets/#all
"""

# Expected Terminal Response:
"""
First Name: Jake Last Name: Sisko GPA: 4.0
First Name: Keira Last Name: Nerys GPA: 3.5
First Name: Julian Last Name: Bashir GPA: 4.4
First Name: Molly Last Name: OBrien GPA: 3.0
First Name: Keiko Last Name: Ishikawa GPA: 4.2
First Name: Eli Last Name: Garak GPA: 3.0
First Name: Thomas Last Name: Riker GPA: 2.5
First Name: Michael Last Name: Eddington GPA: 3.7
First Name: Beckett Last Name: Mariner GPA: 3.8
First Name: Sam Last Name: Rutherford GPA: 2.0
"""

# Expected Resulting SQL Query (Found in "SQL" section of the debug toolbar in browser):
"""
SELECT `school_db_student`.`id`,
       `school_db_student`.`first_name`,
       `school_db_student`.`last_name`,
       `school_db_student`.`year`,
       `school_db_student`.`gpa`
  FROM `school_db_student`
"""


# <><><><><><><><><><><><><><><><><><><><><><><><><><><><>


# P1) Find all students who have a GPA greater than 3.0. 
# Order the data by highest GPAs first (descending).
# Print out each student's full name and gpa to the terminal
def problem_one(request):

    # print("hello everyone")
    # students = Student.objects.all()
    students_with_gpa_greater_than_3 = Student.objects.filter(gpa__gt= 3.0).order_by('-gpa')  # “greater than” = filter(gpa__gt= 3.0)
    
    for student_with_gpa_greater_than_3 in students_with_gpa_greater_than_3 : 
      print(f"{student_with_gpa_greater_than_3.first_name} {student_with_gpa_greater_than_3.last_name} {student_with_gpa_greater_than_3.gpa}")


    return complete(request)


# Supporting Query Method Documentation:
"""
https://docs.djangoproject.com/en/4.0/ref/models/querysets/#filter
https://docs.djangoproject.com/en/4.0/ref/models/querysets/#order-by

Semi's notes : 
https://pythonguides.com/python-django-filter/


"""

# Expected Terminal Response:
"""
Full Name: Julian Bashir GPA: 4.4
Full Name: Keiko Ishikawa GPA: 4.2
Full Name: Jake Sisko GPA: 4.0
Full Name: Beckett Mariner GPA: 3.8
Full Name: Michael Eddington GPA: 3.7
Full Name: Keira Nerys GPA: 3.5
"""

# Expected Resulting SQL Query (Found in "SQL" section of the debug toolbar in browser):
"""
SELECT `school_db_student`.`id`,
       `school_db_student`.`first_name`,
       `school_db_student`.`last_name`,
       `school_db_student`.`year`,
       `school_db_student`.`gpa`
  FROM `school_db_student`
 WHERE `school_db_student`.`gpa` > 3.0
 ORDER BY `school_db_student`.`gpa` DESC
"""

# <><><><><><><><><><><><><><><><><><><><><><><><><><><><>


# P2) Find all instructors hired prior to 2010
# Order by hire date ascending
# Print out the instructor's full name and hire date to the terminal
def problem_two(request):

    # instructors = Instructor.objects.all()
    instructors_hired_prior_2010 = Instructor.objects.filter(hire_date__year__lt = 2010-1-1).order_by("hire_date")   # “less than” = filter(hire_date__lt=2010)

    for instructor_hired_prior_2010 in instructors_hired_prior_2010 : 
      print(f"{instructor_hired_prior_2010.first_name} {instructor_hired_prior_2010.last_name} {instructor_hired_prior_2010.hire_date}")


    return complete(request)


# Supporting Query Method Documentation:
"""
https://docs.djangoproject.com/en/4.0/ref/models/querysets/#filter
https://docs.djangoproject.com/en/4.0/ref/models/querysets/#year
https://docs.djangoproject.com/en/4.0/ref/models/querysets/#lt
"""

# Expected Terminal Response: (format print challenge!)
"""
Full Name: Colin Robinson
Hire Date: 2009-04-10

Full Name: Guillermo de la Cruz
Hire Date: 2009-11-18
"""

# Expected Resulting SQL Query (Found in "SQL" section of the debug toolbar in browser):
"""
SELECT `school_db_instructor`.`id`,
       `school_db_instructor`.`first_name`,
       `school_db_instructor`.`last_name`,
       `school_db_instructor`.`hire_date`
  FROM `school_db_instructor`
 WHERE `school_db_instructor`.`hire_date` < '2010-01-01'
"""


# <><><><><><><><><><><><><><><><><><><><><><><><><><><><>


# P3 ) Find all courses that belong to the instructor that has the primary key of 2
# Print the instructors name and courses that he belongs to in the terminal 
# (Do not hard code his name in the print)
def problem_three(request):

  instructor_holding_PK2 = Instructor.objects.get(id = 2)
  courses_for_PK2 = Course.objects.filter(instructor_id = 2)

  print(f"Instructor Name : {instructor_holding_PK2.first_name} {instructor_holding_PK2.last_name}\nCourses:")
  
  for course in courses_for_PK2 :
    print(f"\t- {course.name}")

  return complete(request)
# remember : James's updated print instruction

# Supporting Query Method Documentation:
"""
https://docs.djangoproject.com/en/4.0/ref/models/querysets/#get
https://docs.djangoproject.com/en/4.0/ref/models/querysets/#filter

Semi's notes : 
https://pythonguides.com/python-django-filter/
https://pythonguides.com/python-django-get/

The Difference between Django's filter() and get() methods are: get throws an error if there's no object matching the query. 
filter will return an empty queryset… Basically use get() when you want to get a single unique object, and filter() when you 
want to get all objects that match your lookup parameters
"""

# Expected Terminal Response: (format print challenge!)
"""
Instructor Name: Colin Robinson
Courses:
    - Science
    - History
"""

# Expected Resulting SQL Query (Found in "SQL" section of the debug toolbar in browser):
"""
# First Query:

SELECT `school_db_instructor`.`id`,
       `school_db_instructor`.`first_name`,
       `school_db_instructor`.`last_name`,
       `school_db_instructor`.`hire_date`
  FROM `school_db_instructor`
 WHERE `school_db_instructor`.`id` = 2
 LIMIT 21

# Second Query:

 SELECT `school_db_course`.`id`,
       `school_db_course`.`name`,
       `school_db_course`.`instructor_id`,
       `school_db_course`.`credits`
  FROM `school_db_course`
 WHERE `school_db_course`.`instructor_id` = 2
"""


# <><><><><><><><><><><><><><><><><><><><><><><><><><><><>


# P4) Get the count of students, courses, and instructors and print them in the terminal
def problem_four(request):

  students_count = Student.objects.count()
  courses_count = Course.objects.count()
  instructors_count = Instructor.objects.count()

  print(f" Student Counts = {students_count}")
  print(f" Courses Counts = {courses_count}")
  print(f" Instructor Counts = {instructors_count}")


  return complete(request)


# Supporting Query Method Documentation:
"""
https://docs.djangoproject.com/en/4.0/ref/models/querysets/#count
"""

# Expected Terminal Response:
"""
Students Count: 10
Courses Count: 10
Instructors Count: 6
"""

# Expected Resulting SQL Query (Found in "SQL" section of the debug toolbar in browser):
"""
# First Query:

SELECT COUNT(*) AS `__count`
  FROM `school_db_student`

# Second Query:

SELECT COUNT(*) AS `__count`
  FROM `school_db_course`

# Third Query:

SELECT COUNT(*) AS `__count`
  FROM `school_db_instructor`
"""


# <><><><><><><><><><><><><><><><><><><><><><><><><><><><>
# CRUD Operations (Create, Read, Update, Delete)
# <><><><><><><><><><><><><><><><><><><><><><><><><><><><>


# P5) Create a new student in the database. Use your information!
# Print the new student's id, full name, year, and gpa to the terminal
# NOTE every time you execute this function a duplicate student will be created with a different primary key number
def problem_five(request):

  new_student = Student.objects.create(first_name="Christine", last_name="Tehrani", year = 2022, gpa = "4.00")
  print(f"ID = 11 ")
  print(f"Full Name : {new_student.first_name} {new_student.last_name}")
  print(f"Year = {new_student.year}")
  print(f"GPA = {new_student.gpa}")

  return complete(request)


# Supporting Query Method Documentation:
"""
https://docs.djangoproject.com/en/4.0/ref/models/querysets/#create
"""

# Expected Terminal Response:
"""
Id: 11
Full Name: Kyle Harwood
Year: 2022
GPA: 3.0
"""

# Expected Resulting SQL Query (Found in "SQL" section of the debug toolbar in browser):
"""
INSERT INTO `school_db_student` (`first_name`, `last_name`, `year`, `gpa`)
# NOTE: The information in the values will be what you chose
VALUES ('Kyle', 'Harwood', 2022, 3.0)
"""


# <><><><><><><><><><><><><><><><><><><><><><><><><><><><>


# P6) Query the previoiusly created student by the id and update the "gpa" to a new value
# Then query the studets table to get that student by their id
# Print the new student's id, full name, and gpa to the terminal
def problem_six(request):
    
    # Make sure to set this equal to the primary key of the row you just created!
  student_id = 11
  # new_student = Student.objects.get(id = 11)
  new_student_updated_gpa_Pk11 = Student.objects.filter(id = 11).update(gpa = 3)
  new_update = Student.objects.get(id = 11)

  # print(f'First Name: {new_update.first_name} Last Name: {new_update.last_name} GPA: {new_update.gpa}')  
  print(f"ID = 11 ")
  print(f"Full Name : {new_update.first_name} {new_update.last_name}")
  print(f"GPA = {new_update.gpa}")

  return complete(request)


# Supporting Query Method Documentation:
"""
https://docs.djangoproject.com/en/4.0/ref/models/querysets/#update

Semi's note : ORM Query Methods Definitions & examples document is much better.


"""

# Expected Terminal Response:
"""
Id: 11
Full Name: Kyle Harwood
GPA: 3.5
"""

# Expected Resulting SQL Query (Found in "SQL" section of the debug toolbar in browser):
"""
# Query One:

UPDATE `school_db_student`
# NOTE: The gpa value will be what you chose
   SET `gpa` = 3.5
 WHERE `school_db_student`.`id` = 11

# Query Two:

SELECT `school_db_student`.`id`,
    `school_db_student`.`first_name`,
    `school_db_student`.`last_name`,
    `school_db_student`.`year`,
    `school_db_student`.`gpa`
FROM `school_db_student`
WHERE `school_db_student`.`id` = 11
LIMIT 21
"""


# <><><><><><><><><><><><><><><><><><><><><><><><><><><><>


# 7) Delete the student that you have created and updated
# Check your MySQL Workbench to confirm the student is no longer in the table!
def problem_seven(request):

    # Make sure to set this equal to the primary key of the row you just created!
    student_id = 11

    deleted_new_student_Pk11 = Student.objects.filter(id = 11).delete()
    
    # print(f"Full Name : {deleted_new_student_Pk11.first_name} {deleted_new_student_Pk11.last_name}")
    

    try:
        student = Student.objects.get(pk=student_id)
    except ObjectDoesNotExist:
        print('Great! It failed and couldnt find the object because we deleted it!')

    return complete(request)


# Supporting Query Method Documentation:
"""
https://docs.djangoproject.com/en/4.0/ref/models/querysets/#delete
"""

# Expected Terminal Response:
"""
Great! It failed and couldnt find the object because we deleted it!
"""

# Expected Resulting SQL Query (Found in "SQL" section of the debug toolbar in browser):
"""
# Query One:

SELECT `school_db_student`.`id`,
       `school_db_student`.`first_name`,
       `school_db_student`.`last_name`,
       `school_db_student`.`year`,
       `school_db_student`.`gpa`
  FROM `school_db_student`
 WHERE `school_db_student`.`id` = 15

 # Query Two:

 DELETE
  FROM `school_db_studentcourse`
 WHERE `school_db_studentcourse`.`student_id` IN (15)

 # Query Three: - NOTE this query is included in the starter code. See the query in the try catch

SELECT `school_db_student`.`id`,
       `school_db_student`.`first_name`,
       `school_db_student`.`last_name`,
       `school_db_student`.`year`,
       `school_db_student`.`gpa`
  FROM `school_db_student`
 WHERE `school_db_student`.`id` = 15
 LIMIT 21
"""


# <><><><><><><><><><><><><><><><><><><><><><><><><><><><>


# Bonus Problem ) Find all of the instructors that only belong to a single course
# Print out the instructors full name and number of courses to the console
def bonus_problem(request):

  instructors_teaching_courses = Course.objects.count(Course.instructor_id)
  print (instructors_teaching_courses)



  return complete(request)


# Supporting Query Method Documentation:
"""
https://docs.djangoproject.com/en/4.0/topics/db/aggregation/
https://docs.djangoproject.com/en/4.0/ref/models/querysets/#annotate
https://docs.djangoproject.com/en/4.0/ref/models/querysets/#filter
https://docs.djangoproject.com/en/4.0/ref/models/querysets/#count
"""

# Expected Terminal Response:
"""
Instructor Name: Guillermo de la Cruz
Instructor Name: Brad Baskshi
"""

# Expected Resulting SQL Query (Found in "SQL" section of the debug toolbar in browser):
"""
SELECT `school_db_instructor`.`id`,
       `school_db_instructor`.`first_name`,
       `school_db_instructor`.`last_name`,
       `school_db_instructor`.`hire_date`,
       COUNT(`school_db_course`.`id`) AS `course__count`
  FROM `school_db_instructor`
  LEFT OUTER JOIN `school_db_course`
    ON (`school_db_instructor`.`id` = `school_db_course`.`instructor_id`)
 GROUP BY `school_db_instructor`.`id`
HAVING COUNT(`school_db_course`.`id`) = 1
 ORDER BY NULL
"""


# <><><><><><><><><><><><><><><><><><><><><><><><><><><><>


# Dont worry about this! You will learn about this in the next class day!
def complete(req):
    context = view_information[req.path]
    return render(req, 'school/index.html', context)