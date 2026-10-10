import unittest
from unittest.mock import patch

from ticket_create import tickets
from ticket_list import find_ticket, list_tickets, view_ticket


class TestTicketList(unittest.TestCase):

    def setUp(self):
        tickets.clear()

        tickets.append({
            "id": "T001",
            "title": "Printer not working",
            "category": "Hardware",
            "urgency": "medium",
            "affected_users": 3,
            "priority": "medium",
            "status": "Open",
            "assigned_to": None
        })

    def test_find_existing_ticket(self):
        result = find_ticket("T001")

        self.assertEqual(result["id"], "T001")
        self.assertEqual(result["title"], "Printer not working")

    def test_find_nonexistent_ticket(self):
        result = find_ticket("T999")

        self.assertIsNone(result)

    def test_find_ticket_with_lowercase_id(self):
        result = find_ticket("t001")

        self.assertIsNotNone(result)
        self.assertEqual(result["id"], "T001")

    
    def test_list_tickets_when_empty(self):
        tickets.clear()

        with patch("builtins.print") as mock_print:
            list_tickets()

        mock_print.assert_any_call(
            "No tickets have been created yet."
        )

    def test_view_nonexistent_ticket(self):
        with patch("builtins.input", return_value="T999"):
            with patch("builtins.print") as mock_print:
                view_ticket()

        mock_print.assert_any_call("Ticket ID not found.")


if __name__ == "__main__":
    unittest.main()