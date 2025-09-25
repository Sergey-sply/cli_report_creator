import argparse
from tabulate import tabulate

from src.reader.csv_reader import CSVReader
from src.reporter import Reporter


def build_argparser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser()

    ap.add_argument(
        "--files",
        nargs="+",
        required=True,
    )

    ap.add_argument(
        "--report",
        required=True,
    )
    return ap



def main(argv: list[str] | None = None) -> None:
    parser = build_argparser()
    args = parser.parse_args(argv)

    reader = CSVReader()
    try:
        students_data = reader.read(args.files)

        if not students_data:
            print("[WARNING] No data in files")
            return

        reporter = Reporter.get(args.report)

        report = reporter.build_report(students_data)

        print(tabulate(report, headers="keys", tablefmt="grid", floatfmt=".1f"))

    except Exception as e:
        print(f"[ERROR] {e}")

    return

if __name__ == "__main__":
    raise SystemExit(main())
