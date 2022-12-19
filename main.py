import easyocr
import os


def text_recognition(file_path, text_file_name="/result/result.txt"):
    reader = easyocr.Reader(["ru", "en"])
    result = reader.readtext(file_path, detail=0, paragraph=True)

    with open(text_file_name, "a") as file:
        for line in result:
            file.write(f"{line}\n")
        file.write(f"\n\n\n\n")

    return f"Result write into {text_file_name}"


def main():
    dir_path = "/DataForOCR"
    for filename in os.listdir(dir_path):

        if filename.endswith('.jpeg') or filename.endswith('.png') or filename.endswith('.jpg'):
            print(text_recognition(file_path=filename))

        else:
            print('Bad file:', filename)


if __name__ == '__main__':
    main()
