
# Course is a class that sets up
# a course number, college code 
# for a course and its priority which
# adjusts if it is a major course
#
class Course():

    # Initializing all main variables College, course, course number
    # and priority
    def __init__(self, college, course, courseNumber, priority, student_major):
        self.setCollege(college)
        self.setCourse(course)
        self.setCourseNumber(courseNumber)
        self.setPriority(priority, course, student_major)

    # setPriority sets the priority of a course based on the student's
    # evaluation and adjusts if it is a major course to take more priority
    def setPriority(self, priority, course, student_major):
        if (priority >= 1):
            self.priority = priority
            
        if (course == student_major):
            self.isMajorCourse = True
            self.priority = self.priority * 2
        
    # setter function to set the course
    # e.g. CS
    def setCourse(self, course):
        self.course = course
    
    # setter function to set the college
    # e.g. CAS
    def setCollege(self, college):
        self.college = college

    # setter function to set the course number
    # e.g. 111
    def setCourseNumber(self, courseNumber):
        self.courseNumber = int(courseNumber)

    # getter function to return the college code
    def getCollege(self):
        return self.college

    # getter function to return the course
    def getCourse(self):
        return self.course

    def getCourseNum(self):
        return self.courseNumber

    # getter function to return the priority of the course
    def getPriority(self):
        return self.priority
    
    # a toString that returns the complete course name + college.
    def toString(self):
        return self.getCollege() + self.getCourse() + self.courseNumber