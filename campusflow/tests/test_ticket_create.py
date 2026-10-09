import unittest
from ticket_create import create_ticket, tickets


class TestTicketCreation(unittest.TestCase):

    def setUp(self):
        tickets.clear()

    def test_create_ticket_successfully(self):
        ticket = create_ticket(
            title="Internet not working",
            category="Network",
            urgency="high",
            affected_users=12
        )

        self.assertIsNotNone(ticket)
        self.assertEqual(ticket["title"], "Internet not working")
        self.assertEqual(ticket["category"], "Network")
        self.assertEqual(ticket["urgency"], "high")
        self.assertEqual(ticket["affected_users"], 12)

    def test_ticket_has_an_id(self):
        ticket = create_ticket(
            title="Computer failure",
            category="Hardware",
            urgency="medium",
            affected_users=2
        )

        self.assertIn("id", ticket)
        self.assertTrue(ticket["id"].startswith("T"))

    def test_ticket_is_saved(self):
        create_ticket(
            title="Network failure",
            category="Network",
            urgency="high",
            affected_users=12
        )

        self.assertEqual(len(tickets), 1)

    def test_blank_title_is_rejected(self):
        with self.assertRaises(ValueError):
            create_ticket(
                title="",
                category="Network",
                urgency="high",
                affected_users=12
            )


if __name__ == "__main__":
    unittest.main()