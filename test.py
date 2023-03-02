from preprocess_data import Question

# 创建问题处理对象，这样模型就可以常驻内存
que=Question()

'''result=que.question_process("CPU的别名是啥？")
print(result)
result1=que.question_process("物理层作用是什么")
print(result1)
result2=que.question_process("处理机调度包含什么")
print(result2)
result3=que.question_process("线性表特点是什么")
print(result3)'''
result2=que.question_process("处理机调度包含什么")
print(result2)