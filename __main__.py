import pygsheets
import json
import ezd

with open("data.json", "r") as read_dile:
    data = json.load(read_dile)
driver = ezd.init_driver()
ezd.auth(driver, data["ezd_login"], data["ezd_password"])
gc = pygsheets.authorize(service_file="client_secret.json")


# Open spreadsheet and then worksheet
sh = gc.open_by_url(data["google_sheet_url"])
wks = sh.sheet1
group = 'start'
strr = 2
while wks[strr][5] != '':
    group = wks[strr][5]
    name = wks[strr][4]
    mark = wks[strr][2]
    id_ezd_col = str("G" + str(strr))
    if(wks[strr][6] == ''):
        if ezd.put(data["group_url"][ezd.group_to_eng(group)], name, mark, group, driver, data["date_id"][ezd.group_to_eng(group)]):
            wks.update_value(id_ezd_col, "да")
        else:
            wks.update_value(id_ezd_col, "нет")

    strr += 1
ezd.successs()

driver.close()


