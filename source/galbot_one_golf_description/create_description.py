#####################################################################################
#
# Copyright (c) 2023-2025 Galbot, Inc. All Rights Reserved.
#
# This software contains confidential and proprietary information of Galbot, Inc.
# ("Confidential Information"). You shall not disclose such Confidential Information
# and shall use it only in accordance with the terms of the license agreement you
# entered into with Galbot, Inc.
#
# UNAUTHORIZED COPYING, USE, OR DISTRIBUTION OF THIS SOFTWARE, OR ANY PORTION OR
# DERIVATIVE THEREOF, IS STRICTLY PROHIBITED. IF YOU HAVE RECEIVED THIS SOFTWARE IN
# ERROR, PLEASE NOTIFY GALBOT, INC. IMMEDIATELY AND DELETE IT FROM YOUR SYSTEM.
#
#####################################################################################
#
# Description: Script for creating robot description for Galbot.
# Maintainer: Herman Ye, Yuhao Zeng@Galbot
#
#####################################################################################
import os
import shutil
import subprocess
import xml.etree.ElementTree as ET
from datetime import datetime
import importlib.util
import sys

# Get the script's directory
SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))

def check_xacro_availability():
    """Check if xacro is available and return the appropriate command."""
    try:
        # First try to use ROS xacro
        subprocess.run(["xacro", "--version"], capture_output=True, check=True)
        return "xacro"
    except (subprocess.CalledProcessError, FileNotFoundError):
        try:
            # Try to import Python xacro package
            importlib.import_module("xacro")
            return "python_xacro"
        except ImportError:
            print("Neither ROS xacro nor Python xacro package is available.")
            print("Please install Python xacro package using:")
            print("pip install xacro")
            sys.exit(1)


# Function: Display robot model options
def select_robot_model():
    print("\nPlease select a robot model (press enter to choose default [0]):")
    print("[0] Galbot One golf [Recommended]")

    model_choice = input("Enter your choice: ")

    if model_choice == "0" or model_choice == "":
        return "galbot_one_golf"
    else:
        print("\nInvalid input, please enter a valid number")
        return select_robot_model()


# Function: Display left arm tool options
def select_left_tool():
    print("\nPlease select the left arm tool (press enter to choose default [0]):")
    print("[0] None")
    print("[1] Hitbot Gripper")
    print("[2] Galbot Suction Cup1")
    print("[3] Galbot Gripper1")

    left_tool_choice = input("Enter your choice: ")

    if left_tool_choice == "0" or left_tool_choice == "":
        return "none"
    elif left_tool_choice == "1":
        return "hitbot_gripper"
    elif left_tool_choice == "2":
        return "galbot_suction_cup1"
    elif left_tool_choice == "3":
        return "galbot_gripper1"
    else:
        print("\nInvalid input, please enter a valid number")
        return select_left_tool()


# Function: Display right arm tool options
def select_right_tool():
    print("\nPlease select the right arm tool (press enter to choose default [0]):")
    print("[0] None")
    print("[1] Hitbot Gripper")
    print("[2] Galbot Suction Cup1")
    print("[3] Galbot Gripper1")

    right_tool_choice = input("Enter your choice: ")

    if right_tool_choice == "0" or right_tool_choice == "":
        return "none"
    elif right_tool_choice == "1":
        return "hitbot_gripper"
    elif right_tool_choice == "2":
        return "galbot_suction_cup1"
    elif right_tool_choice == "3":
        return "galbot_gripper1"
    else:
        print("\nInvalid input, please enter a valid number")
        return select_right_tool()


def select_left_wrist_sensor():
    print("\nPlease select the left wrist sensor (press enter to choose default [0]):")
    print("[0] None")
    print("[1] D415 Camera")
    print("[2] D405 Camera")

    left_wrist_sensor_choice = input("Enter your choice: ")

    if left_wrist_sensor_choice == "0" or left_wrist_sensor_choice == "":
        return "none"
    elif left_wrist_sensor_choice == "1":
        return "d415_camera"
    elif left_wrist_sensor_choice == "2":
        return "d405_camera"

    else:
        print("\nInvalid input, please enter a valid number")
        return select_left_wrist_sensor()


def select_right_wrist_sensor():
    print("\nPlease select the right wrist sensor (press enter to choose default [0]):")
    print("[0] None")
    print("[1] D415 Camera")
    print("[2] D405 Camera")

    right_wrist_sensor_choice = input("Enter your choice: ")

    if right_wrist_sensor_choice == "0" or right_wrist_sensor_choice == "":
        return "none"
    elif right_wrist_sensor_choice == "1":
        return "d415_camera"
    elif right_wrist_sensor_choice == "2":
        return "d405_camera"

    else:
        print("\nInvalid input, please enter a valid number")
        return select_right_wrist_sensor()


