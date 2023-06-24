import sys
from simple_scenarium import simple_scenarium
from dynamic_scenarium import dynamic_scenarium


if __name__ == "__main__":
    if sys.argv[1] == 'simple_scenarium':
        simple_scenarium()
    else:
        dynamic_scenarium()
