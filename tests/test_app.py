import unittest

from src.app import activities, signup_for_activity


class GitHubSkillsActivityTests(unittest.TestCase):
    def setUp(self):
        activities["GitHub Skills"]["participants"].clear()

    def test_github_skills_activity_is_available(self):
        activity = activities.get("GitHub Skills")

        self.assertIsNotNone(activity)
        self.assertEqual(
            activity["description"],
            "Learn practical coding and collaboration skills through GitHub.",
        )
        self.assertEqual(
            activity["schedule"],
            "Schedule to be confirmed",
        )
        self.assertEqual(activity["max_participants"], 20)
        self.assertEqual(activity["participants"], [])

    def test_github_skills_activity_accepts_student_signup(self):
        student_email = "student@mergington.edu"
        activity = activities["GitHub Skills"]
        activity["participants"].clear()

        result = signup_for_activity("GitHub Skills", student_email)

        self.assertEqual(result["message"], f"Signed up {student_email} for GitHub Skills")
        self.assertIn(student_email, activity["participants"])


if __name__ == "__main__":
    unittest.main()
