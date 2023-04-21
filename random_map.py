import random
import matplotlib.pyplot as plt
for i in range(1):
    # 定义栅格环境的大小和分辨率
    grid_width = 1000
    grid_height = 1000
    resolution = 10
    # 定义圆和矩形的最小和最大尺寸
    min_circle_radius = 100
    max_circle_radius = 200
    min_rect_width = 100
    max_rect_width = 250
    min_rect_height = 100
    max_rect_height = 250
    # 创建空白的栅格环境
    grid = [[(255, 255, 255) for y in range(grid_height)] for x in range(grid_width)]
    # 随机生成一定数量的圆和矩形，并检查它们是否与先前生成的形状重叠
    shapes = []
    num_shapes = random.randint(4, 7)
    for i in range(num_shapes):
        shape_type = random.choice(['circle', 'rectangle'])
        if shape_type == 'circle':
            radius = random.randint(min_circle_radius, max_circle_radius)
            x = random.randint(radius, grid_width - radius)
            y = random.randint(radius, grid_height - radius)
            is_overlapping = False
            for shape in shapes:
                if shape[0] == 'circle':
                    dx = shape[1][0] - x
                    dy = shape[1][1] - y
                    distance = (dx ** 2 + dy ** 2) ** 0.5
                    if distance < shape[2] + radius:
                        is_overlapping = True
                        break
                else:
                    if (abs(shape[1][0] - x) < shape[2][0] + radius and
                        abs(shape[1][1] - y) < shape[2][1] + radius):
                        is_overlapping = True
                        break
            if not is_overlapping:
                shapes.append(('circle', (x, y), radius))
        else:
            width = random.randint(min_rect_width, max_rect_width)
            height = random.randint(min_rect_height, max_rect_height)
            x = random.randint(0, grid_width - width)
            y = random.randint(0, grid_height - height)
            is_overlapping = False
            for shape in shapes:
                if shape[0] == 'circle':
                    dx = shape[1][0] - (x + width/2)
                    dy = shape[1][1] - (y + height/2)
                    distance = (dx ** 2 + dy ** 2) ** 0.5
                    if distance < shape[2]:
                        is_overlapping = True
                        break
                else:
                    if (abs(shape[1][0] - x) < shape[2][0] + width and
                        abs(shape[1][1] - y) < shape[2][1] + height):
                        is_overlapping = True
                        break
            if not is_overlapping:
                shapes.append(('rectangle', (x, y), (width, height)))
# 将形状绘制到栅格环境中
    for shape in shapes:
        if shape[0] == 'circle':
            x, y = shape[1]
            radius = shape[2]
            for i in range(int(x - radius), int(x + radius)):
                for j in range(int(y - radius), int(y + radius)):
                    if ((i - x) ** 2 + (j - y) ** 2) ** 0.5 <= radius:
                        grid[i][j] = (0, 0, 0)
        else:
            x, y = shape[1]
            width, height = shape[2]
            for i in range(int(x), int(x + width)):
                for j in range(int(y), int(y + height)):
                    grid[i][j] = (0, 0, 0)
# 将栅格环境保存为图像文件
    from PIL import Image
    img = Image.new('RGB', (grid_width, grid_height))
    pixels = img.load()
    for x in range(grid_width):
        for y in range(grid_height):
            pixels[x, y] = grid[x][y]
    img.save('Obstacle_OceanEnvironment.png')
