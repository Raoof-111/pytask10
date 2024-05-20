
"""1) Ilk olaraq bir "Example" adında bir kateqoriya (directory) yaradırıq.
2)Daha sonra isə bu directorynin içərisində bir  "subdirect"  adında alt kateqoriya(subdirectory) yaradırıq.
3)Növbəti addımda bu subdirectorynin içərisinə  bir şəkil və bir text faylı əlavə edirik. 
(şəkli ilk öncə manual olaraq hal hazırda olduğunuz qovluğun içərisinə sürüşdürüb  
daha sonra alt kateqoriyaya əlavə edin, path-ini tapmağda çətinlik çəkməmək üçün)
4)daha sonra isə subdirectorynin içərisində olub sonu txt ilə bitən faylları 
subdirectorydən çıxarıb Example directory-sinə göndərirsiniz.
    """


import os
import shutil


example_dir = "Example"
os.makedirs(example_dir, exist_ok=True)


subdirect_dir = os.path.join(example_dir, "subdirect")
os.makedirs(subdirect_dir, exist_ok=True)

image_file = "horse.jpg"  
text_file = "belo.txt"    

#
shutil.move(image_file, os.path.join(subdirect_dir, image_file))
shutil.move(text_file, os.path.join(subdirect_dir, text_file))

for file_name in os.listdir(subdirect_dir):
    if file_name.endswith(".txt"):
        shutil.move(os.path.join(subdirect_dir, file_name), os.path.join(example_dir, file_name))

print("bitdi")
