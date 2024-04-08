import os
from tqdm import tqdm

def main():
    label_path = r"datasets\4.2k HRW yolo dataset\4.2k_HRW_yolo_dataset_edited\labels"
    # label_path = "mock"
    directory = list(os.walk(label_path))

    for root, dirs, files in directory:
        for file in files:
            if ".txt" in file:

                file_lines = []
                file_name = f"{root}/{file}"

                with open(file_name, encoding="utf-8", mode="r") as f:
                    file_lines = f.readlines()
                    # print(file_lines)

                    if len(file_lines) == 0:
                        raise ValueError("file empty")

                    for index, line in enumerate(file_lines):

                        category = int(line.split(" ")[0])
                        
                        # raise-hand case (0) -> head-up   (0, nothing changed)
                        # read case       (1) -> head-up   (0)
                        # write case      (2) -> head-down (1)
                        category = category - 1 if category > 0 else category

                        # Join back to origin string
                        line = str(category) + line[1:]

                        file_lines[index] = line
                    
                with open(file_name, encoding="utf-8", mode="w") as f:
                    # print(file_lines)
                    f.writelines(file_lines)

if __name__ == "__main__":
    main()