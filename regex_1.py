import re

dob_format = "^(19|20)[0-9]{2}/([1-9]|1[0-2])/([1-9]|1[0-9]|2[0-9]|3[0-1])$"

while True:
    dob = input("生年月日を入力してください  yyyy/mm//dd")
    result = re.search(dob_format, dob)

    if result:
        print(f"入力した生年月日:{dob}は正しい形式です")
        break
    else:
        print(f"入力した生年月日:{dob}は、正しくない形式です。再度入力してください yyyy/mm/dd")
        continue
