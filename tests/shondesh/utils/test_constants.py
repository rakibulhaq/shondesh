import pytest
from shondesh.utils.constants import Severity


def returns_correct_value_for_info():
    assert Severity.INFO.value == "info"


def returns_correct_value_for_warning():
    assert Severity.WARNING.value == "warning"


def returns_correct_value_for_critical():
    assert Severity.CRITICAL.value == "critical"


def has_all_expected_severity_levels():
    expected_levels = {"info", "warning", "critical"}
    actual_levels = {severity.value for severity in Severity}
    assert actual_levels == expected_levels


def raises_attribute_error_for_invalid_severity():
    with pytest.raises(AttributeError):
        _ = Severity.INVALID
