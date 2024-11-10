import requests
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, '2304.01852v4_22.pdf')
url = "http://127.0.0.1:2000/s3r/upload"  # FastAPI 서버 URL

file_path = "/Users/iyeongho/Desktop/converter_api/2304.01852v4_22.pdf"
with open(FILE_PATH, "rb") as file:
    response = requests.post(url, files={"file": file})

print(response.status_code)  # 응답 코드 확인
print(response.json())       # 응답 내용 확인