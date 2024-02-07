import rosbag, os
import subprocess

def extract_topics_from_bag(bag_file):
    topics = []
    with rosbag.Bag(bag_file, 'r') as bag:
        for topic, _, _ in bag.read_messages():
            if topic not in topics and topic.startswith('/lidar'):
                topics.append(topic)
    return topics

def convert_bag_to_pcd(bag_file, lidar_topics):
    bag_file_name = os.path.splitext(os.path.basename(bag_file))[0]
    for topic in lidar_topics:
        output_folder = os.path.join('output_bag_files', bag_file_name, topic.replace('/', '_'))
        os.makedirs(output_folder, exist_ok=True)
        #output_file = os.path.join(output_folder, f"{bag_file_name}.pcd")
        command = f'rosrun pcl_ros bag_to_pcd {bag_file} {topic} {output_folder} __hostname:=localhost:11311'
        try:
            subprocess.check_output(command, shell=True)
            print(f"PCD file saved: {output_folder}")
        except subprocess.CalledProcessError as e:
            print(f'Error converting topic {topic}: {e}')

def main(bag_files_dir):
    import os
    command = 'bash -c "source /opt/ros/noetic/setup.bash"'
    subprocess.check_output(command, shell=True)
    print('------------------------------------------')
    print('Setupping... Please wait 1-2 minutes.')
    print('------------------------------------------')
    bag_files = [f for f in os.listdir(bag_files_dir) if f.endswith('.bag')]
    for bag_file in bag_files:
        bag_file_path = os.path.join(bag_files_dir, bag_file)
        lidar_topics = extract_topics_from_bag(bag_file_path)
        convert_bag_to_pcd(bag_file_path, lidar_topics)
    print('------------------------------------------')
    print('Done!')
    print('------------------------------------------')

if __name__ == "__main__":
    bag_files_dir = "bag_files"  # Bag files directory path
    main(bag_files_dir)