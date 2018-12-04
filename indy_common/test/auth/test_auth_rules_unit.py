from indy_common.auth_rules import RuleAdd, RuleRemove


def test_allow_all(allow_all_dict):
    rule_cls, rule_dict = allow_all_dict
    rule = rule_cls(**rule_dict)
    assert rule.allow_new_value
    assert rule.allow_old_value
    assert rule.allow_field
    assert rule.allow_for_all


def test_not_allow_all(not_allow_all_dict):
    rule_cls, rule_dict = not_allow_all_dict
    rule = rule_cls(**rule_dict)
    assert not rule.allow_field
    assert not rule.allow_for_all


def test_rule_add_allows(dict_add):
    rule = RuleAdd(**dict_add)
    assert rule.allow_old_value is True


def test_rule_remove_allows(dict_remove):
    rule = RuleRemove(**dict_remove)
    assert rule.allow_old_value is True
    assert rule.allow_new_value is True


def test_make_rule_id_not_allow_all(not_allow_all_dict):
    rule_cls, rule_dict = not_allow_all_dict
    rule = rule_cls(**rule_dict)
    assert rule.rule_id == "SomeTxn--some_field--old_value--new_value"


def test_make_rule_id_allow_all(allow_all_dict):
    rule_cls, rule_dict = allow_all_dict
    rule = rule_cls(**rule_dict)
    assert rule.rule_id == "SomeTxn--*--*--*"