def select_collision_type():
    print("\nPlease select the collision type (press enter to choose default [0]):")
    print("[0] Convex Hull [Recommended]")
    print("[1] Sphere")
    print("[2] Convex Decomposition")
    print("[3] Original Mesh")

    collision_type_choice = input("Enter your choice: ")

    if collision_type_choice == "0" or collision_type_choice == "":
        return "convex_hull"
    elif collision_type_choice == "1":
        return "sphere"
    elif collision_type_choice == "2":
        return "convex_decomposition"
    elif collision_type_choice == "3":
        return "mesh"
    else:
        print("\nInvalid input, please enter a valid number")
        return select_collision_type()


def process_for_isaac_sim(robot_name, urdf_path):
    effort_rate = 5
    velocity_rate = 5
    # Process the URDF file for Isaac Sim

    # Get the directory and filename of the URDF file
    urdf_dir = os.path.dirname(urdf_path)
    urdf_filename = os.path.basename(urdf_path)

    # Create a new directory with the robot name
    new_dir_name = f"isaac_sim_{robot_name}"
    download_dir = os.path.join(os.path.expanduser("~"), "Downloads")
    new_dir_path = os.path.join(download_dir, new_dir_name)
    # Delete the directory if it already exists
    if os.path.exists(new_dir_path):
        shutil.rmtree(new_dir_path)
    os.makedirs(new_dir_path, exist_ok=True)

    # Copy the URDF file to the new directory
    new_urdf_path = os.path.join(new_dir_path, urdf_filename)
    shutil.copy2(urdf_path, new_urdf_path)
    print(f"URDF file copied to: {new_urdf_path}")

    # Copy the meshes folder to the new directory
    meshes_dir = os.path.join(urdf_dir, "meshes")
    if os.path.exists(meshes_dir) and os.path.isdir(meshes_dir):
        new_meshes_dir = os.path.join(new_dir_path, "meshes")
        shutil.copytree(meshes_dir, new_meshes_dir)
        print(f"Meshes folder copied to: {new_meshes_dir}")
    else:
        print(f"No 'meshes' directory found in {urdf_dir}")
        raise FileNotFoundError("Meshes directory not found")

    # Process new_urdf file
    with open(new_urdf_path, "r", encoding="utf-8") as file:
        urdf_content = file.read()

    # Delete the ros package name from the URDF file
    urdf_content = urdf_content.replace(f"package://{robot_name}_description/", "")

    # Parse the URDF XML content and update effort values and velocity
    try:
        root = ET.fromstring(urdf_content)
        for joint in root.findall(".//joint"):
            limit = joint.find("limit")
            if limit is not None and "effort" in limit.attrib:
                original_effort = float(limit.attrib["effort"])
                tripled_effort = original_effort * effort_rate
                limit.attrib["effort"] = str(tripled_effort)
                print(
                    f"Joint '{joint.attrib['name']}' effort updated: "
                    f"{original_effort} -> {tripled_effort}"
                )
            if limit is not None and "velocity" in limit.attrib:
                original_velocity = float(limit.attrib["velocity"])
                tripled_velocity = original_velocity * velocity_rate
                limit.attrib["velocity"] = str(tripled_velocity)
                print(
                    f"Joint '{joint.attrib['name']}' effort updated: "
                    f"{original_effort} -> {tripled_effort}"
                )
                print(
                    f"Joint '{joint.attrib['name']}' velocity updated: "
                    f"{original_velocity} -> {tripled_velocity}"
                )
        urdf_content = ET.tostring(root, encoding="unicode")
    except ET.ParseError as e:
        print(f"Error parsing URDF for effort or velocity adjustment: {e}")
        return

    # Write the modified URDF content back to the file
    with open(new_urdf_path, "w", encoding="utf-8") as file:
        file.write(urdf_content)

    print(
        f"All 'package://{robot_name}_description/' occurrences removed from: {new_urdf_path}"
    )
    print(f"\nIsaac Sim URDF file {robot_model}.urdf created successfully.")
    print(f"Isaac Sim URDF Path: {new_urdf_path}")

    # Get version from package.xml
    package_xml_path = os.path.join(urdf_dir, "package.xml")
    version = "unknown"
    if os.path.exists(package_xml_path):
        try:
            tree = ET.parse(package_xml_path)
            root = tree.getroot()
            version = (
                root.find("version").text.strip()
                if root.find("version") is not None
                else "unknown"
            )
        except ET.ParseError:
            print("Error parsing package.xml for version.")

    # Get the latest git commit hash
    try:
        hash_result = subprocess.run(
            ["git", "rev-parse", "HEAD"], capture_output=True, text=True, cwd=urdf_dir
        )
        git_hash = hash_result.stdout.strip()
    except Exception as e:
        git_hash = "unknown"
        print(f"Error getting git hash: {e}")

    # Create a README.md file in the new directory
    readme_path = os.path.join(new_dir_path, "README.md")
    readme_content = f"""
    Generated by Galbot Description Creator\nAuthor: Herman Ye@Galbot\nVersion: {version}\nName: {robot_name}\nHash: {git_hash}\nDate: {datetime.now().strftime('%Y-%m-%d')}\nNote: All torques have been set to their fake peak values ({effort_rate} times the rated torque).
    """
    with open(readme_path, "w", encoding="utf-8") as readme_file:
        readme_file.write(readme_content.strip())

    print(f"README.md created at: {readme_path}")


