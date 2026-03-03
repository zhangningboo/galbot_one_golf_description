# 🔩 Galbot One golf Description | Galbot One golf 描述

This package provides the robot description files (URDF/XACRO/MJCF) and 3D models for the Galbot robot. It includes essential files needed for configuration, visualization, and simulation.

本包提供了Galbot机器人的描述文件（URDF/XACRO/MJCF）和3D模型。它包含了配置、可视化和仿真所需的基本文件。

## 📁 Package Structure | 包结构

The repository is organized into the following main directories:

仓库包含以下主要目录：

### Root Level | 根目录

- **`source/galbot_one_golf_description/`** – The main ROS package directory containing all source files.
- **`source/galbot_one_golf_description/`** – 主要的ROS包目录，包含所有源文件。

- **`mjcf/`** – Generated MJCF model files and associated meshes for MuJoCo simulation.
- **`mjcf/`** – 生成的MJCF模型文件及相关网格文件，用于MuJoCo仿真。

- **`urdf/`** – Generated URDF files and associated meshes.
- **`urdf/`** – 生成的URDF文件及相关网格文件。

- **`usd/`** – USD (Universal Scene Description) files for robot visualization and simulation.
- **`usd/`** – USD（通用场景描述）文件，用于机器人可视化和仿真。

### Package Directory (`source/galbot_one_golf_description/`) | 包目录

- **`config/`** – Contains configuration files, including RViz display configurations.
- **`config/`** – 包含配置文件，包括RViz显示配置。

- **`launch/`** – Includes ROS launch files for visualizing the robot and its individual components.
- **`launch/`** – 包含用于可视化机器人及其各个组件的ROS启动文件。

- **`meshes/`** – Stores 3D models (original mesh, convex hull, convex decomposition) of the robot, with separate files for collision and visual representation.
- **`meshes/`** – 存储机器人的3D模型（原始网格、凸包、凸分解），包含用于碰撞和视觉表示的单独文件。

- **`xacro/`** – Contains modular Xacro files used to define and assemble the robot model, including collision types, end effector types, and camera mounting types.
- **`xacro/`** – 包含用于定义和组装机器人模型的模块化Xacro文件，包括碰撞类型、末端执行器类型和相机安装类型。

- **`metadata/`** – Contains metadata files for MJCF conversion (actuator.json, default.json, metadata.json, appendix.xml).
- **`metadata/`** – 包含用于MJCF转换的元数据文件（actuator.json、default.json、metadata.json、appendix.xml）。

- **`predefined_description/`** – Contains predefined URDF descriptions (e.g., sphere collision model).
- **`predefined_description/`** – 包含预定义的URDF描述（例如，球体碰撞模型）。

- **`scripts/`** – Contains utility scripts (e.g., visualize_urdf.py).
- **`scripts/`** – 包含实用脚本（例如，visualize_urdf.py）。

- **`test/`** – Contains test Xacro files for individual robot components.
- **`test/`** – 包含用于单个机器人组件的测试Xacro文件。

- **`tools/`** – Contains TOML configuration files and meshes for different end effector configurations.
- **`tools/`** – 包含不同末端执行器配置的TOML配置文件和网格文件。

## 🚀 Usage | 使用方法

### Viewing the Robot in RViz | 在RViz中查看机器人

To visualize the robot in RViz, use the provided launch file:

要在RViz中可视化机器人，请使用提供的启动文件：

```bash
roslaunch galbot_one_golf_description display.launch
```

To display a single component, such as the head, use the following command:

要显示单个组件（如头部），请使用以下命令：

```bash
roslaunch galbot_one_golf_description launch_individual_part.launch xacro_file:=test/test_left_arm.xacro collision_type:=convex_decomposition
```

> Available collision types: `mesh`, `convex_hull`, `convex_decomposition`, `sphere`

> 可用的碰撞类型：`mesh`（网格）、`convex_hull`（凸包）、`convex_decomposition`（凸分解）、`sphere`（球体）

### Generating a Custom Description | 生成自定义描述

Users can customize the robot by selecting different end effectors, sensors, and collision types, and then generate URDF or MJCF files for simulation.

用户可以通过选择不同的末端执行器、传感器和碰撞类型来自定义机器人，然后生成用于仿真的URDF或MJCF文件。

For example, if you need a gripper on the left hand, a suction cup on the right hand, and cameras mounted on both wrists, and you want to represent collisions using convex decomposition, you can configure these options and generate the corresponding robot description.

例如，如果您需要在左手安装夹爪，右手安装吸盘，并在两个手腕上安装摄像头，并且希望使用凸分解来表示碰撞，您可以配置这些选项并生成相应的机器人描述。

Run the following command to create a custom robot description:

运行以下命令创建自定义机器人描述：

```bash
cd source/galbot_one_golf_description
python create_description.py
```

> Continuous pressing the enter key will select the default option (no end effector, no sensor, using convex hull to represent collision).

> 连续按下回车键将选择默认选项（不带任何末端工具、传感器，使用凸包表示碰撞）。


### Create mjcf file | 创建mjcf文件

Run the following command to install `urdf2mjcf`, need python>=3.10.

运行以下指令安装`urdf2mjcf`,要求python版本>=3.10.

```
git clone https://github.com/TATP-233/urdf2mjcf.git
cd urdf2mjcf
pip install .
```

To create a mjcf model

创建一个mjcf模型
```
cd galbot_one_golf_description
urdf2mjcf galbot_one_golf.urdf --output mjcf/galbot_one_golf.xml --metadata metadata/metadata.json --default-metadata metadata/default.json --actuator-metadata metadata/actuator.json --appendix metadata/appendix.xml
```


---

## 🙋 Troubleshooting | 故障排除

If you encounter any issues, have questions, or would like to contribute, please reach out to the maintainers listed in the [package.xml](source/galbot_one_golf_description/package.xml).

如果您遇到任何问题、有疑问或想要贡献，请联系[package.xml](source/galbot_one_golf_description/package.xml)中列出的维护者。

---

## 📜 License | 许可证

Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

Apache License 2.0 - 详见 [LICENSE](LICENSE) 文件
