import unittest

from campusflow.reports import generate_report


class TestTicketReports(unittest.TestCase):

    def test_empty_report(self):
        report = generate_report([])

        self.assertEqual(report["total"], 0)

        self.assertEqual(
            report["by_status"],
            {
                "open": 0,
                "in_progress": 0,
                "resolved": 0,
            },
        )

        self.assertEqual(
            report["by_priority"],
            {
                "critical": 0,
                "high": 0,
                "medium": 0,
                "low": 0,
            },
        )

    def test_report_counts_status_and_priority(self):
        tickets = [
            {
                "id": "T001",
                "status": "open",
                "priority": "critical",
            },
            {
                "id": "T002",
                "status": "in_progress",
                "priority": "high",
            },
            {
                "id": "T003",
                "status": "resolved",
                "priority": "low",
            },
            {
                "id": "T004",
                "status": "open",
                "priority": "high",
            },
        ]

        report = generate_report(tickets)

        self.assertEqual(report["total"], 4)

        self.assertEqual(
            report["by_status"]["open"],
            2,
        )

        self.assertEqual(
            report["by_status"]["in_progress"],
            1,
        )

        self.assertEqual(
            report["by_status"]["resolved"],
            1,
        )

        self.assertEqual(
            report["by_priority"]["critical"],
            1,
        )

        self.assertEqual(
            report["by_priority"]["high"],
            2,
        )

        self.assertEqual(
            report["by_priority"]["low"],
            1,
        )


if __name__ == "__main__":
    unittest.main()