import Course as course
import Assignment as assign

def AssignmentSort(lst_assignments, lst_percents, lst_deadline, student_major):
    # setting up the assignments in a list
    course_data = [[lst_assignments[i].split(" ")] for i in range(len(lst_assignments))]
    courses = {}
    assignments = []
    for i in range(len(course_data)):
        course_name = str(course_data[i][0]) + str(course_data[i][1])
        deadline_date_time = lst_deadline.split(" ")
        deadline_date = deadline_date_time[0]
        deadline_time = deadline_date_time[1]
        if str(course_data[i][0]) + str(course_data[i][1]) not in courses:
            courses[course_name] = 1
        else:
            courses[course_name] += 1
        assignments += [assign.__init__(course_name, lst_percents[i], deadline_date, deadline_date_time)]

    # sorting them based on time and priority
    sorted_assignments = mergeSort(assignments, 0, len(assignments) - 1)
    return sorted_assignments
    

# using mergeSort to sort the assignments
def mergeSort(A, start, end):
    n = end - start + 1
    if (n > 2):
        mid = start + n//2
        mergeSort(A, start, mid)
        mergeSort(A, mid, end)
        merge(A, start, mid, end, n)


# using merge to merge the separate assignments based 
# on priority and deadline
def merge(A, start, mid, end, n):
    i = start
    j = mid + 1
    k = 0
    sorted_part = []
    while (i <= mid and j <= end):
        assign_i = A[i].getDeadline()
        assign_j = A[j].getDeadline()
        if (assign_i.isLater(assign_j) or A[i].getPriority() <  A[j].getPriority()):
            sorted_part[k] = A[j]
            k += 1
            j += 1
        else:
            sorted_part[k] = A[i]
            i += 1
            k += 1
    
    while (i <= mid):
        sorted_part[k] = A[i]
        i += 1
        k += 1
    
    while (j <= end):
        sorted_part[k] = A[j]
        j += 1
        k += 1

    for i in range(len(sorted_part)):
        A[start + i] = sorted_part[i]



    
        
    
