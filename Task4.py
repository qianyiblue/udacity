"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
任务4:
电话公司希望辨认出可能正在用于进行电话推销的电话号码。
找出所有可能的电话推销员:
这样的电话总是向其他人拨出电话，
但从来不发短信、接收短信或是收到来电


请输出如下内容
"These numbers could be telemarketers: "
<list of numbers>
电话号码不能重复，每行打印一条，按字典顺序排序后输出。
"""

texts_incoming_num, texts_answering_num, texts_timestamp = zip(*texts)
calls_incoming_num, calls_answering_num, calls_timestamp, calls_duration = zip(*calls)
texts_incoming_num_set = set(texts_incoming_num)
texts_answering_num_set = set(texts_answering_num)
calls_incoming_num_set = set(calls_incoming_num)
calls_answering_num_set = set(calls_answering_num)
sales_num = calls_incoming_num_set.difference(calls_answering_num_set, texts_incoming_num_set, texts_answering_num_set)
print("These numbers could be telemarketers: \n{}".format("\n".join(sorted(sales_num))))
