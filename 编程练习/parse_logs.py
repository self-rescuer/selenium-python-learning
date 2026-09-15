def parse_logs(logs):
    Newlogs = []
    result = {}
    total = 0
    info_count = 0
    error_count = 0
    user_ids = []
    errors = []
    for log in logs:
        Newlogs.append(log.split(' '))
    for log in Newlogs:
        total += 1
        if log[2] == 'INFO':
            info_count += 1
        else:
            error_count += 1
            errors.append(log[3])
        if log[4].split('=')[1] not in user_ids:
            user_ids.append(log[4].split('=')[1])
    result['total'] = total
    result['info_count'] = info_count
    result['error_count'] = error_count
    result['errors'] = errors
    result['user_ids'] = user_ids
    return result


logs1 = [
    "2026-09-15 10:23:45 INFO 用户登录成功 user_id=1001",
    "2026-09-15 10:24:12 ERROR 数据库连接失败 user_id=1002",
    "2026-09-15 10:24:30 INFO 订单创建成功 user_id=1001",
    "2026-09-15 10:25:00 ERROR 请求超时 user_id=1003"
]

print(parse_logs(logs1))
