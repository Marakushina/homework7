my_dict={"Мария":1990,"Катерина":1956,"Артём":1991}
print("Dict:",my_dict)
print("Existing value:",my_dict["Артём"])
print("Not existing value:",my_dict.get("Евгения"))
my_dict.update({"Анастасия":2001,"Иван":1978})
a=my_dict.pop("Мария")
print("Deleted value:",a)
print("Modified dictionary:",my_dict)

