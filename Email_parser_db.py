import imaplib, os, email, webbrowser, credentials
from email.header import decode_header
from datetime import datetime
from bs4 import BeautifulSoup
import pandas as pd
from lxml import html
# @author: roigecode

CONTADOR_INSCRIPCIONES = 0
print("-> Introduce la fecha inicial de inscripciones en formato (y-m-d h-m-s)")
print("-> Ejemplo: 2022-03-19 13:57:00")
#FECHA_INICIAL = input(">> ")

# This function parses de IMAP date into a datetime format
def parseDate(date_string):

    date_parser = {
        "Jan" : "01",
        "Feb" : "02",
        "Mar" : "03",
        "Apr" : "04",
        "May" : "05",
        "Jun" : "06",
        "Jul" : "07",
        "Aug" : "08",
        "Sep" : "09",
        "Oct" : "10",
        "Nov" : "11",
        "Dec" : "11" 
    }

    try:
        date_string_list = list(date_string)
        date_string_list[2] = '/'
        date_string_list[6] = '/'
        date_string_list[3:6] = date_parser[''.join(date_string_list[3:6])]
        date_string_list[7:9] = ''
        date_string = ''.join(date_string_list)
    except:
        pass

    return date_string

def clean(text):
    # Clean text for creating a folder:
    return "".join(c if c.isalnum() else "_" for c in text)

# ---------- #
# Main Code: #
# ---------- #

# Create an IMAP4 class with SSL and authenticate:
imap = imaplib.IMAP4_SSL("imap.ionos.es")
imap.login(f"{credentials.USERNAME}", f"{credentials.PASSWORD}")

# Select inbox mailbox:
status, messages = imap.select("INBOX")

# Number of top emails to fetch, change to all after testing:
N = 5

# Total of emails:
messages = int(messages[0])

print(f"\n>> Leyendo: {credentials.USERNAME}\n")

# Loop in reverse so we start from the top:

for i in range(messages,0, -1):
    # Fetch the email message by ID:
    res, msg = imap.fetch(str(i), "(RFC822)")

    for response in msg:
        if isinstance(response, tuple):
            # Parse a bytes email into a message object
            msg = email.message_from_bytes(response[1])
         

            # Decode the email subject
            subject, encoding = decode_header(msg["Subject"])[0]

            if isinstance(subject, bytes):
                # If it's a bytes, decode to string:
                try:
                    subject = subject.decode(encoding)
                except:
                    pass

                if subject == "Nueva Inscripción":
                    # Decode the email sender:
                    From, encoding = decode_header(msg.get("From"))[0]

                    if isinstance(From, bytes):
                        From = From.decode(encoding)

                    try:
                        date_string = msg["Date"][5:25]
                        parsed_date = str(parseDate(date_string))
                        date_normal = datetime.strptime(parsed_date, f'%d/%m/%y %H:%M:%S')
                        print("Fecha: ",date_normal)
                    except:
                        print("Fecha: --/--/-- --:--:--")

                    print("Subject:", subject)
                    print("From:", From)
                    print(">> ¡Añadiendo inscripción al Excel!")

                    # If the email message is multipart
                    # Iterate over email parts:
                    for part in msg.walk():
                        # Extract content type of email:
                        content_type = part.get_content_type()
                        content_disposition = str(part.get("Content-Disposition"))

                        try:
                            # Get the email body
                            body = part.get_payload(decode=True).decode()
                        except:
                            print("Error reading body!")

                        # READ BODY: 
                        if content_type == "text/html":
                            # if it's HTML, create a new HTML file and open it in browser
                            folder_name = "inscripciones"

                            if not os.path.isdir(folder_name):
                                # make a folder for this email (named after the subject)
                                os.mkdir(folder_name)

                            CONTADOR_INSCRIPCIONES += 1
                            filename = f"inscripcion{CONTADOR_INSCRIPCIONES}.html"
                            filepath = os.path.join(folder_name, filename)
                            # write the file
                            try:
                                open(filepath, "w").write(body)
                                pass
                            except:
                                print(">> Error abriendo el HTML")
                            
                            # Open in the default browser:
                            # webbrowser.open(filepath)                 

            # Prints:
            if subject == "Nueva Inscripción":
                print("-"*51)

# Close the connection and logout:
imap.close()
imap.logout()

# Use beautiful soup to read the html files:

nombres = []
emails = []
telf = []
sexo_y_talla = []
categoria = []
horario_pref = []
ropa_extra = []

for i in range(1,CONTADOR_INSCRIPCIONES):
    soup = BeautifulSoup(open(f"F:\webmarc\scripts\inscripciones\inscripcion{i}.html"), "html.parser")
    p = soup.find_all('p')

    for i in range(1,len(p),2):
        aux1 = str(p[i]).replace('<p style="font-family: sans-serif; font-size: 14px; font-weight: normal; margin: 0; Margin-bottom: 15px; padding-bottom: 5px;">','')
        aux2 = aux1.replace('</p>','')
        p[i] = aux2

    if (p[1], p[9]) not in nombres:
        nombres.append((p[1], p[9]))
        emails.append((p[3], p[11]))
        telf.append((p[5], p[13]))
        sexo_y_talla.append((p[7], p[15]))
        categoria.append((p[17]))
    else:
        print(f'>> ¡REPETIDO! : ', (p[1], p[9]))
        nombres.append((f'>> ¡REPETIDO! : ', p[1], p[9]))
        emails.append((p[3], p[11]))
        telf.append((p[5], p[13]))
        sexo_y_talla.append((p[7], p[15]))
        categoria.append((p[17]))
    
    try:
        if p[19] == "Tades":
            p[19] = "Tardes (15:00h - 22:00h)"
            horario_pref.append(p[19])
        elif p[19] == "Mañanas":
            p[19] = "Mañanas (9:00h - 15:00h)"
            horario_pref.append(p[19])
        elif p[19] == '2 x Sudadera Golden Point (40€)':
            horario_pref.append(p[19])
        else:
            horario_pref.append(p[19])
    except:
        horario_pref.append(('-'))

columnas = [nombres,emails,telf,sexo_y_talla, categoria, horario_pref, ropa_extra]
    
df = pd.DataFrame({
    'Nombres' : nombres,
    'Emails' : emails,
    'Teléfonos' : telf,
    'Sexo - Talla' : sexo_y_talla,
    'Categoría' : categoria,
    'Horario Pref.' : horario_pref,
})

writer = pd.ExcelWriter('inscripciones.xlsx', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer, sheet_name='Inscripciones', index=False)

# Close the Pandas Excel writer and output the Excel file.
try:
    writer.save()
except:
    print(">> ERROR: Asegúrate de no tener el EXCEL abierto!")

print("\n>> ¡EXCEL CREADO CON ÉXITO! <<\n")
