students = []
N =int(input())
for _ in range(N):
    name = input()
    score = float(input())
    students.append([name,score])
scores = set([students[x][1] for x in range(N)])
scores = list(scores)
scores.sort()
student = [students[x][0] for x in range(N) if students[x][1]==scores[1]]
student.sort()
for i in student:
    print(i)