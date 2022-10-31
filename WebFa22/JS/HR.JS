var JSON = {
    "company": [
        {
        "company Name":"Tech Stars",/*problem 2*/
        "Website": "www.techstars.site",
        "Employees": [
            {
                "first name": "Sam",/*problem 1*/
                "Department": "Tech",
                "Designation": "Manager",
                "salary":40000,
                "raise Eligible":true
              },
              {
                "first name": "Mary",
                "Department": "finance",
                "Designation": "Trainee",
                "salary":18500,
                "raise Eligible":true,
              },
              {
                "first name": "Bill",
                "Department": "HR",
                "Designation": "Executive",
                "salary":21200,
                "raise Eligible":true,
              }, 
              {
                "First Name":"Anna",
                "Department":"Tech",
                "Designation":"Executive",
                "salary":256000,
                "raise Eligible":false
              }
            ]
        }
    ]
};

/* problem 4*/
let total = 0;
    for (let i = 0; i<4; i++){
        total += JSON.company[0].Employees[i].salary
        }
console.log(total);
    
    let OldSalary = JSON.company[0].Employees[i].salary;
    let NewSalary = (OldSalary + 0.1*OldSalary);
    console.log(    )
    JSON.company[0].Employees[] = NewSalary