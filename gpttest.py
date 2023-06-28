import steamship
from steamship import Steamship


client = Steamship(workspace="gpt-4")

generator = client.use_plugin('gpt-4')

task = generator.generate(text="生成一张狗的图片")
task.wait()
print(task.output.blocks[0].text)