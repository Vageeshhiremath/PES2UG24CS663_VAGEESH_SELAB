# test_processor.py
from hypothesis import given, strategies as st, settings
from processor import sanitize_string, parse_int_list, is_palindrome


ANY_INPUT = st.one_of(
    st.none(), st.text(), st.integers(), st.booleans(), st.lists(st.integers())
)


@settings(max_examples=300)
@given(ANY_INPUT)
def test_sanitize_string_is_total_and_idempotent(value):
    result = sanitize_string(value)
    assert isinstance(result, str)
    if isinstance(value, str):
        assert result == value.strip().strip("!").strip()
        assert sanitize_string(result) == result
    else:
        assert result == ""


@settings(max_examples=300)
@given(ANY_INPUT)
def test_parse_int_list_is_total_and_returns_only_integers(value):
    result = parse_int_list(value)
    assert isinstance(result, list)
    assert all(type(item) is int for item in result)
    if not isinstance(value, str):
        assert result == []


@settings(max_examples=300)
@given(st.lists(st.integers(), max_size=50))
def test_parse_int_list_round_trips_valid_integer_lists(values):
    encoded = ",".join(str(value) for value in values)
    assert parse_int_list(encoded) == values


@settings(max_examples=300)
@given(ANY_INPUT)
def test_is_palindrome_is_total_and_returns_bool(value):
    result = is_palindrome(value)
    assert isinstance(result, bool)
    if not isinstance(value, str):
        assert result is False


@settings(max_examples=300)
@given(st.text())
def test_is_palindrome_is_invariant_under_reversal(value):
    assert is_palindrome(value) == is_palindrome(value[::-1])


# Deterministic regression tests for known edge cases
def test_parse_int_list_empty_elements():
    assert parse_int_list("1,,3") == [1, 3]


def test_parse_int_list_invalid_tokens():
    assert parse_int_list("one,two") == []


def test_sanitize_string_removes_whitespace_around_exclamation_marks():
    assert sanitize_string("  !! hello !!  ") == "hello"


def test_none_inputs():
    assert sanitize_string(None) == ""
    assert parse_int_list(None) == []
    assert is_palindrome(None) is False


def test_palindrome_ignores_case_and_punctuation():
    assert is_palindrome("A man, a plan, a canal: Panama!") is True
    assert is_palindrome("not a palindrome") is False


def test_palindrome_uses_unicode_casefolding():
    assert is_palindrome("ßss") is True
