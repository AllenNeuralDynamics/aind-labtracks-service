"""Tests validators in models module"""

import unittest
from unittest.mock import MagicMock, patch

from pydantic import ValidationError

from aind_labtracks_service_server.models import (
    MouseCustomClass,
    SexNames,
    SpeciesNames,
    Subject,
    Procedure,
)


class TestSubject(unittest.TestCase):
    """Test validators in Subject class"""

    def test_parse_xml_string(self):
        """Tests xml string parsed correctly"""

        valid_string = (
            '<?xml version="1.0" encoding="utf-16"?>\r\n'
            "<MouseCustomClass"
            ' xmlns:xsd="http://www.w3.org/2001/XMLSchema"'
            ' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">\r\n'
            "  <Reserved_by>Anna Apple</Reserved_by>\r\n"
            "  <Reserve_Date>2022-07-21T00:00:00-07:00</Reserve_Date>\r\n"
            "  <Solution>1xPBS</Solution>\r\n"
            "  <Full_Genotype>Adora2a-Cre/wt</Full_Genotype>\r\n"
            "</MouseCustomClass>"
        )
        example_string = (
            '<?xml version="1.0" encoding="utf-16"?>\r\n'
            "<MouseCustomClass"
            ' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"'
            ' xmlns:xsd="http://www.w3.org/2001/XMLSchema">\r\n'
            "  <Reserved_by></Reserved_by>\r\n"
            "  <Reserve_Date>2017-08-18T00:00:00-07:00</Reserve_Date>\r\n"
            "  <Reason>EU-Retire</Reason>\r\n"
            "  <ExtraField>test</ExtraField>\r\n"
            "</MouseCustomClass>"
        )
        corrupt_string = "Corrupted xml string"
        with self.assertLogs() as captured:
            lab_tracks_subject = Subject(
                id="123456",
                sex=SexNames.MALE,
                class_values=valid_string,
                species_name=SpeciesNames.MOUSE,
                paternal_id="123455",
                paternal_class_values=example_string,
                maternal_id="123454",
                maternal_class_values=corrupt_string,
            )
        expected_subject = Subject(
            id="123456",
            sex=SexNames.MALE,
            class_values=MouseCustomClass(
                reserved_by="Anna Apple",
                reserved_date="2022-07-21T00:00:00-07:00",
                solution="1xPBS",
                full_genotype="Adora2a-Cre/wt",
            ),
            species_name=SpeciesNames.MOUSE,
            paternal_id="123455",
            paternal_class_values=MouseCustomClass(
                reserved_date="2017-08-18T00:00:00-07:00",
                reason="EU-Retire",
            ),
            maternal_id="123454",
        )
        self.assertEqual(
            ["WARNING:root:XML parsing error: syntax error: line 1, column 0"],
            captured.output,
        )
        self.assertEqual(expected_subject, lab_tracks_subject)

    @patch("aind_labtracks_service_server.models.MouseCustomClass.from_xml")
    def test_parse_xml_string_validation_errors(
        self, mock_parse_xml: MagicMock
    ):
        """Tests edge case where pydantic raises validation issues"""

        # Mock parse_xml to raise a Validation Error.
        mock_parse_xml.side_effect = ValidationError.from_exception_data(
            "Invalid data", line_errors=[]
        )

        with self.assertLogs() as captured:
            lab_tracks_subject = Subject(
                id=123456,
                class_values="<some_xml></some_xml>",
            )
        self.assertEqual(Subject(id=123456), lab_tracks_subject)
        self.assertEqual(
            ["WARNING:root:Pydantic validation error: []"], captured.output
        )

    @patch("aind_labtracks_service_server.models.MouseCustomClass.from_xml")
    def test_parse_xml_string_exception(self, mock_parse_xml: MagicMock):
        """Tests edge case where an exception happens"""

        # Mock parse_xml to raise a Validation Error.
        mock_parse_xml.side_effect = Exception("Something went wrong")

        with self.assertLogs() as captured:
            lab_tracks_subject = Subject(
                id=123456,
                class_values="<some_xml></some_xml>",
            )
        self.assertEqual(Subject(id=123456), lab_tracks_subject)
        self.assertEqual(
            [
                "ERROR:root:Something went wrong parsing "
                "<some_xml></some_xml>: ('Something went wrong',)"
            ],
            captured.output,
        )

    def test_parse_xml_string_edge_case(self):
        """Tests edge case where input is not a string"""

        lab_tracks_subject = Subject(
            id=123456,
            class_values=0,
        )
        self.assertEqual(Subject(id=123456), lab_tracks_subject)


class TestProcedure(unittest.TestCase):
    """Test validators in Procedure class"""

    def test_parse_task_description(self):
        raw = (
            'Create cages in a \"Surgical Group\" in LT.'
            ' Prep per LASWI-0021 Surgical Cage Preparation.\r\n\r\n    '
            'Ear Notch and Tattoo Confirmation (__) Does cage need a change flag? (___)'
            ' Entered into Post-operative observation sheet?  (__)'
        )
        expected = (
            'Create cages in a "Surgical Group" in LT.'
            ' Prep per LASWI-0021 Surgical Cage Preparation.'
            ' Ear Notch and Tattoo Confirmation (__) Does cage need a change flag? (___)'
            ' Entered into Post-operative observation sheet? (__)'
        )
        proc = Procedure(
            id=1,
            type_name="Test",
            date_start=None,
            date_end=None,
            investigator_id=None,
            task_name=None,
            task_description=raw,
            task_object=None,
            protocol_number=None,
            protocol_title=None,
            task_status=None,
        )
        self.assertEqual(proc.task_description, expected)

    def test_parse_task_description_none(self):
        proc = Procedure(
            id=1,
            type_name="Test",
            date_start=None,
            date_end=None,
            investigator_id=None,
            task_name=None,
            task_description=None,
            task_object=None,
            protocol_number=None,
            protocol_title=None,
            task_status=None,
        )
        self.assertIsNone(proc.task_description)


if __name__ == "__main__":
    unittest.main()