# Main program
robot_model = select_robot_model()
left_tool = select_left_tool()
right_tool = select_right_tool()
left_wrist_sensor = select_left_wrist_sensor()
right_wrist_sensor = select_right_wrist_sensor()
collision_type = select_collision_type()

# Check selections
print("\nYou have selected:")
print(f"Robot model: {robot_model}")
print(f"Left arm tool: {left_tool}")
print(f"Right arm tool: {right_tool}")
print(f"Left wrist sensor: {left_wrist_sensor}")
print(f"Right wrist sensor: {right_wrist_sensor}")
print(f"Collision type: {collision_type}")
proceed_choice = input(
    "\nDo you want to proceed with these selections? (y/n) or press enter to choose default [y]: "
)

if proceed_choice.lower() == "y" or proceed_choice.lower() == "":
    print("Creating URDF file...")

    # Construct the robot description path
    ROBOT_DESCRIPTION_DIR = os.path.join(
        os.path.dirname(SCRIPT_DIR), f"{robot_model}_description"
    )

    print(f"Robot Description Directory: {ROBOT_DESCRIPTION_DIR}")

    # Go to specific robot description xacro folder
    os.chdir(os.path.join(ROBOT_DESCRIPTION_DIR, "xacro"))

    # Backup previous urdf file
    urdf_file_path = os.path.join(ROBOT_DESCRIPTION_DIR, f"{robot_model}.urdf")
    backup_file_path = urdf_file_path + ".bak"

    if os.path.isfile(urdf_file_path):
        os.rename(urdf_file_path, backup_file_path)
        print("Backup of previous URDF file created.")
        print(f"Path: {backup_file_path}")

    # Convert xacro to urdf
    subprocess.run(
        [
            "xacro",
            f"{robot_model}.xacro",
            f"left_arm_end_effector_type:={left_tool}",
            f"right_arm_end_effector_type:={right_tool}",
            f"left_wrist_sensor_type:={left_wrist_sensor}",
            f"right_wrist_sensor_type:={right_wrist_sensor}",
            f"collision_type:={collision_type}",
            "-o",
            urdf_file_path,
        ]
    )
    # Add to predefined description
    if collision_type == "sphere":
        subprocess.run(
            [
                "xacro",
            f"{robot_model}.xacro",
            f"left_arm_end_effector_type:={left_tool}",
            f"right_arm_end_effector_type:={right_tool}",
            f"left_wrist_sensor_type:={left_wrist_sensor}",
            f"right_wrist_sensor_type:={right_wrist_sensor}",
            f"collision_type:={collision_type}",
            "-o",
            os.path.join(ROBOT_DESCRIPTION_DIR, "predefined_description", f"{robot_model}_sphere.urdf"),
        ]
    )
    # Ask user if they want to create URDF for isaac sim
    create_isaac_sim_urdf = input(
        "\nDo you want to create URDF for isaac sim?"
        "\nThis is only applicable for sim (y/n) or press enter to skip: "
    )
    if create_isaac_sim_urdf.lower() == "y":
        # Call the create_isaac_sim_urdf function
        process_for_isaac_sim(robot_model, urdf_file_path)
    else:
        print("Skipping the creation of isaac sim URDF.")

    print(f"\nStandard URDF file {robot_model}.urdf created successfully.")
    print(f"Standard URDF Path: {urdf_file_path}")

else:
    print("Exiting program...")
