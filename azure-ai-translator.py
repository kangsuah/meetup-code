import requests
import json

# 1. 정보 입력(번역기 - 키 및 엔드포인트)
endpoint = ""
key = ""

# 2. SAS URL 입력 (스토리지 컨테이너에서 생성한 것)
# beforeUrl: 원본 파일이 들어있는 컨테이너의 전체 SAS URL
before_sas_url = ""
# afterUrl: 번역본을 저장할 컨테이너의 전체 SAS URL
after_sas_url = ""

# 3. 요청 URL 구성 (Batch Translation 경로)
path = "translator/text/batch/v1.1/batches"
constructed_url = endpoint + path

# 4. 헤더 및 본문 구성
headers = {
    "Ocp-Apim-Subscription-Key": key,
    "Content-Type": "application/json"
}

body = {
    "inputs": [
        {
            "source": {  
                "sourceUrl": before_sas_url,
                "storageSource": "AzureBlob",
                "language": ""
            },
            "targets": [
                {
                    "targetUrl": after_sas_url,
                    "storageSource": "AzureBlob",
                    "category": "general",
                    "language": ""
                }
            ]
        }
    ]
}

# 5. 전송
try:
    response = requests.post(constructed_url, headers=headers, json=body)

    if response.status_code == 202:
        print("✅ 작업이 성공적으로 제출되었습니다!")
        print(f"Operation Location: {response.headers.get('Operation-Location')}")
        print("잠시 후 Azure Storage의 after 컨테이너를 확인해보세요.")
    else:
        print(f"❌ 오류 발생: {response.status_code}")
        print(response.text)

except Exception as e:
    print(f"Error: {e}")

# 5. 전송
try:
    response = requests.post(constructed_url, headers=headers, json=body)

    if response.status_code == 202:
        print("✅ 작업이 성공적으로 제출되었습니다!")
        print(f"Operation Location: {response.headers.get('Operation-Location')}")
        print("잠시 후 Azure Storage의 after 컨테이너를 확인해보세요.")
    else:
        print(f"❌ 오류 발생: {response.status_code}")
        print(response.text)

except Exception as e:
    print(f"Error: {e}")


