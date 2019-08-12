import os
import glob
import shutil
import getpass # 유저 네임 추출
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers import interval

print('Made By Jung Ji Woo')
print()
print("Downloads 폴더를 확인해보세요")
user_name = getpass.getuser() # 유저 네임


dir_path = 'C:/Users/{}/Downloads'.format(user_name) # 경로
dir_name_Image = 'Image' # Image 폴더 이름
dir_name_Zip = 'Zip' # Zip 폴더 이름
dir_name_Pdf = 'Pdf' # Pdf 폴더 이름
dir_name_Excel = 'Excel' # Excel 폴더 이름
dir_name_Video = 'Video' # Video 폴더 이름
dir_name_Word = 'Word' # Word 폴더 이름
dir_name_Etc = 'Etc' # Etc 폴더 이름

def job_function():
# Image 폴더 존재 하지 않을 시 Image 폴더 생성
    if os.path.isdir(dir_path+"/"+dir_name_Image+"/"): 
        pass
    else:
        os.mkdir(dir_path+"/"+dir_name_Image+"/")

    # Zip 폴더 
    if os.path.isdir(dir_path+"/"+dir_name_Zip+"/"):
        pass
    else:
        os.mkdir(dir_path+"/"+dir_name_Zip+"/")

    # Pdf 폴더
    if os.path.isdir(dir_path+"/"+dir_name_Pdf+"/"):
        pass
    else:
        os.mkdir(dir_path+"/"+dir_name_Pdf+"/")

    # Excel 폴더
    if os.path.isdir(dir_path+"/"+dir_name_Excel+"/"):
        pass
    else:
        os.mkdir(dir_path+"/"+dir_name_Excel+"/")
    
    # Video 폴더
    if os.path.isdir(dir_path+"/"+dir_name_Video+"/"):
        pass
    else:
        os.mkdir(dir_path+"/"+dir_name_Video+"/")
    
    # Word 폴더
    if os.path.isdir(dir_path+"/"+dir_name_Word+"/"):
        pass
    else:
        os.mkdir(dir_path+"/"+dir_name_Word+"/")

    # Etc 폴더
    if os.path.isdir(dir_path+"/"+dir_name_Etc+"/"): 
        pass
    else:
        os.mkdir(dir_path+"/"+dir_name_Etc+"/") 


    # 수정해야할 것들 
    # for (1) in glob.glob(~~~~~~~~~~~~~~~~,(2)):
    #       (3) = str(4).split~~~~
    #       shutil.move(dir_path / (5), dir_path / dir_name_(6) / (7))

    
    # 경로에 있는 jpg , bmp , gif 파일 모두 image 폴더에 넣기 
    for a in glob.glob(os.path.join(dir_path,'*.gif')):
        gif_final = str(a).split("\\")[1]
        shutil.move(dir_path+"/"+gif_final,dir_path+"/"+dir_name_Image+"/"+gif_final)

    for b in glob.glob(os.path.join(dir_path,'*.jpg')):
        jpg_final = str(b).split("\\")[1]
        shutil.move(dir_path+"/"+jpg_final,dir_path+"/"+dir_name_Image+"/"+jpg_final)

    for c in glob.glob(os.path.join(dir_path,'*.bmp')):
        bmp_final = str(c).split("\\")[1]
        shutil.move(dir_path+"/"+bmp_final,dir_path+"/"+dir_name_Image+"/"+bmp_final)

    # 경로에 있는 zip 파일 Zip 폴더에 넣기
    for d in glob.glob(os.path.join(dir_path,'*.zip')):
        zip_final = str(d).split("\\")[1]
        shutil.move(dir_path+"/"+zip_final,dir_path+"/"+dir_name_Zip+"/"+zip_final)

    # 경로에 있는 pdf 파일 Pdf 폴더에 넣기
    for e in glob.glob(os.path.join(dir_path,'*.pdf')):
        pdf_final = str(e).split("\\")[1]
        shutil.move(dir_path+"/"+pdf_final,dir_path+"/"+dir_name_Pdf+"/"+pdf_final)

    # 경로에 있는 xlsx 파일 Excel 폴더에 넣기
    for f in glob.glob(os.path.join(dir_path,'*.xlsx')):
        xlsx_final = str(f).split("\\")[1]
        shutil.move(dir_path+"/"+xlsx_final,dir_path+"/"+dir_name_Excel+"/"+xlsx_final)

    # 경로에 있는 mp4,avi,mkv Video 폴더에 넣기

    for g in glob.glob(os.path.join(dir_path,'*.mp4')):
        mp4_final = str(g).split("\\")[1]
        shutil.move(dir_path+"/"+mp4_final,dir_path+"/"+dir_name_Video+"/"+mp4_final)

    for h in glob.glob(os.path.join(dir_path,'*.avi')):
        avi_final = str(h).split("\\")[1]
        shutil.move(dir_path+"/"+avi_final,dir_path+"/"+dir_name_Video+"/"+avi_final)

    for i in glob.glob(os.path.join(dir_path,'*.mkv')):
        mkv_final = str(i).split("\\")[1]
        shutil.move(dir_path+"/"+mkv_final,dir_path+"/"+dir_name_Video+"/"+mkv_final)
    
    # 경로에 있는 hwp 파일 , txt파일 Word 폴더에 넣기
    for j in glob.glob(os.path.join(dir_path,'*.hwp')):
        hwp_final = str(j).split("\\")[1]
        shutil.move(dir_path+"/"+hwp_final,dir_path+"/"+dir_name_Word+"/"+hwp_final)

    for k in glob.glob(os.path.join(dir_path,'*.txt')):
        txt_final = str(k).split("\\")[1]
        shutil.move(dir_path+"/"+txt_final,dir_path+"/"+dir_name_Word+"/"+txt_final)


    # 경로에 있는 나머지 파일들 Etc 폴더에 넣기
    for z in glob.glob(os.path.join(dir_path,'*.*')):
        etc_final = str(z).split("\\")[1]
        shutil.move(dir_path+"/"+etc_final,dir_path+"/"+dir_name_Etc+"/"+etc_final)
    

