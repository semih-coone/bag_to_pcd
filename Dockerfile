FROM osrf/ros:noetic-desktop-full

RUN apt-get update && apt-get install -y \
    pcl-tools nano \
    && rm -rf /var/lib/apt/lists/*

COPY convert_pcd.py /convert_pcd.py

RUN mkdir /bag_files /output_bag_files

COPY start.sh /start.sh
RUN chmod +x /start.sh

CMD ["/start.sh"]
