if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    for key in student_marks:
        if key==query_name:
            le=len(student_marks[key])
            su=sum(student_marks[key])
    print("{0:.2f}".format(su/le))
