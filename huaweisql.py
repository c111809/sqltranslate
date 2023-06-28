import pandas as pd

def generate_create_table_statements(file_path, sheet_name):
    # 读取 Excel 文件
    df = pd.read_excel(file_path, sheet_name=sheet_name, header=None)

    # 获取第二列中 "字段编码" 所在行的索引
    indices = df[df.iloc[:, 1] == "字段编码"].index

    # 存储建表语句的列表
    create_table_statements = []

    # 遍历每个 "字段编码" 单元格上面一个单元格的值
    for idx in indices:
        # 取index的上一个
        row_index = idx - 1
        # 获取到单元格值
        table_name = df.iloc[row_index, 1]
        table_comment = df.iloc[row_index, 0]

        # 表名
        create_table_statement = f"CREATE TABLE `{table_name}` (\n"

        # 存储列定义语句的列表
        column_definitions = []

        # 遍历每个 "字段编码" 单元格后面的值直到空单元格结束
        row_indexc = idx + 1
        # 判断空单元格
        while row_indexc < len(df) and pd.notna(df.iloc[row_indexc, 1]):
            column_name = df.iloc[row_indexc, 1]
            column_comment = df.iloc[row_indexc, 0]
            # 列定义语句
            column_definition = f"  `{column_name}` VARCHAR(255) COMMENT '{column_comment}'"
            column_definitions.append(column_definition)
            row_indexc += 1

        # 将列定义语句添加到建表语句中
        create_table_statement += ",\n".join(column_definitions)
        create_table_statement += f"\n) COMMENT='{table_comment}';"

        # 将建表语句添加到列表中
        create_table_statements.append(create_table_statement)

    return create_table_statements

# 保存为.sql文件
def save_to_sql_file(file_path, sheet_name, output_file):
    create_table_statements = generate_create_table_statements(file_path, sheet_name)
    with open(output_file, 'w', encoding='utf-8') as f:
        for statement in create_table_statements:
            f.write(statement + '\n\n')

# 调用函数保存为.sql文件
file_path = 'ts.xlsx'
sheet_name = '表结构'
output_file = 'huawei.txt'
save_to_sql_file(file_path, sheet_name, output_file)
