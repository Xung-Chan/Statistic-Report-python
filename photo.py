import random

gender = ["W","M","M","W","M","M","W","M","M","W","M","W","M","W",
          "M","M","M","W","M","M","M","W","W","W","M","M","W","M",
          "M","W","M","M","W","W","M","M","W","M","M","M","W","W",
          "W","W","M","M","W","M","M","M","W","W","W","M","M","M",
          "W","W","W","M","M","M","W","W","M"]
salary = [27,61,52,69,88,85,79,99,77,165,41,83,144,74,143,131,34,
          59,46,105,61,118,114,138,24,67,130,56,99,125,87,30,119,
          40,25,44,123,45,25,94,86,128,69,102,91,106,119,139,67,
          47,62,92,124,31,49,68,109,138,105,84,86,66,128,146,59]

print("Mẫu 30:")
exam_30_stt = [random.randint(0, len(gender) - 1) for i in range(30)]
exam_30_gender=[gender[i] for i in exam_30_stt]
exam_30_salary=[salary[i] for i in exam_30_stt]
print(exam_30_stt)
print(exam_30_gender)
print(exam_30_salary)
print("Mẫu 15:")
exam_15_stt = [random.randint(0, len(gender) - 1) for i in range(15)]
exam_15_gender=[gender[i] for i in exam_15_stt]
exam_15_salary=[salary[i] for i in exam_15_stt]
print(exam_15_stt)
print(exam_15_gender)
print(exam_15_salary)