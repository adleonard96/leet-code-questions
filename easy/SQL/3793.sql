/* Write your T-SQL query statement below */
SELECT user_id, prompt_count, avg_tokens FROM (
SELECT DISTINCT user_id, count(*) over (partition by user_id) prompt_count, round(avg(cast(tokens as float)) over (partition by user_id), 2) avg_tokens, max(tokens) over (partition by user_id) highest_token from prompts) f where prompt_count >= 3 and highest_token > avg_tokens
order by avg_tokens desc, user_id asc 