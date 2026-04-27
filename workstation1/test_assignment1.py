from typing import List
from pathlib import Path
from unittest.mock import patch
from pytest import mark
from assignment1sol import dna_match, collect_email_from_text


@mark.parametrize(
    "dna, expected",
    [
        ("AAA", True),  # Test neither p1 nor p2
        ("AATGATTT", True),  # Test neither p1 nor p2 (extra)
        ("TTAGGCTA", True),  # Test no p1, but p2 (extra)
        ("AATTTAZGGCTA", False),  # Test wrong symbol in middle (extra)
        ("AATTTAGGCTAZAA", False),  # Test wrong symbol after (extra)
        ("AATTTA", False),  # Test p1, but no p2
        ("AATTTAGGCTA", True),  # Test p1 and p2 nothing in between
        ("AATTTATACGGGCTA", True),  # Test p1 and p2; 3 symbols in between
        ("AATTTATTTTTTTTTTGGCTA", True),  # Test p1 and p2; 10 symbols in between
        ("AATTTATTTTTTTTTTTGGCTA", False),  # Test p1 and p2; 11 symbols in between
        (
            "AATTTATTTTTTTTTTTCGGCTA",
            False,
        ),  # Test p1 and p2; 12 symbols in between (extra)
        (
            "AATTTATTTTTTTTGGGTTTGGCTA",
            False,
        ),  # Test p1 and p2; 14 symbols in between (extra)
        ("AATTTAATTTAGGCTA", True),  # Test 2 interleved p1 with 1 p2
        ("AATTTAGGCTAAATTTA", False),  # Test 2 p1 but not every p1 has a match (extra)
        ("AATTTATTTTTTTTTTTTTTAATTTAGGCTA", False),  # Test 2 p1 but not every p1 has a match (extra)
        (
            "AATTTAGGCTAAATTTAGGCTA",
            True,
        ),  # Test multiple p1 and every p1 has a match (extra)
        (
            "AATTTAGGCTAAATTTACGGCTACCAATTTAC",
            False,
        ),  # Test 3 p1 but not every p1 has a match (extra)
        ("AATTTAGGCTATTTTAAAGGCTA", True),  # Test p2 more than p1 (extra)
        ("GGAATTTAGGCTA", True),  # Test dna does not begin with p1 (extra)
        ("AATTTAGGCTAAAT", True),  # Test dna does not end with p2 (extra)
    ],
)
def test_dna_match(record_property, dna: str, expected: bool) -> None:
    record_property("input", dna)
    record_property("expected", expected)
    record_property("output", dna_match(dna))
    assert dna_match(dna) is expected


@mark.parametrize(
    "content, emails",
    [
        ("", []),
        ("___e--mail@123.123.123.123", ["___e--mail@123.123.123.123"]),
        ('"john"@doe.com', ['"john"@doe.com']),
        ("email@-domain.com", []),
        ("email@domain..com", []),
        ("e..mail@domain..com", []),
        (".email@domain.com", ["email@domain.com"]),
        ("<b>email me on</b><em>john@doe.com</em>", ["john@doe.com"]),
        ("This is valid also john.doe+1@gmail.com", ["john.doe+1@gmail.com"]),
        (
            "you have jane@do-e-e.uk.com but als john@this.be, although not me@this",
            ["jane@do-e-e.uk.com", "john@this.be"],
        ),
    ],
)
def test_collect_email_from_text(
    record_property, tmp_path: Path, content: str, emails: List[str]
) -> None:
    record_property("input", content)
    # record_property("expected", ", ".join(emails))
    record_property("expected", emails)

    log_file = tmp_path / "log.txt"
    with patch("assignment1sol.collect_email_from_text"):
        output = collect_email_from_text(content, log_file.as_posix())
    expected_result = "\n".join(
        [f"The number of emails extracted is {len(emails)}"] + emails
    )
    # record_property("output", ", ".join(output))
    record_property("output", output)
    assert log_file.read_text() == expected_result