sched = BlockingScheduler()
trigger = interval.IntervalTrigger(seconds=3)
sched.add_job(job_function,trigger=trigger)
sched.start()


# 코드를 짜다가, endswith 방법은 나머지 확장자들을 etc 폴더에 넣을 수 있는 방법이 없어서
# 위에  적혀진 str.split('.')[1] 를 썻지만 이것 또한 파일이름이 .이 여러개면 해결 할 수 없고, 폴더명이 같이 포함되서 해결할수없음.
# 그래서 glob.glob를 알아냈는데, glob를 쓰면 모든 경로가 다 나오고 마지막 경로가 \으로 나오는걸  이용해서 split("\\")를 사용해서 경로의 파일확장자를 추출함

# for f in os.listdir(dir_path):
#     # if str(f).split('.')[1] in name:
#     #     shutil.move(os.path.join(dir_path,f),os.path.join(dir_path,dir_name_Image,f))
#     # else:
#     #     shutil.move(dir_path+"/"+f,dir_path+"/"+dir_name_Etc+"/"+f)
#     if f.glob("*.jpg"):
#         shutil.move(dir_path+"/"+f,dir_path+"/"+dir_name_Image+"/"+f) # jpg
#     if f.glob("*.bmp"):
#         shutil.move(dir_path+"/"+f,dir_path+"/"+dir_name_Image+"/"+f) # bmp
#     if glob.("*.gif"):
#         shutil.move(dir_path+"/"+f,dir_path+"/"+dir_name_Image+"/"+f) # gif
#     if f.endswith(".zip"):
#         shutil.move(dir_path+"/"+f,dir_path+"/"+dir_name_Zip+"/"+f) # zip
        
#     shutil.move(dir_path+"/"+f,dir_path+"/"+dir_name_Etc+"/"+f) # ETC 해결해야함

# # 파일리스트 갯수
# a = len(next(os.walk(dir_path))[2])-1

# print(a)