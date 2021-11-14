
# importing time and course class
import Time as time
import Course as course

# Assignment class stores the course class,
# The deadline and ratio of the course grade

class Assignment():

    # initializing an Assignment object:
    # inputs: percent_of_grade (ratio of grade for course)
    #           deadline_date (string input dd/mm/yyyy or dd/mmm/yyyy)
    #           deadline_time (string input hh:mm)
    def __init__(self, assignment_name, course, percent_of_grade, deadline_date, deadline_time):
        self.course = course.__init__(course)
        self.setName(assignment_name)
        self.setDeadline(time)
        self.setGradePercent(percent_of_grade)
        self.finished = False

    # returns the assignment name
    def getName(self):
        return self.course.toString() + self.name

    # returns the courses priority
    def getPriority(self):
        return self.course.getPriority()

    # returns the deadline of the assignments
    def getDeadline(self):
        return self.deadline

    # setter function to set the name of the assignment
    def setName(self, assignment_name):
        self.name = assignment_name
        
    # setter function to set the date of the assginment deadline
    def setDeadline(self, deadline_date, deadline_time):
        self.deadline = time.__init__(deadline_date, deadline_time)

    # setter function to set the percent of the course grade this
    # assignment is worth
    def setGradePercent(self, percent_of_grade):
        if (percent_of_grade > 0 and percent_of_grade <= 100):
            self.gradePercent = percent_of_grade
            return True
        return False

    # setter function to set the assignment to finished
    def setToFinished(self):
        self.finished = True

    # getter function to get the grade percent of assignment
    # relative to the course
    def getGradePercent(self):
        return self.gradePercent

    # returns a bool value on whether assignment is finished.
    def isFinished(self):
        return self.finished
