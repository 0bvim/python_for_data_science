from Hello import ft_dict, ft_list, ft_set, ft_tuple, ordered_set


def test_data_types():
    """Verify each variable is the correct collection type."""
    assert isinstance(ft_list, list)
    assert isinstance(ft_tuple, tuple)
    assert isinstance(ft_set, set)
    assert isinstance(ft_dict, dict)


def test_set_conversion():
    """Verify the ordered_set is a list and contains the original elements."""
    assert isinstance(ordered_set, list)
    assert "Hello" in ordered_set
    assert "São Paulo!" in ordered_set
    assert len(ordered_set) == len(ft_set)


def test_dict_content():
    """Check specific key-value mapping."""
    assert ft_dict["Hello"] == "42SP!"


test_data_types()
test_set_conversion()
test_dict_content()
print("✅ success")
