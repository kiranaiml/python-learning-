from abc import ABC, abstractmethod

# The Low-Level Tool Interface
class PlatformAPI(ABC):
    @abstractmethod
    def upload(self, video_file):
        pass

class InstagramAPI(PlatformAPI):
    def upload(self, video_file):
        print(f"Uploading {video_file} to Instagram...")

# The High-Level Manager
class ReelPublisher:
    def __init__(self, platform: PlatformAPI):
        self.platform = platform

    def publish_video(self, video_file):
        self.platform.upload(video_file)

# Execution
my_publisher = ReelPublisher(InstagramAPI())
my_publisher.publish_video("forest_ride_techno.mp4")