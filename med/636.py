class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        times = []
        ans = []
        jobs = {}
        for i in range(len(logs)):
            if logs[i].split(":")[1] == "start":
                times.append([logs[i], 0])
            else:
                stack_val = times.pop()
                wait = stack_val[1]
                start = int(stack_val[0].split(":")[-1])
                end = int(logs[i].split(":")[-1])
                job = int(logs[i].split(":")[0])
                start -= 1
                job_time = end - start - wait

                if job in jobs:
                    ans[jobs[job]] += job_time
                else:
                    ans.append(job_time)
                    jobs[job] = len(ans) - 1
                for time in times:
                    time[1] += job_time
        
        return ans


# failed question need to revisit