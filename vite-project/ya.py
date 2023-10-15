import json
import csv

data = {
  "-Nglto3GYStR9bo0vyAo": {
    "date": "2023-08-15",
    "duration_minutes": 10,
    "time": "23:08"
  },
  "-Ngltqo1nf49HVrCSCvD": {
    "date": "2023-08-16",
    "duration_minutes": 12,
    "time": "23:08"
  },
  "-NgltsjONAAMCv9DWpdV": {
    "date": "2023-08-17",
    "duration_minutes": 9,
    "time": "23:14"
  },
  "-NgltuPfRQH_LkqaJ0T1": {
    "date": "2023-08-18",
    "duration_minutes": 10,
    "time": "23:12"
  },
  "-Nglu0RsHizHk8qGuTp3": {
    "date": "2023-08-19",
    "duration_minutes": 11,
    "time": "23:12"
  },
  "-Nglu2OjOkreIJhZGy42": {
    "date": "2023-08-20",
    "duration_minutes": 12,
    "time": "23:12"
  },
  "-Nglu2wU2I1QG_Z96U6x": {
    "date": "2023-08-21",
    "duration_minutes": 13,
    "time": "23:12"
  },
  "-Nglu3TTTdazg6e4psdg": {
    "date": "2023-08-22",
    "duration_minutes": 9,
    "time": "23:12"
  },
  "-Nglu47goEu-gwntrsZZ": {
    "date": "2023-08-23",
    "duration_minutes": 11,
    "time": "23:12"
  },
  "-Nglu586jZzbl_UnGzyj": {
    "date": "2023-08-24",
    "duration_minutes": 12,
    "time": "23:12"
  },
  "-Nglu5Ym9XTRiISNqiWE": {
    "date": "2023-08-25",
    "duration_minutes": 9,
    "time": "23:12"
  },
  "-Nglu6Cnc5qoUBKSYyZG": {
    "date": "2023-08-26",
    "duration_minutes": 14,
    "time": "23:12"
  },
  "-Nglu6a_npDuQ3GZ6ih8": {
    "date": "2023-08-27",
    "duration_minutes": 10,
    "time": "23:12"
  },
  "-Nglu6s31mtSfINxwNMW": {
    "date": "2023-08-28",
    "duration_minutes": 9,
    "time": "23:12"
  },
  "-NgluxoxoigRBZuJSbFl": {
    "date": "2023-08-29",
    "duration_minutes": 10,
    "time": "22:09"
  },
  "-Nglv5FUWPgqnZZz0Yu3": {
    "date": "2023-08-30",
    "duration_minutes": 8,
    "time": "21:44"
  },
  "-Nglv63hoBQCngmguA-B": {
    "date": "2023-08-31",
    "duration_minutes": 9,
    "time": "22:40"
  },
  "-Nglv6MQVQrCF3BKefow": {
    "date": "2023-09-01",
    "duration_minutes": 10,
    "time": "21:38"
  },
  "-Nglv6WQrQqL0hbcBHQ5": {
    "date": "2023-09-02",
    "duration_minutes": 10,
    "time": "22:30"
  },
  "-Nglv6eWSoW6wz-y4Ye4": {
    "date": "2023-09-03",
    "duration_minutes": 10,
    "time": "22:35"
  },
  "-Nglv6nkkb_bHKQOjyOy": {
    "date": "2023-09-04",
    "duration_minutes": 8,
    "time": "21:35"
  },
  "-Nglv6wcn058glQo4m6c": {
    "date": "2023-09-05",
    "duration_minutes": 10,
    "time": "22:34"
  },
  "-Nglv72u_sJw_OjqhZ9L": {
    "date": "2023-09-06",
    "duration_minutes": 10,
    "time": "22:43"
  },
  "-Nglv7AMkumVC3C37Rsd": {
    "date": "2023-09-07",
    "duration_minutes": 9,
    "time": "22:36"
  },
  "-Nglv7GjXLkbmlYUN92X": {
    "date": "2023-09-08",
    "duration_minutes": 9,
    "time": "21:45"
  },
  "-Nglv7NbyCxMX5Gv_zPV": {
    "date": "2023-09-09",
    "duration_minutes": 10,
    "time": "21:45"
  },
  "-Nglv7UVNxi7L7h_2K6t": {
    "date": "2023-09-10",
    "duration_minutes": 10,
    "time": "21:30"
  },
  "-Nglv7aXWOfj1SJcmF35": {
    "date": "2023-09-11",
    "duration_minutes": 8,
    "time": "21:32"
  },
  "-Nglv7iIgo4NILMFPIrM": {
    "date": "2023-09-12",
    "duration_minutes": 10,
    "time": "22:41"
  },
  "-Nglv7pe4y1q79w7DWIi": {
    "date": "2023-09-13",
    "duration_minutes": 0,
    "time": "22:45"
  },
  "-Nglv7xzrbAgastmRblJ": {
    "date": "2023-09-14",
    "duration_minutes": 8,
    "time": "21:36"
  },
  "-Nglv83edsgoQx6d6Uh8": {
    "date": "2023-09-15",
    "duration_minutes": 10,
    "time": "21:38"
  },
  "-Nglv8Au0ELNvKe4jqHC": {
    "date": "2023-09-16",
    "duration_minutes": 10,
    "time": "21:42"
  },
  "-Nglv8MhetoD3BMkG0wy": {
    "date": "2023-09-17",
    "duration_minutes": 9,
    "time": "22:39"
  },
  "-NglvGYlu9rUFEIEy9n-": {
    "date": "2023-09-18",
    "duration_minutes": 11,
    "time": "22:35"
  },
  "-NglvGeYhwBTLgKUOxJo": {
    "date": "2023-09-19",
    "duration_minutes": 11,
    "time": "21:42"
  },
  "-NglvGkpEqGTHaHQR805": {
    "date": "2023-09-20",
    "duration_minutes": 9,
    "time": "21:37"
  },
  "-NglvGrZ8Ro3DA0QCiQy": {
    "date": "2023-09-21",
    "duration_minutes": 7,
    "time": "21:31"
  },
  "-NglvGzYCFKJLnMUQH5y": {
    "date": "2023-09-22",
    "duration_minutes": 8,
    "time": "21:36"
  },
  "-NglvH5TKfHZYs67qZ2i": {
    "date": "2023-09-23",
    "duration_minutes": 11,
    "time": "21:44"
  },
  "-NglvHBCjBlC2NHt__bG": {
    "date": "2023-09-24",
    "duration_minutes": 9,
    "time": "22:45"
  },
  "-NglvHHXZOW3ESDIsyk-": {
    "date": "2023-09-25",
    "duration_minutes": 8,
    "time": "22:31"
  },
  "-NglvHO7_Vz5b7gKmQ-7": {
    "date": "2023-09-26",
    "duration_minutes": 8,
    "time": "22:34"
  },
  "-NglvHUNF_J531y_muia": {
    "date": "2023-09-27",
    "duration_minutes": 9,
    "time": "21:30"
  },
  "-NglvHa2EIhtTlRcj3As": {
    "date": "2023-09-28",
    "duration_minutes": 7,
    "time": "21:31"
  },
  "-NglvHgfCRbYaHx9JEi7": {
    "date": "2023-09-29",
    "duration_minutes": 9,
    "time": "21:30"
  },
  "-NglvHn05cCoacCh2qaU": {
    "date": "2023-09-30",
    "duration_minutes": 9,
    "time": "21:33"
  },
  "-NglvHt9_jpFoPUkJUDq": {
    "date": "2023-10-01",
    "duration_minutes": 8,
    "time": "21:40"
  },
  "-NglvHzD37rbRxLBB-yu": {
    "date": "2023-10-02",
    "duration_minutes": 7,
    "time": "22:33"
  },
  "-NglvI4OTcdsoiTHwfx2": {
    "date": "2023-10-03",
    "duration_minutes": 6,
    "time": "22:45"
  },
  "-NglvI9lmKd5xkZKXAh3": {
    "date": "2023-10-04",
    "duration_minutes": 7,
    "time": "21:33"
  },
  "-NglvIEjuoL_vF8vrdaf": {
    "date": "2023-10-05",
    "duration_minutes": 7,
    "time": "22:36"
  },
  "-NglvQnJC5xOpFldNdOv": {
    "date": "2023-10-06",
    "duration_minutes": 5,
    "time": "22:35"
  },
  "-NglvQw1SL6bP2KNWiU6": {
    "date": "2023-10-07",
    "duration_minutes": 6,
    "time": "21:45"
  },
  "-NglvR4VcirEr5g7vhA9": {
    "date": "2023-10-08",
    "duration_minutes": 4,
    "time": "21:34"
  },
  "-NglvRD5tTlFcWj02CLM": {
    "date": "2023-10-09",
    "duration_minutes": 6,
    "time": "22:34"
  },
  "-NglvS6q5lrQ-X0C4fID": {
    "date": "2023-10-10",
    "duration_minutes": 5,
    "time": "21:31"
  },
  "-NglvSsScVGPFMRAJ7aR": {
    "date": "2023-10-11",
    "duration_minutes": 6,
    "time": "21:35"
  },
  "-NglvT1wnz4aQc0-Ui8v": {
    "date": "2023-10-12",
    "duration_minutes": 6,
    "time": "22:36"
  },
  "-NglvTB8U94NcMnony5G": {
    "date": "2023-10-13",
    "duration_minutes": 5,
    "time": "22:30"
  },
  "-NglvTI05i8CnXfEbe-6": {
    "date": "2023-10-14",
    "duration_minutes": 5,
    "time": "21:41"
  }
}


cleaned_data = [v for v in data.values()]

# Define the CSV file path
csv_file = 'output.csv'

# Write data to CSV
with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(cleaned_data[0].keys())  # Write header
    for row in cleaned_data:
        writer.writerow(row.values())

print(f'Data written to {csv_file}')