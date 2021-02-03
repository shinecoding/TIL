while True:
    try:
        print(input())
    except EOFError:
        break

#EOF (End Of File)로 파일이 끝나는 곳이 아닌데 끝이 났다는 에러
