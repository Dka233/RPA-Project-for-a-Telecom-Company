# To Read CSV files
import csv
# To do the automatization process
import rpa as r

# The main function to create the property in the system
def gestionar_uuii(uuii, codigoPostal, cto):
    r.url(uuii)
    r.timeout(120)
    if r.read('//*[@id="btnNew"]'):
        r.click('//*[@id="btnNew"]')
        r.timeout(120)
        if r.read('//*[@id="btnFormEditSave"]'):
            r.select('//*[@name="planta"]', 'BA')
            r.type('//*[@name="cp"]', codigoPostal)
            r.click('//*[@id="btnFormEditSave"]')
            if r.read('//*[@class="tableCell"]'):
                r.click('//*[@class="tableCell"]')
                r.click('//*[@id="btnRD"]')
                if r.read('//*[@id="btnFormRDSave"]'):
                    r.timeout(120)
                    r.select('//*[@name="rd"]', cto)
                    r.wait(5)
                    if r.read('//*[@id="ctoAddress_ctoName"]'):
                        r.click('//*[@id="btnFormRDSave"]')
                        if r.url('xxxx.do?dispatchMethod=rdSave'):
                            print('Gestionada')



# Start the program
r.init()
# Open the website
r.url('http://xxxxxt/login.jsp')
# Log in if you are not log in
if r.url() == 'http://fxxxxxx/login.jsp':
    user = input("Introduce el usuario de FDTT: ")
    password = input("Introduce el password: ")
    r.type('//*[@name="user"]', user)
    r.type('//*[@name="password"]', password + '[enter]')
    # path to the file with the information
    file = input("Introduce la ruta del archivo de fincas: ")
    # iteration of rows in file
    with open(file, 'rt') as f:
        data = csv.reader(f)
        for row in data:
            ui = row[0]
            cp = row[1]
            cto = row[2]
            # main function
            gestionar_uuii(ui, cp, cto)
# If the website log out you during the process
elif r.url() == 'http://xxxxorType=logoff':
    user = input("Introduce el usuario de FDTT: ")
    password = input("Introduce el password: ")
    r.type('//*[@name="user"]', user)
    r.type('//*[@name="password"]', password + '[enter]')
    # path to the file with the information
    file = input("Introduce la ruta del archivo de fincas: ")
    # iteration of rows in file
    with open('ui.csv', 'rt') as f:
        data = csv.reader(f)
        for row in data:
            ui = row[0]
            cp = row[1]
            cto = row[2]
            # main function
            gestionar_uuii(ui, cp, cto)
# If you are already log in
elif r.url() == 'http://xxxxxxxtt/index.jsp':
    file = input("Introduce la ruta del archivo de fincas: ")
    with open(file, 'rt') as f:
        data = csv.reader(f)
        for row in data:
            ui = row[0]
            cp = row[1]
            cto = row[2]
            gestionar_uuii(ui, cp, cto)
