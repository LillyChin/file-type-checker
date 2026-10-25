from pathlib import Path
print("檔案分類小工具")
folder = Path("test_files")

counts ={}
total = 0

for file in folder.iterdir():
    if file.is_file():
        extension = file.suffix.lower()
        if extension == ".pdf":
            what = "PDF"
        elif extension in [".jpg",".jpeg",".png"]:
            what= "圖片"
        elif extension in [".doc",".docx",".txt"]:
            what= "文件"
        elif extension in [".xls",".xlsx",".csv"]:
            what= "試算表"
        elif extension in [".mp4"]:
            what= "影片"
        elif extension in [".mp3"]:
            what= "音檔"
        elif extension in [".rar",".zip",".7z"]:
            what= "壓縮檔"
        else:
            what= "其他檔案"
        print(file.name," 我是",what)

        if what not in counts:
            counts[what]=0
        counts[what] = counts[what]+1
        total += 1

print("\n======計算結果======")
for what , count in counts.items():
    print(what, "有", count ,"個")
print("總計",total,"個檔案")