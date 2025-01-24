from commands import test
from commands.tasks import tasks
import loader
def main():
    loader.add_group(tasks.init)
    loader.run_bot()
if __name__ == "__main__":
    main()