import unittest

from ticket_create import create_ticket, tickets
from assign import assign_ticket


class TestTicketAssignment(unittest.TestCase):

    def setUp(self):
        tickets.clear()

        self.ticket = create_ticket(
            title="Printer not working",
            category="Hardware",
            urgency="medium",
            affected_users=3
        )

    def test_assign_ticket_successfully(self):
        result = assign_ticket(
            self.ticket["id"],
            "Chinedu"
        )

        self.assertIsNotNone(result)
        self.assertEqual(result["assigned_to"], "Chinedu")

    def test_ticket_does_not_disappear_after_assignment(self):
        assign_ticket(self.ticket["id"], "Chinedu")

        self.assertEqual(len(tickets), 1)

    def test_assign_nonexistent_ticket(self):
        result = assign_ticket("T999", "Chinedu")

        self.assertIsNone(result)

    def test_assignment_uses_correct_ticket(self):
        result = assign_ticket(
            self.ticket["id"],
            "Chinedu"
        )

        self.assertEqual(result["id"], self.ticket["id"])


if __name__ == "__main__":
    unittest.main()