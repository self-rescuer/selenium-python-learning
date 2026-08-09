from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get('https://baidu.com')

'获取当前主窗口句柄'
main_window=driver.current_window_handle
print(f'主窗口句柄：{main_window}')

'点击新闻链接'
news_link=driver.find_element(By.LINK_TEXT,'新闻')
news_link.click()
print('已点击新闻链接')

'等待新标签页加载'
time.sleep(2)


'获取所有窗口句柄'
all_windows=driver.window_handles
print(f'当前窗口数量：{len(all_windows)}')


'切换到新窗口'
driver.switch_to.window(all_windows[-1])
print(f'当前窗口标题:{driver.title}')

'切回主窗口'
driver.switch_to.window(main_window)
print(f'切回主窗口后标题{driver.title}')

time.sleep(2)
driver.quit()