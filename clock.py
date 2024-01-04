import time

def focus_timer(duration_minutes):
    duration_seconds = duration_minutes * 60
    start_time = time.time()

    print(f"专注时钟已启动，将持续 {duration_minutes} 分钟.")

    while True:
        elapsed_time = time.time() - start_time
        remaining_time = max(0, duration_seconds - elapsed_time)
        
        minutes, seconds = divmod(remaining_time, 60)
        time_format = "{:02}:{:02}".format(int(minutes), int(seconds))

        print(f"剩余时间: {time_format}", end="\r")

        if elapsed_time >= duration_seconds:
            break

        time.sleep(1)

    print("\n专注时钟结束！")

if __name__ == "__main__":
    focus_duration = int(input("请输入专注时长（分钟）: "))
    focus_timer(focus_duration)
