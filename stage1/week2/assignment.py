print("===== Task 1 =====")


def find_and_print(messages):
    # write down your judgment rules in comments
    # 將關鍵字列出
    # 用for迴圈將訊息取出，並用空格將訊息拆分成字串
    # 在用if判斷式，將words中有keywords的人列出

    # your code here, based on your own rules
    keywords = ["18", "college", "legal", "vote"]
    for person, message in messages.items():
        words = message.split()
        for keyword in keywords:
            if keyword in words:
                print(person)


find_and_print(
    {
        "Bob": "My name is Bob. I'm 18 years old.",
        "Mary": "Hello, glad to meet you.",
        "Copper": "I'm a college student. Nice to meet you.",
        "Leslie": "I am of legal age in Taiwan.",
        "Vivian": "I will vote for Donald Trump next week",
        "Jenny": "Good morning.",
    }
)

print("===== Task 2 =====")


def calculate_sum_of_bonus(data):
    # write down your bonus rules in comments
    # bonus:以3000元為基準
    # 薪水:平均薪水低於50000元，則每人加2000
    # 表現:優良加2000，表現不優減2000
    # 職位:Engineer加1000，CEO加500，Sales加1000

    # your code here, based on your own rules
    # 先處理部分salary非數字以及單位不同的問題
    for employee in data["employees"]:
        if isinstance(employee["salary"], str):
            if employee["salary"].endswith("USD"):
                employee["salary"] = (int(employee["salary"][:-3])) * 30
            else:
                employee["salary"] = int(employee["salary"].replace(",", ""))

    # 計算bonus
    bonus = 3000
    average_salary = (sum(employee["salary"] for employee in data["employees"])) / len(
        data["employees"]
    )

    for employee in data["employees"]:
        salary = employee.get("salary", 0)
        performance = employee.get("performance", "")
        role = employee.get("role", "")

        if salary < average_salary:
            bonus += 2000

        if performance == "above average":
            bonus += 2000
        elif performance == "below average":
            bonus -= 2000

        if role == "Engineer":
            bonus += 1000
        elif role == "CEO":
            bonus += 500
        elif role == "Sales":
            bonus += 1000

    return print(bonus)


calculate_sum_of_bonus(
    {
        "employees": [
            {
                "name": "John",
                "salary": "1000USD",
                "performance": "above average",
                "role": "Engineer",
            },
            {"name": "Bob", "salary": 60000, "performance": "average", "role": "CEO"},
            {
                "name": "Jenny",
                "salary": "50,000",
                "performance": "below average",
                "role": "Sales",
            },
        ]
    }
)  # call calculate_sum_of_bonus function

print("===== Task 3 =====")


def func(*data):
    # your code here
    middle_names = []
    unique_names = []

    for name in data:
        middle = name[1]
        middle_names.append(middle)

    for name in data:
        unique = name[1]
        if middle_names.count(unique) == 1:
            unique_names.append(name)

    if len(unique_names) == 0:
        return print("沒有")
    else:
        return print(" ".join(unique_names))


func("彭大牆", "王明雅", "吳明")  # print 彭大牆
func("郭靜雅", "王立強", "林靜宜", "郭立恆", "林花花")  # print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花")  # print 沒有


print("===== Task 4 =====")


def get_number(index):
    # your code here
    sequence = [0]

    for i in range(1, index + 1):
        if i % 2 == 1:
            sequence.append(sequence[i - 1] + 4)
        else:
            sequence.append(sequence[i - 1] - 1)

    return print(sequence[index])


get_number(1)  # print 4
get_number(5)  # print 10
get_number(10)  # print 15
