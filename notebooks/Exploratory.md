


shift_check = df.groupby(["WD EID", "Emp Name"])["Shift"].agg(
    shift_count = (lambda x: ", ".join(set(x))),
    count = ("nunique")
).reset_index()

shift_check

#Employees who have had to change their working schedule more than once
shift_check[shift_check["count"] != 1]

#Employees who can keep their work schedule stay still 
shift_check[shift_check["count"] == 1]