import numpy as np
def read_txt(inputpath, output_path1, output_path2, output_path3):
    with open(output_path1, 'w', encoding='utf-8') as file1:
        with open(output_path2, 'w', encoding='utf-8') as file2:
            with open(output_path3, 'w', encoding='utf-8') as file3:
                with open(inputpath, 'r', encoding='utf-8') as infile:
                    data2 = []
                    for line in infile:
                        data_line = line.strip("\n").split('\t')
                        print(data_line)
                        data2.append([int(i) for i in data_line])
                    np.random.seed(789786)
                    np.random.shuffle(data2)
                    print(data2)
                    
                    cou = 0
                    for line in data2:
                            cou=cou+1
                            data = '' + '\t'.join(str(i) for i in line) + '\n'  # 用\t隔开
                            if(cou<=4549):
                                file1.write(data)
                            elif(4550<=cou<=5199):
                                file2.write(data)
                            else:
                                file3.write(data)

if __name__ == "__main__":
    input_path = 'all.txt'
    output_path1 = 'RQ4/train.txt'
    output_path2 = 'RQ4/valid.txt'
    output_path3 = 'RQ4/test.txt'
    read_txt(input_path, output_path1, output_path2, output_path3)