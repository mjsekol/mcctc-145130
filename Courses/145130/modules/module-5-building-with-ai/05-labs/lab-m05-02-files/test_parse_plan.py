# test_parse_plan.py  .  Lab M05-02, Parse What The Model Said
#
# These tests are already written. Your job is to make them pass by writing
# parse_plan.py. Do not change this file.
#
# Why the tests come first: you are building a parser against ten answers a
# model really produced, and every one of them is a different kind of mess.
# Deciding what "correct" means after you look at your own output is how you
# end up with a parser that agrees with itself and nothing else.
#
#   python test_parse_plan.py
#   python test_parse_plan.py -v
#
# Standard library only. Nothing here starts a server or needs a model.

import os
import unittest

import parse_plan

ANSWERS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "answers")


def answer(name):
    """The text of one captured model answer."""
    with open(os.path.join(ANSWERS, name), "r", encoding="utf-8") as handle:
        return handle.read()


class TestAnswersThatWork(unittest.TestCase):
    """Six answers that carry a usable plan, in six different wrappings."""

    def check(self, filename, title, steps, minutes):
        plan = parse_plan.parse_study_plan(answer(filename))
        self.assertIsNotNone(plan, f"{filename} should parse into a plan")
        self.assertEqual(plan["title"], title)
        self.assertEqual(plan["steps"], steps)
        self.assertEqual(plan["minutes"], minutes)
        self.assertIsNone(parse_plan.validate_study_plan(plan),
                          f"{filename} should pass validation")

    def test_plain_json(self):
        self.check("01_plain_json.txt", "Chemistry unit 4 catch-up", [
            "Re-read the mole conversion notes",
            "Redo problems 7 to 14",
            "Check answers against the key",
        ], 45)

    def test_fenced_json(self):
        self.check("02_fenced_json.txt", "Chemistry unit 4 catch-up", [
            "Re-read the mole conversion notes",
            "Redo problems 7 to 14",
            "Check answers against the key",
        ], 45)

    def test_json_after_a_sentence(self):
        self.check("03_preamble_json.txt", "Algebra 2 quiz prep", [
            "Copy the three worked examples",
            "Do the odd problems on page 212",
            "Write down every step you had to look up",
        ], 40)

    def test_prose_with_labels_and_bullets(self):
        self.check("04_prose_labelled.txt", "Physics lab report finish", [
            "Paste the data table into the report",
            "Write the error analysis paragraph",
            "Read the whole thing out loud once",
        ], 60)

    def test_prose_with_numbered_steps(self):
        self.check("05_numbered_steps.txt", "Welding portfolio photos", [
            "Photograph the four finished coupons on the blue mat",
            "Crop each photo to square and name it by joint type",
            "Write two sentences under each photo saying what you would redo",
        ], 35)

    def test_minutes_written_as_words(self):
        self.check("06_minutes_as_text.txt", "Spanish 3 vocabulary", [
            "Write the 20 unit words on cards",
            "Say each one out loud twice",
            "Sort the cards into knew it and did not",
        ], 25)


class TestAnswersThatDoNotWork(unittest.TestCase):
    """Four answers that must not reach the rest of the program."""

    def test_a_refusal_parses_to_nothing(self):
        plan = parse_plan.parse_study_plan(answer("07_refusal.txt"))
        self.assertIsNone(plan, "a refusal carries no plan, so parsing gives None")

    def test_a_refusal_fails_validation_with_a_reason(self):
        reason = parse_plan.validate_study_plan(
            parse_plan.parse_study_plan(answer("07_refusal.txt")))
        self.assertIsInstance(reason, str)
        self.assertNotEqual(reason.strip(), "")

    def test_one_step_is_not_a_plan(self):
        plan = parse_plan.parse_study_plan(answer("08_one_step.txt"))
        self.assertIsNotNone(plan, "this answer parses. It is the rules it fails.")
        self.assertEqual(plan["steps"], ["Outline the three branches"])
        reason = parse_plan.validate_study_plan(plan)
        self.assertIsInstance(reason, str, "one step should be rejected by validation")

    def test_ten_hours_is_not_a_study_session(self):
        plan = parse_plan.parse_study_plan(answer("09_minutes_out_of_range.txt"))
        self.assertIsNotNone(plan)
        self.assertEqual(plan["minutes"], 600)
        reason = parse_plan.validate_study_plan(plan)
        self.assertIsInstance(reason, str, "600 minutes should be rejected")

    def test_right_json_wrong_field_names(self):
        plan = parse_plan.parse_study_plan(answer("10_wrong_keys.txt"))
        reason = parse_plan.validate_study_plan(plan)
        self.assertIsInstance(reason, str,
                              "valid JSON with the wrong field names is not a plan")


class TestTheRulesThemselves(unittest.TestCase):
    """The contract, checked without any captured answer."""

    def test_empty_text_parses_to_nothing(self):
        self.assertIsNone(parse_plan.parse_study_plan(""))
        self.assertIsNone(parse_plan.parse_study_plan("   \n  "))

    def test_something_that_is_not_text(self):
        self.assertIsNone(parse_plan.parse_study_plan(None))

    def test_a_good_plan_passes(self):
        self.assertIsNone(parse_plan.validate_study_plan(
            {"title": "Fine", "steps": ["one", "two"], "minutes": 30}))

    def test_no_title_fails(self):
        self.assertIsInstance(parse_plan.validate_study_plan(
            {"title": "", "steps": ["one", "two"], "minutes": 30}), str)

    def test_minutes_must_be_a_number(self):
        self.assertIsInstance(parse_plan.validate_study_plan(
            {"title": "Fine", "steps": ["one", "two"], "minutes": "thirty"}), str)

    def test_too_many_steps_fails(self):
        self.assertIsInstance(parse_plan.validate_study_plan(
            {"title": "Fine", "steps": [f"step {n}" for n in range(20)], "minutes": 30}), str)

    def test_steps_are_capped_not_dropped(self):
        many = "\n".join(f"- step {n}" for n in range(20))
        plan = parse_plan.parse_study_plan("Title: Long one\n" + many + "\nMinutes: 30")
        self.assertLessEqual(len(plan["steps"]), 8,
                             "the parser trims to the field limit before anyone validates")

    def test_a_long_step_is_shortened_not_refused(self):
        long_step = "x" * 500
        plan = parse_plan.parse_study_plan(
            'Title: Long step\n- ' + long_step + '\n- second step\nMinutes: 20')
        self.assertLessEqual(len(plan["steps"][0]), 160)

    def test_the_fallback_is_always_usable(self):
        plan = parse_plan.fallback_study_plan("I have a chemistry test on Friday")
        self.assertIsNone(parse_plan.validate_study_plan(plan),
                          "a fallback that fails validation is worse than no fallback")


if __name__ == "__main__":
    unittest.main(verbosity=2)
