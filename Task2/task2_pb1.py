import os
import sys

def create_hello_file():
    target_dir = "/study/linux/test"
    file_path = os.path.join(target_dir, "hello.txt")
    
    try:
        # /test 디렉토리가 없으면 생성 시도
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)
            print(f"디렉토리 생성 완료: {target_dir}")
            
        # 파일 생성 및 내용 작성
        with open(file_path, "w", encoding="utf-8") as f:
            f.write("Hello Linux\n")
            
        print(f"파일 생성 성공: {file_path}")
        print("내용: Hello Linux")
        
    except PermissionError:
        print(f"[오류] {target_dir}에 접근하거나 파일을 생성할 권한이 없습니다.", file=sys.stderr)
        print("팁: sudo 권한을 사용해 프로그램을 실행하거나, 해당 디렉토리의 권한을 변경하세요.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"[예외 발생] {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    create_hello_file()
