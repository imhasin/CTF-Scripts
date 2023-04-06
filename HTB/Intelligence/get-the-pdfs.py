import datetime
import requests
import PyPDF2
import io

start_date = datetime.date(2020, 1, 1)
end_date = datetime.date.today()
timedelta = datetime.timedelta(1)


while start_date != end_date:

    filename = f"{start_date}-upload.pdf"
    url = f"http://10.10.10.248/documents/{filename}"
    
    r = requests.get(url)
    if r.status_code == 200:       
        with open(filename, "wb") as f:
            f.write(r.content)
            print(f"{filename} successfully downloaded!")
    start_date += timedelta
