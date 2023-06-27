import sys
from simple_scenarium import simple_scenarium
from automated_scenarium import automated_scenarium


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Passe como argumento um dos cenários possíveis:")
        print("1 - simple_scenarium")
        print("2 - automated_scenarium")
    else:
        if sys.argv[1] == 'simple_scenarium':
            simple_scenarium()
        elif sys.argv[1] == 'automated_scenarium':
            automated_scenarium()


