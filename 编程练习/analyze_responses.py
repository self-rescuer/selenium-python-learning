def analyze_responses(responses):
    total=len(responses)
    success_count=0
    fail_count=0
    success_time=0
    for i in range(len(responses)):
        if responses[i]['status_code']==200:
            success_count+=1
            success_time+=responses[i]['response_time']
        else:
            fail_count+=1
    if success_count > 0:
        avg_success_time = round(success_time / success_count, 2)
    else:
        avg_success_time = 0
    result={
        'total':total,
        'success_count':success_count,
        'fail_count':fail_count,
        'avg_success_time':avg_success_time,
    }
    return result
response = [
    {"url": "/users/octocat", "status_code": 200, "response_time": 0.35},
    {"url": "/users/torvalds", "status_code": 200, "response_time": 0.42},
    {"url": "/users/notexist", "status_code": 404, "response_time": 0.18},
    {"url": "/repos", "status_code": 200, "response_time": 0.55},
    {"url": "/error", "status_code": 500, "response_time": 0.90}
]

print(analyze_responses(response))



