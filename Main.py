import random
import itertools as it
import statistics as st
import math
gender = ["W","M","M","W","M","M","W","M","M","W","M","W","M","W",
          "M","M","M","W","M","M","M","W","W","W","M","M","W","M",
          "M","W","M","M","W","W","M","M","W","M","M","M","W","W",
          "W","W","M","M","W","M","M","M","W","W","W","M","M","M",
          "W","W","W","M","M","M","W","W","M"]
salary = [27,61,52,69,88,85,79,99,77,165,41,83,144,74,143,131,34,
          59,46,105,61,118,114,138,24,67,130,56,99,125,87,30,119,
          40,25,44,123,45,25,94,86,128,69,102,91,106,119,139,67,
          47,62,92,124,31,49,68,109,138,105,84,86,66,128,146,59]

# cau 1
mean= st.mean(salary)
stdev= st.pstdev(salary)
print(mean, stdev)
# print(st.stdev(salary))
# cau 2
# female=[salary[i] for i in range(len(salary)) if gender[i] == 'W']
# female=sorted(female)
# print(female)
# print(len(female))
# count=0
# for i in female:
#     if i > mean:
#         count+=1
# print(count)
# cau 3
# male=[salary[i] for i in range(len(salary)) if gender[i] == 'M']
# male=sorted(male)
# print(male)
# print(len(male))
# count=0
# for i in male:
#     if i > mean:
#         count+=1
# print(count)
# cau 5
# exam_30=math.comb(65,30)
# print(exam_30)
# exam_15=math.comb(65,15)
# print(exam_15)
# cau 6
# print("Mẫu 30:")
# exam_30_stt = [random.randint(0, len(gender) - 1) for i in range(30)]
# exam_30_gender=[gender[i] for i in exam_30_stt]
# exam_30_salary=[salary[i] for i in exam_30_stt]
exam_30_stt=[44, 38, 12, 25, 33, 25, 10, 35, 57, 51, 57, 22, 26, 35, 61, 44, 17, 63, 36, 32, 45, 60, 6, 61, 52, 46, 53, 46, 9, 4]
exam_30_gender=['M', 'M', 'M', 'M', 'W', 'M', 'M', 'M', 'W', 'W', 'W', 'W', 'W', 'M', 'M', 'M', 'W', 'W', 'W', 'W', 'M', 'M', 'W', 'M', 'W', 'W', 'M', 'W', 'W', 'M']
exam_30_salary=[91, 25, 144, 67, 40, 67, 41, 44, 138, 92, 138, 114, 130, 44, 66, 91, 59, 146, 123, 119, 106, 86, 79, 66, 124, 119, 31, 119, 165, 88]    
# print(exam_30_stt)
# print(exam_30_gender)
# print(exam_30_salary)
# print("Mẫu 15:")
# exam_15_stt = [random.randint(0, len(gender) - 1) for i in range(15)]
# exam_15_gender=[gender[i] for i in exam_15_stt]
# exam_15_salary=[salary[i] for i in exam_15_stt]
exam_15_stt=[24, 56, 45, 63, 53, 10, 48, 50, 19, 48, 45, 49, 20, 29, 0]
exam_15_gender=['M', 'W', 'M', 'W', 'M', 'M', 'M', 'W', 'M', 'M', 'M', 'M', 'M', 'W', 'W']
exam_15_salary=[24, 109, 106, 146, 31, 41, 67, 62, 105, 67, 106, 47, 61, 125, 27]
# print(exam_15_stt)
# print(exam_15_gender)
# print(exam_15_salary)
# cau 7
mean_exam_30=st.mean(exam_30_salary)
stdev_exam_30=st.stdev(exam_30_salary)
mean_exam_15=st.mean(exam_15_salary)
stdev_exam_15=st.stdev(exam_15_salary)
# print(mean_exam_30,stdev_exam_30)
# print(mean_exam_15,stdev_exam_15)