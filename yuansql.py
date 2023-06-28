import pandas as pd
import rey


def convert_data_type(data_type):
    """
    将通用数据类型转换为MySQL数据类型
    """
    data_type = data_type.lower()
    if data_type == '不多于10个字符':
        return 'VARCHAR(10)'
    elif data_type == '32 位 16 进制字符，uuid ver4 采用':
        return 'CHAR(32)'
    elif data_type == '1-32位字符串':
        return 'VARCHAR(32)'
    elif data_type == '4 位时间格式':
        return 'TIME'
    elif data_type == '1个字符':
        return 'CHAR(1)'
    elif data_type == '1-10 位数字':
        return 'INT(10)'
    elif data_type == '5 位数字':
        return 'INT(5)'
    elif data_type == '1 位数字':
        return 'INT(1)'
    else:
        return 'varchar(255)'


def has_chinese(text):
    """
    判断文本中是否包含中文字符
    """
    pattern = re.compile(r'[\u4e00-\u9fa5]')
    return bool(pattern.search(text))


def generate_create_table_sql(file_path):
    # 读取Excel文件
    df = pd.read_excel(file_path)

    # 获取唯一的表名称列表
    table_names = df.iloc[:, 0].unique()

    # 创建表的SQL语句列表
    sql_list = []

    # 遍历每个表名称
    for table_name in table_names:
        # 筛选当前表的数据项
        table_df = df[df.iloc[:, 0] == table_name]

        # 创建表的SQL语句
        sql = f"CREATE TABLE {table_name} ("

        # 遍历当前表的每个数据项
        for _, row in table_df.iterrows():
            column_name = row[2]
            column_comment = row[1]
            data_type = convert_data_type(row[3])

            # 判断是否包含中文，如果包含中文则跳过当前行
            if has_chinese(column_name):
                continue

            # 添加列定义到SQL语句
            sql += f"\n    {column_name} {data_type} COMMENT '{column_comment}',"

        # 移除最后一个逗号
        sql = sql[:-1]

        # 完成SQL语句
        sql += "\n);"

        # 添加到SQL语句列表
        sql_list.append(sql)

    return sql_list


# 替换为你的Excel文件路径
excel_file_path = "yuan12.xlsx"

# 生成创建表的SQL语句列表
create_table_sql_list = generate_create_table_sql(excel_file_path)

# 写入到txt文件
output_file_path = "output12.txt"
with open(output_file_path, 'w', encoding='utf-8') as file:
    for sql in create_table_sql_list:
        file.write(sql)
        file.write('\n\n')

print(f"生成的MySQL创建表语句已写入文件：{output_file_path}")
