# 🔩 Galbot One Golf Description

![Galbot One Golf](docs/images/g1.png)

**[中文](#中文文档) | [English](#english-docs)**

---

## 中文文档

本包提供了 Galbot One Golf 机器人的描述文件（URDF/XACRO/MJCF）和3D模型，包含配置、可视化和仿真所需的基本文件。

### 📁 包结构

仓库包含以下主要目录：

#### 根目录

- **`source/galbot_one_golf_description/`** – 主要的 ROS 包目录，包含所有源文件。
- **`mjcf/`** – 生成的 MJCF 模型文件及相关网格文件，用于 MuJoCo 仿真。
- **`urdf/`** – 生成的 URDF 文件及相关网格文件。
- **`usd/`** – USD（通用场景描述）文件，用于机器人可视化和仿真。

#### 包目录（`source/galbot_one_golf_description/`）

- **`config/`** – 包含配置文件，包括 RViz 显示配置。
- **`launch/`** – 包含用于可视化机器人及其各个组件的 ROS 启动文件。
- **`meshes/`** – 存储机器人的3D模型（原始网格、凸包、凸分解），包含用于碰撞和视觉表示的单独文件。
- **`xacro/`** – 包含用于定义和组装机器人模型的模块化 Xacro 文件，包括碰撞类型、末端执行器类型和相机安装类型。
- **`metadata/`** – 包含用于 MJCF 转换的元数据文件（actuator.json、default.json、metadata.json、appendix.xml）。
- **`predefined_description/`** – 包含预定义的 URDF 描述（例如，球体碰撞模型）。
- **`scripts/`** – 包含实用脚本（例如，visualize_urdf.py）。
- **`test/`** – 包含用于单个机器人组件的测试 Xacro 文件。
- **`tools/`** – 包含不同末端执行器配置的 TOML 配置文件和网格文件。

### 🚀 使用方法

#### 在 RViz 中查看机器人

使用提供的启动文件在 RViz 中可视化机器人：

```bash
roslaunch galbot_one_golf_description display.launch
```

要显示单个组件（如左臂），请使用以下命令：

```bash
roslaunch galbot_one_golf_description launch_individual_part.launch xacro_file:=test/test_left_arm.xacro collision_type:=convex_decomposition
```

> 可用的碰撞类型：`mesh`（网格）、`convex_hull`（凸包）、`convex_decomposition`（凸分解）、`sphere`（球体）

#### 生成自定义描述

用户可以通过选择不同的末端执行器、传感器和碰撞类型来自定义机器人，然后生成用于仿真的 URDF 或 MJCF 文件。

例如，如果您需要在左手安装夹爪、右手安装吸盘，并在两个手腕上安装摄像头，同时使用凸分解表示碰撞，可以运行以下命令：

```bash
cd source/galbot_one_golf_description
python create_description.py
```

> 连续按下回车键将选择默认选项（不带任何末端工具、传感器，使用凸包表示碰撞）。

#### 创建 MJCF 文件

安装 `urdf2mjcf`（需要 Python >= 3.10）：

```bash
git clone https://github.com/TATP-233/urdf2mjcf.git
cd urdf2mjcf
pip install .
```

生成 MJCF 模型：

```bash
cd galbot_one_golf_description
urdf2mjcf galbot_one_golf.urdf --output mjcf/galbot_one_golf.xml --metadata metadata/metadata.json --default-metadata metadata/default.json --actuator-metadata metadata/actuator.json --appendix metadata/appendix.xml
```

### 🙋 故障排除

如果您遇到任何问题、有疑问或想要贡献，请联系 [package.xml](source/galbot_one_golf_description/package.xml) 中列出的维护者。

### 📜 许可证

Apache License 2.0 - 详见 [LICENSE](LICENSE) 文件

---

## English Docs

This package provides the robot description files (URDF/XACRO/MJCF) and 3D models for the Galbot One Golf robot. It includes essential files needed for configuration, visualization, and simulation.

### 📁 Package Structure

The repository is organized into the following main directories:

#### Root Level

- **`source/galbot_one_golf_description/`** – The main ROS package directory containing all source files.
- **`mjcf/`** – Generated MJCF model files and associated meshes for MuJoCo simulation.
- **`urdf/`** – Generated URDF files and associated meshes.
- **`usd/`** – USD (Universal Scene Description) files for robot visualization and simulation.

#### Package Directory (`source/galbot_one_golf_description/`)

- **`config/`** – Contains configuration files, including RViz display configurations.
- **`launch/`** – Includes ROS launch files for visualizing the robot and its individual components.
- **`meshes/`** – Stores 3D models (original mesh, convex hull, convex decomposition) of the robot, with separate files for collision and visual representation.
- **`xacro/`** – Contains modular Xacro files used to define and assemble the robot model, including collision types, end effector types, and camera mounting types.
- **`metadata/`** – Contains metadata files for MJCF conversion (actuator.json, default.json, metadata.json, appendix.xml).
- **`predefined_description/`** – Contains predefined URDF descriptions (e.g., sphere collision model).
- **`scripts/`** – Contains utility scripts (e.g., visualize_urdf.py).
- **`test/`** – Contains test Xacro files for individual robot components.
- **`tools/`** – Contains TOML configuration files and meshes for different end effector configurations.

### 🚀 Usage

#### Viewing the Robot in RViz

To visualize the robot in RViz, use the provided launch file:

```bash
roslaunch galbot_one_golf_description display.launch
```

To display a single component, such as the left arm, use the following command:

```bash
roslaunch galbot_one_golf_description launch_individual_part.launch xacro_file:=test/test_left_arm.xacro collision_type:=convex_decomposition
```

> Available collision types: `mesh`, `convex_hull`, `convex_decomposition`, `sphere`

#### Generating a Custom Description

Users can customize the robot by selecting different end effectors, sensors, and collision types, and then generate URDF or MJCF files for simulation.

For example, if you need a gripper on the left hand, a suction cup on the right hand, and cameras mounted on both wrists with convex decomposition for collisions:

```bash
cd source/galbot_one_golf_description
python create_description.py
```

> Continuous pressing the enter key will select the default option (no end effector, no sensor, using convex hull to represent collision).

#### Create MJCF File

Install `urdf2mjcf` (requires Python >= 3.10):

```bash
git clone https://github.com/TATP-233/urdf2mjcf.git
cd urdf2mjcf
pip install .
```

Generate a MJCF model:

```bash
cd galbot_one_golf_description
urdf2mjcf galbot_one_golf.urdf --output mjcf/galbot_one_golf.xml --metadata metadata/metadata.json --default-metadata metadata/default.json --actuator-metadata metadata/actuator.json --appendix metadata/appendix.xml
```

### 🙋 Troubleshooting

If you encounter any issues, have questions, or would like to contribute, please reach out to the maintainers listed in the [package.xml](source/galbot_one_golf_description/package.xml).

### 📜 License

Apache License 2.0 - see the [LICENSE](LICENSE) file for details.
