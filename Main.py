from commands import create_channel
from commands import tasks
import loader
def main():
    loader.add_group(tasks.init)
    loader.add_group(create_channel.init)
    loader.run_bot()
if __name__ == "__main__":
    main()
