# 파이썬프로그래밍
# Json File Parser 개발
# 정보보호학과 20184606 김준영

import glob # 파일 리스트를 얻기 위해 'glob' 모듈 사용
import json # Json 데이터를 처리하기 위해 'json' 모듈 사용
import csv # CSV 데이터를 처리하기 위해 'csv' 모듈 사용

# 'glob' 모듈을 이용해 매개변수 'path' 위치에 확장자가 '.json'인 파일의 경로 목록을 리스트 'json_list'로 반환하는 함수 'glob_json_list' 정의
def glob_json_list(path):
    file_list = glob.glob(path)
    json_list = [file for file in file_list if file.endswith(".json")]
    return json_list

print("[Json File Parser]")

# 변수 'path'에 현재 경로 저장
path = "./*"

#현재 디렉터리에 있는 파일들을 파싱할건지 묻기
print("Do you want to parse files in current directory?")

# 오류 처리를 위해 사용될 변수 'error' 선언
error = 1 

# 오류 발생 시 입력을 다시 받기 위한 반복문
while error != 0:
    # 사용자의 입력 받기
    answer = input("[y/n] : ")

    # 오류 발생 여부 판단
    if answer == "y": # 현재 디렉터리의 Json 파일을 파싱
        error = 0 # 변수 'error'를 0으로 초기화하여 while문 반복 방지
        pass
    elif answer == "n": # 다른 디렉터리의 Json 파일을 파싱
        error = 0 # 변수 'error'를 0으로 초기화하여 while문 반복 방지
        # 사용자로부터 파싱할 파일이 있는 디렉터리 주소를 입력받음
        # ex) ../otherDirectory
        path = input("Input other directory's path : ") + "/*"
    else: # y나 n이 아닌 다른 문자를 입력했을때 변수 'error'는 1로 변함이 없으므로 while문 반복
        print("Error! Enter [y] or [n]")

# 디렉터리에 Json 파일이 없을 경우 프로그램 종료
if not glob_json_list(path):
    print("No Json File in directory... This program will be terminated.")
    exit()
else: # 파싱할 파일 리스트(함수 'glob_json_list(path)'의 반환값) 출력
    print("Files to be parsed : %s" % glob_json_list(path))

print("Saving data to \"result.csv\"...")

# 함수 'glob_json_list'의 반환값 'json_list' 리스트의 요소들을 대입해 반복 수행
for json_list in glob_json_list(path):
    # Json 파일의 데이터를 불러와서 'data'에 저장
    with open(json_list) as json_file:
            data = json.load(json_file)

    # Json 파일의 'objects' 데이터를 'objects'에 저장
    objects = data['objects']

    # 파싱한 데이터를 저장할 CSV 파일을 추가 모드로 여는 'data_file' 정의
    data_file = open("./result.csv", 'a')

    csv_writer = csv.writer(data_file)

    # 헤더를 구분하기 위해 사용할 변수 'count' 선언
    count = 0

    for car in objects:
        # CSV 파일에 헤더 작성
        if count == 0:
            header = car.keys()
            csv_writer.writerow(header)
            count += 1

        # CSV 파일에 데이터 작성
        csv_writer.writerow(car.values())

    # CSV 파일 닫기
    data_file.close()

# 파싱 완료 문구 출력
print("Json File Parsing is done! (Json -> CSV)")
