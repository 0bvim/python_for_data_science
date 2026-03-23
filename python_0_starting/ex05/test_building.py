from building import count_types, validate_arguments

# ──────────────────────────────────────────────────────────────
#  Tests for count_types
# ──────────────────────────────────────────────────────────────


def test_empty_string():
    """Test if an empty string returns an empty dictionary."""
    assert count_types("") == {}, "empty string should return empty dict"


def test_only_uppercase():
    """Test if a string with only uppercase letters is correctly counted."""
    result = count_types("ABC")
    assert result == {"upper": 3}, f"expected upper:3, got {result}"


def test_only_lowercase():
    """Test if a string with only lowercase letters is correctly counted."""
    result = count_types("abc")
    assert result == {"lower": 3}, f"expected lower:3, got {result}"


def test_only_digits():
    """Test if a string with only digits is correctly counted."""
    result = count_types("123")
    assert result == {"digits": 3}, f"expected digits:3, got {result}"


def test_only_spaces():
    """Test if a string with only spaces is correctly counted."""
    result = count_types("   ")
    assert result == {"spaces": 3}, f"expected spaces:3, got {result}"


def test_only_punctuation():
    """Test if a string with only punctuation is correctly counted."""
    result = count_types("!@#")
    assert result == {"punctuation": 3}, f"expected punctuation:3, \
    got {result}"


def test_tabs_count_as_spaces():
    """Test if tabs are counted as spaces."""
    result = count_types("\t\t")
    assert result == {"spaces": 2}, f"tabs should count as spaces, \
    got {result}"


def test_newlines_count_as_spaces():
    """Test if newlines are counted as spaces."""
    result = count_types("\n\n")
    assert result == {"spaces": 2}, f"newlines should count as spaces, \
    got {result}"


def test_mixed_text():
    """Test if a mixed string of characters is correctly counted."""
    result = count_types("Hello World! 123")
    assert result == {
        "upper": 2,
        "lower": 8,
        "spaces": 2,
        "punctuation": 1,
        "digits": 3,
    }, f"mixed text failed, got {result}"


def test_all_character_types():
    """Test if all character types are identified in a single string."""
    result = count_types("Aa1 !")
    assert result["upper"] == 1
    assert result["lower"] == 1
    assert result["digits"] == 1
    assert result["spaces"] == 1
    assert result["punctuation"] == 1


def test_missing_keys_not_present():
    """Test if result only contains keys for character types present in string."""
    result = count_types("abc")
    assert "upper" not in result, "upper should not be in result"
    assert "digits" not in result, "digits should not be in result"
    assert "spaces" not in result, "spaces should not be in result"
    assert "punctuation" not in result, "punctuation should not be in result"


def test_single_characters():
    """Test each character type individually."""
    assert count_types("A") == {"upper": 1}
    assert count_types("a") == {"lower": 1}
    assert count_types("0") == {"digits": 1}
    assert count_types(" ") == {"spaces": 1}
    assert count_types(".") == {"punctuation": 1}


# ──────────────────────────────────────────────────────────────
#  Tests for validate_arguments
# ──────────────────────────────────────────────────────────────


def test_single_argument():
    """Test if a single argument is returned correctly."""
    assert validate_arguments(["Hello"]) == "Hello"


def test_single_argument_with_spaces():
    """Test if a single argument with spaces is returned correctly."""
    assert validate_arguments(["Hello World"]) == "Hello World"


def test_multiple_arguments_raises():
    """Test if multiple arguments raise an AssertionError."""
    try:
        validate_arguments(["arg1", "arg2"])
        assert False, "should have raised AssertionError"
    except AssertionError:
        pass


def test_three_arguments_raises():
    """Test if three arguments raise an AssertionError."""
    try:
        validate_arguments(["a", "b", "c"])
        assert False, "should have raised AssertionError"
    except AssertionError:
        pass


# ──────────────────────────────────────────────────────────────
#  Run all tests
# ──────────────────────────────────────────────────────────────

if __name__ == "__main__":
    tests = [
        test_empty_string,
        test_only_uppercase,
        test_only_lowercase,
        test_only_digits,
        test_only_spaces,
        test_only_punctuation,
        test_tabs_count_as_spaces,
        test_newlines_count_as_spaces,
        test_mixed_text,
        test_all_character_types,
        test_missing_keys_not_present,
        test_single_characters,
        test_single_argument,
        test_single_argument_with_spaces,
        test_multiple_arguments_raises,
        test_three_arguments_raises,
    ]

    passed = 0
    failed = 0
    for test in tests:
        try:
            test()
            passed += 1
            print(f"  ✅ {test.__name__}")
        except AssertionError as e:
            failed += 1
            print(f"  ❌ {test.__name__}: {e}")

    print(f"\n{'=' * 40}")
    print(f"  {passed} passed, {failed} failed, {len(tests)} total")
    if failed == 0:
        print("  All tests passed! 🎉")
    else:
        print("  Some tests failed.")
