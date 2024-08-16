my_dict={"Мария":1990,"Катерина":1956,"Артём":1991}
print("Dict:",my_dict)
print("Existing value:",my_dict["Артём"])
print("Not existing value:",my_dict.get("Евгения"))
my_dict.update({"Анастасия":2001,"Иван":1978})
a=my_dict.pop("Мария")
print("Deleted value:",a)
print("Modified dictionary:",my_dict)

my_set={"Artem",6,6,6,"Artem","Anna",True,True}
print("Set:",my_set)
my_set.update({"William",12,12,False,13})
my_set.discard(12)
print("Modified set:",my_set)
