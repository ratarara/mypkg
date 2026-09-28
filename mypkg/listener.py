import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16


def main():
    rclpy.init()
    node = Node("listener")

    def cb(msg):
        node.get_logger().info("Listen: %d" % msg.data)

    node.create_subscription(Int16, "countup", cb, 10)
    rclpy.spin(node)


if __name__ == '__main__':
    main()
