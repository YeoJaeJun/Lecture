# jupyter notebook 명령어 (magic command)
# %%writefile file_name: 실행하면 cell의 내용을 파일에 출력한다.

def memo():
    print("저장할 파일명을 입력하세요.")
    file_name = input("파일명 입력: ")
    print(f"{file_name}에 저장합니다.")
    print("=" * 30)

    with open(file_name, mode = "wt", encoding = "utf-8") as fw:
        print("저장할 내용을 입력하세요.")
        print("=" * 30)
        while True:
            line_txt = input("> ")
            if line_txt == "!q":
                break
            fw.write(line_txt + "\n")

    print("입력을 종료합니다.")
    print("=" * 30)
