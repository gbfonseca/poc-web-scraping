import sys
from simple_scenarium import simple_scenarium
from automated_scenarium import automated_scenarium


if __name__ == "__main__":
    if sys.argv[1] == 'simple_scenarium':
        simple_scenarium()
    else:
        automated_scenarium()
