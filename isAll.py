import csv

# 用于保存已经出现过的 bvid
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
