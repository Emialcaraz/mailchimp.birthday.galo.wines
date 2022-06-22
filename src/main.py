import sys
import traceback

from mailchimp_birthday.orchestrator import Orchestrator


def main():
    orch = Orchestrator()
    try:
        orch.start()
    except Exception:
        traceback.print_exc(file=sys.stderr)
    finally:
        orch.stop()


if __name__ == "__main__":
    main()
