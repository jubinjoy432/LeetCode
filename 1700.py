#Number of Students Unable to Eat Lunch
class Solution(object):
    def countStudents(self, students, sandwiches):
        count=0
        while count<len(students) and students:
            if students[0]==sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                count=0
            else:
                students.append(students.pop(0))
                count+=1
        return len(students)