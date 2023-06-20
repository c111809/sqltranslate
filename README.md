# sqltranslate
这是一个萌新写的把oracle sql语句转换成表结构的脚本



感谢Chatgpt大力支持:)附上gpt的对话：https://chat.openai.com/share/9af3bc4b-5886-494c-ac01-476143bb7e71



有兴趣的小伙伴可以看一下（好多废话，前面一大半都没用，懒得删了）



一开始的想法是把Oracle变成Mysql再导入到Mysql库里再获取表结构，结果问题太多，能力不够搞不定



这里给出的办法是直接提取create语句中的表名、列名、表解释、列解释。本来还应该包括主键的



可以生成一个带目录的表结构。




by the way 似乎缺失了一个文件，后续补上
