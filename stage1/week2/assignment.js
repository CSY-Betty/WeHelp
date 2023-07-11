console.log("===== Task 1 =====")

function findAndPrint(messages){
    // write down your judgment rules in comments
    // 將關鍵字列出
    // 用for迴圈將訊息取出，並用空格將訊息拆分成字串
    // 在用if判斷式，將words中有keywords的人列出

    // your code here, based on your own rules
    let keywords = ["18", "college", "legal", "vote"];
    for (let person in messages){
        let message = messages[person];
        let words = message.split(" ");
        for (i = 0; i<words.length; i++){
            let word = words[i]
            if (keywords.includes(word)){
                console.log(person);
            }
        }
    }
}


findAndPrint({
    "Bob":"My name is Bob. I'm 18 years old.", 
    "Mary":"Hello, glad to meet you.",
    "Copper":"I'm a college student. Nice to meet you.", 
    "Leslie":"I am of legal age in Taiwan.",
    "Vivian":"I will vote for Donald Trump next week",
    "Jenny":"Good morning." 
});

console.log("===== Task 2 =====")

function calculateSumOfBonus(data) {
    // write down your bonus rules in comments
    // bonus:以3000元為基準
    // 薪水:平均薪水低於50000元，則每人加2000
    // 表現:優良加2000，表現不優減2000
    // 職位:Engineer加1000，CEO加500，Sales加1000

    // your code here, based on your own rules
    // 先處理部分salary非數字以及單位不同的問題
    for (i = 0; i < data.employees.length; i++) {
        let employee = data.employees[i];
        if (typeof employee.salary === "string") {
            if (employee.salary.endsWith("USD")) {
                employee.salary = parseInt(employee.salary.slice(0, -3)) * 30;
            } else {
                employee.salary = parseInt(employee.salary.replace(",", ""));
            }
        }
        data.employees[i].salary = employee.salary; 
    };


    // 計算bonus
    let bonus = 3000;
    let totalSalary = 0;
    for (let i = 0; i < data.employees.length; i++) {
        let employee = data.employees[i];
        totalSalary += employee.salary;
    }
    let averageSalary = totalSalary / data.employees.length;

    for (let i = 0; i < data.employees.length; i++) {
        let employee = data.employees[i];
        let salary = employee.salary;
        let performance = employee.performance;
        let role = employee.role;

        if (salary < averageSalary) {
            bonus += 2000;
        }

        if (performance == "above average") {
            bonus += 2000;
        } else if (performance == "below average") {
            bonus -= 2000;
        }

        if (role == "Engineer") {
            bonus += 1000;
        } else if (role == "CEO") {
            bonus += 500;
        } else if (role == "Sales") {
            bonus += 1000;
        }
    }

    console.log(bonus);
}

calculateSumOfBonus({
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
});


console.log("===== Task 3 =====")

function func(...data) {
    // your code here
    let middle_names = [];
    let unique_names = [];

    for (i = 0; i < data.length; i++) {
        let name = data[i];
        let middle = name[1];
        middle_names.push(middle);
    }

    for (i = 0; i < data.length; i++) {
        let name = data[i];
        let unique = name[1];
        if (middle_names.filter((n) => n === unique).length === 1) {
            unique_names.push(name);
        }
    }

    if (unique_names.length === 0) {
        console.log("沒有");
    } else {
        console.log(unique_names.join(" "));
    }
}

func("彭大牆", "王明雅", "吳明"); // print 彭大牆
func("郭靜雅", "王立強", "林靜宜", "郭立恆", "林花花"); // print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花"); // print 沒有


console.log("===== Task 4 =====")

function getNumber(index) {
    // your code here
    let sequence = [0];

    for (i = 1; i <= index; i++) {
        if (i % 2 === 1) {
            sequence.push(sequence[i - 1] + 4);
        } else {
            sequence.push(sequence[i - 1] - 1);
        }
    }

    console.log(sequence[index]);
}

getNumber(1); // print 4
getNumber(5); // print 10
getNumber(10); // print 15
