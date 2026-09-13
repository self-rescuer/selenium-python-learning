class AssertUtils:
    """接口测试常用断言工具类"""

    @staticmethod
    def assert_status_code(response, expected_code):
        actual = response.status_code
        assert actual == expected_code, \
            f"状态码错误：期望 {expected_code}，实际 {actual}"

    @staticmethod
    def assert_key_exists(data, key):
        assert key in data, \
            f"字段 '{key}' 不存在，实际字段：{list(data.keys())}"

    @staticmethod
    def assert_value_equal(data, key, expected_value):
        actual = data.get(key)
        assert actual == expected_value, \
            f"字段 '{key}' 期望值 {expected_value}，实际值 {actual}"

    @staticmethod
    def assert_type(data, key, expected_type):
        actual = data.get(key)
        assert isinstance(actual, expected_type), \
            f"字段 '{key}' 期望类型 {expected_type.__name__}，实际类型 {type(actual).__name__}"

    @staticmethod
    def assert_contains(container, item):
        assert item in container, f"期望包含 {item}，实际内容：{container}"