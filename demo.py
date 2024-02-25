import csv
import os

# 要合并的 CSV 文件夹路径
folder_path = 'data'

# 合并后的 CSV 文件名
output_file = 'merged_data.csv'

# 打开合并后的 CSV 文件以写入模式
with open(output_file, 'w', newline='', encoding='utf-8') as output_csvfile:
    writer = csv.writer(output_csvfile)

    # 遍历文件夹中的每个 CSV 文件
    for filename in os.listdir(folder_path):
        if filename.endswith('.csv'):
            csv_file = os.path.join(folder_path, filename)

            # 打开当前 CSV 文件以读取模式
            with open(csv_file, 'r', newline='', encoding='utf-8') as input_csvfile:
                reader = csv.reader(input_csvfile)

                # 从当前 CSV 文件中读取数据，并写入合并后的 CSV 文件中
                for row in reader:
                    writer.writerow(row)

print("CSV 文件合并完成")

seen_bvids = set()

# 打开原始文件和写入文件
with open('merged_data.csv', 'r', newline='', encoding='utf-8') as input_file, \
        open('unique.csv', 'w', newline='', encoding='utf-8') as output_file:
    reader = csv.reader(input_file)
    writer = csv.writer(output_file)

    # 逐行读取原始文件
    for row in reader:
        # 提取每行的第一列（bvid）
        bvid = row[0].strip()
        # 如果当前 bvid 是新的，则将整行写入到输出文件中，并将其添加到已经出现过的 bvid 集合中
        if bvid not in seen_bvids:
            writer.writerow(row)
            seen_bvids.add(bvid)

print("重复行已剔除，唯一行已保存到 unique.csv 文件中")
