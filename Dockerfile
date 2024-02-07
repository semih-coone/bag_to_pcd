FROM osrf/ros:noetic-desktop-full

RUN apt-get update && apt-get install -y \
    pcl-tools nano \
    && rm -rf /var/lib/apt/lists/*

# convert_pcd.py betiğini kopyala
COPY convert_pcd.py /convert_pcd.py

# /bag_files, /output_bag_files gibi mount noktaları için dizinler oluştur
RUN mkdir /bag_files /output_bag_files

# Docker container başladığında çalışacak komut
COPY start.sh /start.sh
RUN chmod +x /start.sh

CMD ["/start.sh"]
