from building import count_types, validate_arguments

# ──────────────────────────────────────────────────────────────
#  Tests for count_types
# ──────────────────────────────────────────────────────────────


def test_empty_string():
    assert count_types("") == {}, "empty string should return empty dict"


def test_only_uppercase():
    result = count_types("ABC")
    assert result == {"upper": 3}, f"expected upper:3, got {result}"


def test_only_lowercase():
    result = count_types("abc")
    assert result == {"lower": 3}, f"expected lower:3, got {result}"


def test_only_digits():
    result = count_types("123")
    assert result == {"digits": 3}, f"expected digits:3, got {result}"


def test_only_spaces():
    result = count_types("   ")
    assert result == {"spaces": 3}, f"expected spaces:3, got {result}"


def test_only_punctuation():
    result = count_types("!@#")
    assert result == {"punctuation": 3}, f"expected punctuation:3, got {result}"


def test_tabs_count_as_spaces():
    result = count_types("\t\t")
    assert result == {"spaces": 2}, f"tabs should count as spaces, got {result}"


def test_newlines_count_as_spaces():
    result = count_types("\n\n")
    assert result == {"spaces": 2}, f"newlines should count as spaces, got {result}"


def test_mixed_text():
    result = count_types("Hello World! 123")
    assert result == {
        "upper": 2,
        "lower": 8,
        "spaces": 2,
        "punctuation": 1,
        "digits": 3,
    }, f"mixed text failed, got {result}"


def test_all_character_types():
    result = count_types("Aa1 !")
    assert result["upper"] == 1
    assert result["lower"] == 1
    assert result["digits"] == 1
    assert result["spaces"] == 1
    assert result["punctuation"] == 1


def test_missing_keys_not_present():
    result = count_types("abc")
    assert "upper" not in result, "upper should not be in result"
    assert "digits" not in result, "digits should not be in result"
    assert "spaces" not in result, "spaces should not be in result"
    assert "punctuation" not in result, "punctuation should not be in result"


def test_single_characters():
    assert count_types("A") == {"upper": 1}
    assert count_types("a") == {"lower": 1}
    assert count_types("0") == {"digits": 1}
    assert count_types(" ") == {"spaces": 1}
    assert count_types(".") == {"punctuation": 1}


# ──────────────────────────────────────────────────────────────
#  Tests for validate_arguments
# ──────────────────────────────────────────────────────────────


def test_single_argument():
    assert validate_arguments(["Hello"]) == "Hello"


def test_single_argument_with_spaces():
    assert validate_arguments(["Hello World"]) == "Hello World"


def test_multiple_arguments_raises():
    try:
        validate_arguments(["arg1", "arg2"])
        assert False, "should have raised AssertionError"
    except AssertionError:
        pass


def test_three_arguments_raises():
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
